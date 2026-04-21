from flask import Flask, render_template, request
import pickle
import numpy as np
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, 'car_price_model.pkl')

model = pickle.load(open(model_path, 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        engine = float(request.form['engine'])
        year = int(request.form['year'])
        mileage = int(request.form['mileage'])
        manufacturer = request.form['manufacturer']
        fuel = request.form['fuel']

        manufacturers = ['BMW', 'Ford', 'Porsche', 'Toyota', 'VW']
        fuels = ['Diesel', 'Hybrid', 'Petrol']

        manufacturer_values = [1 if manufacturer == m else 0 for m in manufacturers]
        fuel_values = [1 if fuel == f else 0 for f in fuels]

        final_input = np.array([[engine, year, mileage] + manufacturer_values + fuel_values])

        prediction = model.predict(final_input)

        return render_template(
            'index.html',
                prediction_text=f"Estimated Price: ${round(prediction[0], 2)}"        )

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)