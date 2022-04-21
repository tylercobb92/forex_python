from flask import Flask, render_template, request, json
from forex_python.converter import CurrencyRates, CurrencyCodes

app=Flask(__name__)
app.config['SECRET KEY']="asdfQWERDsfawet"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert')
def convert_currency():
    c=CurrencyRates()
    currency_from=request.args['currencyFrom'].upper()
    currency_to=request.args['currencyTo'].upper()
    start_amount=float(request.args['amount'])
    finish_amount = c.convert(currency_from, currency_to, start_amount)
    curr_code=CurrencyCodes()
    code=curr_code.get_symbol(currency_to)
    return render_template('conversion.html', code=code, amount=finish_amount)
