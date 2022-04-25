from ast import Num
from flask import Flask, redirect, render_template, request
from forex_python.converter import CurrencyRates, CurrencyCodes

app=Flask(__name__)
app.config['SECRET KEY']="asdfQWERDsfawet"

allowed_currencies=['EUR','IDR','BGN','ILS','GBP','DKK','CAD','JPY','HUF','RON','MYR','SEK','SGD','HKD','AUD','CHF','KRW','CNY','TRY','HRK','NZD','THB','USD','NOK','RUB','INR','MXN','CZK','BRL','PLN','PHP','ZAR']

c=CurrencyRates()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/conversion', methods=['POST'])
def convert_currency():
    currency_from=request.form['currencyFrom'].upper()
    currency_to=request.form['currencyTo'].upper()
    start_amount=float(request.form['amount'])

    finish_amount = c.convert(currency_from, currency_to, start_amount)
    curr_code=CurrencyCodes()

    code=curr_code.get_symbol(currency_to)
    
    print(currency_from, currency_to, start_amount)
    return render_template('conversion.html', code=code, amount=finish_amount)
