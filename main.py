from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('./index.html')


@app.route('/sum/x=<a>&y=<b>')
def get_sum(a, b):
    total = eval(a)+eval(b)
    return str(total)


@app.route('/today')
def date():
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return date


@app.route('/bmi/name=<a>&height=<b>&weight=<c>')
def get_bmi(a, b, c):
    bmi = round(eval(c)/(eval(b)/100)**2, 2)
    return f'{a} bmi={str(bmi)}'


if __name__ == '__main__':
    app.run(debug=True)
