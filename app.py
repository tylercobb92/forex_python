from ast import Num
from locale import currency
from decimal import Decimal
from flask import Flask, render_template, request, json
from forex_python.converter import CurrencyRates

app=Flask(__name__)
app.config['SECRET KEY']="asdfQWERDsfawet"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert')
def convert_currency():
    c=CurrencyRates()
    currency_from=request.args['currencyFrom']
    currency_to=request.args['currencyTo']
    start_amount=float(request.args['amount'])
    finish_amount = c.convert(currency_from, currency_to, start_amount)
    return render_template('conversion.html', amount=finish_amount)
