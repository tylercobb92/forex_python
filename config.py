from flask import request

allowed_currencies=['EUR','IDR','BGN','ILS','GBP','DKK','CAD','JPY','HUF','RON','MYR','SEK','SGD','HKD','AUD','CHF','KRW','CNY','TRY','HRK','NZD','THB','USD','NOK','RUB','INR','MXN','CZK','BRL','PLN','PHP','ZAR']

currency_from=request.args['currencyFrom'].upper()
currency_to=request.args['currencyTo'].upper()
start_amount=float(request.args['amount'])