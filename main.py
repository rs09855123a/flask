from flask import Flask, render_template, request
from datetime import datetime
from numpy.core.fromnumeric import sort
import pandas as pd

from pm25 import get_pm25

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    name = 'Jerry'
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # context = {
    #     'name': name,
    #     'date': date
    # }   第3種
    return render_template('./index.html', **locals())
    # return render_template('./index.html', name=name, date=date)  第2種
    # return render_template('./index.html', context=context)  第3種


@app.route('/stocks')
def stocks():
    stocks = [
        {'分類': '日經指數', '指數': '22,920.30'},
        {'分類': '韓國綜合', '指數': '2,304.59'},
        {'分類': '香港恆生', '指數': '25,083.71'},
        {'分類': '上海綜合', '指數': '3,380.68'}
    ]
    return render_template('./stock.html', stocks=stocks)


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


@app.route('/pm25', methods=['GET', 'POST'])
def pm25():
    if request.method == 'GET':
        columns, values, update_time = get_pm25()

    if request.method == 'POST':
        columns, values, update_time = get_pm25(sort)
    return render_template('./pm25.html', columns=columns, values=values, update_time=update_time)


if __name__ == '__main__':
    app.run(debug=True)
