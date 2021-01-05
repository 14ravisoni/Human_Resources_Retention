from flask import Flask, render_template, request
import pandas as pd
from models import process_dataFrame
import pickle
from sklearn.ensemble import RandomForestClassifier

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

    dataframe = pd.DataFrame(dict_data, index=[0])
    main_data = process_dataFrame.process_dataframe(dataframe)
    print(type(main_data))

    loaded_model = pickle.load(open('RandomForestClassifier.pkl', 'rb'))
    result = loaded_model.predict(main_data)

    return render_template('result.html', raw_data=dataframe.values.tolist(), processed_data=main_data.tolist(), result=result)


if __name__ == '__main__':
    app.run(debug=True)
