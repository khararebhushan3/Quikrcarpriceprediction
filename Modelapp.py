import pickle
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.pipeline import Pipeline

app = Flask(__name__, template_folder='templates')

# Load the models and preprocessed data
model1 = pickle.load(open('model1.pkl', 'rb'))  # Assuming this is the Quantile Regressor model
model2 = pickle.load(open('model2.pkl', 'rb'))  # Assuming this is the Linear Regression model
car = pd.read_csv('Cleaned_Car_data.csv')

# Function to preprocess and validate input data
def preprocess_input(data):
    # Check if all required fields are present
    required_fields = ['Name', 'Company', 'Year', 'Kms_driven', 'Fuel_type']
    if not all(field in data for field in required_fields):
        return None, 'Missing required fields'
    
    # Validate numeric fields
    try:
        data['Year'] = int(data['Year'])
        data['Kms_driven'] = int(data['Kms_driven'])
    except ValueError:
        return None, 'Year and Kms driven must be numeric'

    return data, None

@app.route('/')
def home():
    car_names = car['Name'].unique().tolist()
    return render_template('home.html', car_names=car_names)

@app.route('/predict_api', methods=['POST'])
def predict_api():
    try:
        # Validate and preprocess input data
        data = request.form.to_dict()
        data, error = preprocess_input(data)
        if error:
            return jsonify({'error': error}), 400
        
        # Ensure the input data matches the column order of the preprocessed car data
        input_df = pd.DataFrame([data], columns=car.columns)
        
        # Make prediction using Model 2 (Linear Regression)
        predicted_price = model2.predict(input_df)[0]
        
        # Make prediction using Model 1 (Quantile Regressor) for estimating the 95% confidence interval
        quantile_predictions = {}
        for quantile, regressor in model1.items():
            quantile_predictions[quantile] = regressor.predict(input_df)[0]
        
        # Estimate the 95% confidence interval
        lower_bound = quantile_predictions[0.05]
        upper_bound = quantile_predictions[0.95]
        
        return jsonify({'Predicted Price': predicted_price, 'Lower Bound': lower_bound, 'Upper Bound': upper_bound})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
