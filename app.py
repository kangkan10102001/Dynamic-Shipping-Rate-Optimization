from flask import Flask, render_template, request
from model import predict_shipping_rate  # Import your prediction model

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    predicted_rate = None  # Default value for predicted rate

    if request.method == 'POST':
        # Get values from the form
        weight = float(request.form['weight'])  # Get weight input from form
        distance = float(request.form['distance'])  # Get distance input from form
        
        # Call your prediction function
        predicted_rate = predict_shipping_rate(weight, distance)  # Calculate the shipping rate

    # Render the template with the predicted rate
    return render_template('index.html', predicted_rate=predicted_rate)

if __name__ == "__main__":
    app.run(debug=True)
