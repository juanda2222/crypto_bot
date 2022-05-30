# for more information of the request parameters:
# https://coinmarketcap.com/api/documentation/v1/#operation/getV1GlobalmetricsQuotesHistorical

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

def getHistoricGlobalData(interval='15m', limit=100):
    # this endpoint does not work unless you pay 300 USD
    print('>>> Getting historical global market stats...')
    url = 'https://web-api.coinmarketcap.com/v1.1/global-metrics/quotes/historical'
    parameters = {
        'count': limit,
        'convert':'USD',
        'interval': interval
    }
    headers = {
        'Accepts': 'application/json'
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        return json.loads(response.text)['data']['quotes']
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)