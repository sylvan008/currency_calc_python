import requests

USD = 'usd'
EUR = 'eur'
RATE = 'rate'
CODE = 'code'


def convert_currency(value, rate):
    return round(value * rate, 2)


def printer(message):
    print(message)


def get_rates(currency):
    url = f"http://www.floatrates.com/daily/{currency}.json"
    r = requests.get(url)
    return r.json()


def get_user_currency():
    return input().lower()


def get_user_money():
    return int(input())


def init_cash(default_list, currency_json):
    cash = dict()
    for currency_key in currency_json:
        currency = currency_json[currency_key]
        code = currency[CODE].lower()
        if code in default_list:
            cash[code] = currency
    return cash


def main():
    default_currency = [USD, EUR]
    user_currency = get_user_currency()
    cash = init_cash(default_currency, get_rates(user_currency))

    while True:
        ceil_currency = get_user_currency()
        if not ceil_currency:
            break
        user_money = get_user_money()
        printer('Checking the cache...')
        if ceil_currency not in cash:
            printer('Sorry, but it is not in the cache!')
            json_rates = get_rates(user_currency)
            cash[ceil_currency] = json_rates[ceil_currency]
        else:
            printer('Oh! It is in the cache!')
        value = convert_currency(user_money, cash[ceil_currency][RATE])
        printer("You received {} {}.".format(value, ceil_currency.upper()))


main()
