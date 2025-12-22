from flask import Flask, render_template, request
import pickle
import numpy as np
import os

app = Flask(__name__)

# Correct model path
MODEL_PATH = os.path.join("notebooks", "models", "model.pkl")

# Load trained model
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

FEATURES = [
    'Age', 'Education', 'Marital Status', 'Parental Status', 'Children',
    'Income', 'Total_Spending', 'Days_as_Customer', 'Recency', 'Wines',
    'Fruits', 'Meat', 'Fish', 'Sweets', 'Gold', 'Web', 'Catalog',
    'Store', 'Discount Purchases', 'Total Promo', 'NumWebVisitsMonth'
]

@app.route("/", methods=["GET", "POST"])
def predict():
    prediction = None

    if request.method == "POST":
        input_data = [float(request.form[f]) for f in FEATURES]
        input_array = np.array(input_data).reshape(1, -1)

        prediction = model.predict(input_array)[0]

    return render_template(
        "index.html",
        features=FEATURES,
        prediction=prediction
    )

if __name__ == "__main__":
    app.run(debug=True)
