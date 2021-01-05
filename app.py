from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    return 'Good click but no'


if __name__ == '__main__':
    app.run(debug=True)
