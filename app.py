from flask import Flask, render_template, request, jsonify
import pandas as pd
import pickle
import sqlite3

app = Flask(__name__)

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Database connection
DB_FILE = "shipping_rates.db"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        weight = float(data.get("weight", 0))
        distance = float(data.get("distance", 0))

        if weight <= 0 or distance <= 0:
            return jsonify({"error": "Invalid input values"}), 400

        prediction = model.predict([[weight, distance]])[0]

        return jsonify({"shipping_rate": round(prediction, 2)})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/get_rates", methods=["GET"])
def get_rates():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM rates")
    data = cursor.fetchall()
    conn.close()

    return jsonify({"rates": data})

if __name__ == "__main__":
    app.run(debug=True)
