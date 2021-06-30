from app.exchange_rate_parser import Exchange_rate_parser

currency_input = input("Please enter the currency to find exchange rate: ").upper()

Exchange_rate_parser.currency_converter(currency_input)