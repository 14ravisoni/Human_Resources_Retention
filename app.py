import pickle

from flask import Flask, render_template, request
import numpy as np


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    dict_data = {
        'employee_id': request.form['employee_id'],
        'number_project': request.form['number_project'],
        'average_montly_hours': request.form['average_montly_hours'],
        'time_spend_company': request.form['time_spend_company'],
        'Work_accident': request.form['Work_accident'],
        'promotion_last_5years': request.form['promotion_last_5years'],
        'department': request.form['department'],
        'salary': request.form['salary'],
        'satisfaction_level': request.form['satisfaction_level'],
        'last_evaluation': request.form['last_evaluation']
    }
    x = [
        dict_data['number_project'],
        dict_data['average_montly_hours'],
        dict_data['time_spend_company'],
        dict_data['Work_accident'],
        dict_data['promotion_last_5years'],
        dict_data['satisfaction_level'],
        dict_data['last_evaluation']
    ]
    for i in dict_data['department']:
        x.append(i)
    for i in dict_data['salary']:
        x.append(i)

    loaded_model = pickle.load(open('RandomForestClassifier.pkl', 'rb'))
    result1 = loaded_model.predict(np.array(x))

    return render_template('result.html', raw_data=x, result=result1)


if __name__ == '__main__':
    app.run(debug=True)
