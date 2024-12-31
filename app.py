import pickle
import pandas as pd
import numpy as np
from flask import Flask, request, render_template
from flask_cors import CORS
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import PredictPipeline, CustomData
from src.logger import logging

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template("home.html")
    else:
        data = CustomData(
            gender = request.form.get('gender'),
            race_ethnicity = request.form.get('ethnicity'),
            parental_level_of_education = request.form.get('parental_level_of_education'),
            lunch = request.form.get('lunch'),
            test_preparation_course = request.form.get('test_preparation_course'),
            reading_score = float(request.form.get('reading_score')),
            writing_score = float(request.form.get('writing_score'))
        )
        pred_df = data.get_data_to_data_frame()
        print(pred_df)

        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df) 
        logging.info("The entered data is: ")
        logging.info(f"Predicted results: {results}") 
        return render_template('home.html', results=results[0])
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
