from ast import Num
from flask import Flask, render_template, request
from forex_python.converter import CurrencyRates, CurrencyCodes
from config import allowed_currencies

app=Flask(__name__)
app.config['SECRET KEY']="asdfQWERDsfawet"


c=CurrencyRates()

@app.route('/')
def home():
    """Render currency exchance form"""

    return render_template('index.html')

@app.route('/conversion')
def convert_currency():
    """Check currency exchange form fields. Return error code if filled incorrectly, or show completed conversion if correct. A currency converted to itself should always be 1 to 1. 

    >>> c.convert('usd','usd',1)
    1.0

    >>> c.convert('cad','cad',1000)
    1000.0
    """

    currency_from=request.args['currencyFrom'].upper()
    currency_to=request.args['currencyTo'].upper()
    start_amount=float(request.args['amount'])
    
    rule_1=currency_from in allowed_currencies
    rule_2=currency_to in allowed_currencies
    rule_3=start_amount>0

    err_0='All fields required'
    err_1=f'Not a valid code: {currency_from}'
    err_2=f'Not a valid code: {currency_to}'
    err_3=f'Amount must be greater than 0'

    if not currency_from or not currency_to or not start_amount:
        return render_template('index.html', err_msg=err_0)
    elif not rule_1:
        return render_template('index.html', err_msg=err_1)
    elif not rule_2:
        return render_template('index.html', err_msg=err_2)
    elif not rule_3:
        return render_template('index.html', err_msg=err_3)
    else:
        finish_amount = c.convert(currency_from, currency_to, start_amount)
        curr_code=CurrencyCodes()

        code=curr_code.get_symbol(currency_to)
    
        return render_template('conversion.html', code=code, amount=finish_amount)
