# command line arguments = number of bitcoin they want to buy
# can't be converted to a float - exit

import requests
import sys


def main():
    print(f"${get_value():,.4f}")

# number of bitcoins
def get_bitcoins():
    while True:
        try:
            number = sys.argv[1]
            number = float(number)
            return number
        except:
            sys.exit("Must be a number")


def get_value():
    respone = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    respone = respone.json()
    rate_float = respone["bpi"]["USD"]["rate_float"]
    result = float(rate_float) * get_bitcoins()
    return result


if __name__ == '__main__':
    main()