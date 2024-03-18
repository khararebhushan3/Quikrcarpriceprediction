import pickle
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template

app = Flask(__name__, template_folder='templates')

# Load the model and preprocessed data
regmodel = pickle.load(open('regmodel.pkl', 'rb'))
car=pd.read_csv('Cleaned_Car_data.csv')
car=pd.read_csv('Cleaned_Car_data.csv')

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
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    try:
        # Validate and preprocess input data
        data = request.json['data']
        data, error = preprocess_input(data)
        if error:
            return jsonify({'error': error}), 400
        
        # Ensure the input data matches the column order of the preprocessed car data
        input_df = pd.DataFrame([data], columns=car.columns)
        
        # Make prediction
        output = regmodel.predict(input_df)
        
        return jsonify({'prediction': output[0]})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

#if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=8080)    