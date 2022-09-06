from flask import request
from config import currency_from, currency_to, start_amount, allowed_currencies

def check_form():

    rule_1 = currency_from in allowed_currencies,
    rule_2 = currency_to in allowed_currencies,
    rule_3 = start_amount >= 0.01

    if not rule_1:
        print(f'{currency_from} is not valid')
    if not rule_2:
        print(f'{currency_to} is not valid')
    if not rule_3:
        print(f'{start_amount} is not valid')