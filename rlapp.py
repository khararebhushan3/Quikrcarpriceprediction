import pickle
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template

app = Flask(__name__, template_folder='templates')

# Load the model and transformer
regmodel = pickle.load(open('regmodel.pkl', 'rb'))
#car = pickle.load(open('car.pkl', 'rb'))
car=pd.read_csv('Cleaned_Car_data.csv')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.json['data']
    # Ensure the input data matches the column order of the preprocessed car data
    input_df = pd.DataFrame([data], columns=car.columns)
    # Make prediction
    output = regmodel.predict(input_df)
    return jsonify(output[0])

if __name__ == "__main__":
    app.run(debug=True)
