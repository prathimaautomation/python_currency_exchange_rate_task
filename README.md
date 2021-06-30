# Task 
### create a new repo for this task
- A new repo has been created as `python_currency_exchange_rate_task` on GitHub
### new package in pycharm
- A new package created as `python_currency_exchange_rate_task` in Pycharm
### create a python package with setup.py
```python
from setuptools import setup

# Let's add some information about your package
setup(name = "app")
version = "1.0"
description = "Python currency exchange rate checker app"
author = "Prathima at Sparta Global"
url = "https://spartaglobal.com"
```
### put the json file in the pycharm package dir structure
```python
exchange_rates.js file has been added to app directory
```
### create a python file called exchange_rate_paser.py
```python
import json

# create a class
class Exchange_rate_parser:

    # create a funtion
    def currency_converter(currency_input):
        f = open('exchange_rates.json')
        data = json.load(f)
        # iterating through the json list
        for i in data['rates']:
            if i == currency_input:
                #print the country currency code with matching exchange rate
                print(f"{currency_input} exchange rate is {data['rates'][i]}")
                break

### HINT- import json and utilise available methods in json module
### expected outcome: GBP exchange rate is 0.89275
```
```python
from app.exchange_rate_parser import Exchange_rate_parser

currency_input = input("Please enter the currency to find exchange rate: ").upper()

Exchange_rate_parser.currency_converter(currency_input)
```

