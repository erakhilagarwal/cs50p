import sys
import requests
import json

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    try:
        count = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        bitcoin = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        bitcoin = bitcoin.json()
        price = bitcoin['bpi']['USD']['rate_float']
        price = float(price)
        amount = price * count
        print(f"${amount:,.4f}")
        #print(json.dumps(bitcoin.json()))
    except (requests.RequestException, ValueError):
        pass


if __name__ == "__main__":
    main()