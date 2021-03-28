import requests
from time import sleep
from requests.exceptions import HTTPError

waluty = ('BTC', 'GAME', 'ETH')


def contest(url):
    try:
        response = requests.get(url)

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')


def asknbid(w):
    url = f'https://bitbay.net/API/Public/{w}/ticker.json'
    if not contest(url):
        return contest(url)
    response = requests.get(url)
    a = response.json()['ask']
    b = response.json()['bid']
    return a, b


contest('http;s://bitbay.net/API/Public/BTC/ticker.json')