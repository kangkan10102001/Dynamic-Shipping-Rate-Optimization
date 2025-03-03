def predict_shipping_rate(weight, distance):
    # Example formula for shipping rate: (weight * 0.5) + (distance * 0.2)
    rate = (weight * 0.5) + (distance * 0.2)
    return round(rate, 2)  # Round to 2 decimal places for clarity
