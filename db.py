import sqlite3

DB_FILE = "shipping_rates.db"

# Create database
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS rates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    weight REAL,
    distance REAL,
    rate REAL
)
""")

conn.commit()
conn.close()

print("Database and table created successfully.")
