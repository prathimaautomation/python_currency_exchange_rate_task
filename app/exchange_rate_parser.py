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