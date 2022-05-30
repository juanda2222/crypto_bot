# for more information of the request parameters:
# https://coinmarketcap.com/api/documentation/v1/#operation/getV1GlobalmetricsQuotesHistorical

from os import environ
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from Constants import DEFAULT_MARKET_NAME

from FileHelpers import write_to_json_file

MARKET_TO_FETCH = DEFAULT_MARKET_NAME
SAVE_ON_FILES = True
NUMBER_OF_POINTS = 500 # MAX 1000


# example script
def main():
  print('>>> Getting latest global market stats...')
  url = 'https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest'
  parameters = {
    'convert':'USD'
  }
  headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': environ.get('COINMARKETCAP_API_KEY'),
  }

  session = Session()
  session.headers.update(headers)

  try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    write_to_json_file('GLOBAL_current_global_data', data, save_on_files=SAVE_ON_FILES)
  except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)


  # this pro endpoint does not work unless you pay 300 USD (that is why we are using the web-api subdomain)
  print('>>> Getting historical global market stats...')
  url = 'https://web-api.coinmarketcap.com/v1.1/global-metrics/quotes/historical'
  parameters = {
    'count': NUMBER_OF_POINTS,
    'convert':'USD',
    'interval': '15m'
  }
  headers = {
    'Accepts': 'application/json',
  }

  session = Session()
  session.headers.update(headers)

  try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    write_to_json_file('GLOBAL_historic_global_data', data, save_on_files=SAVE_ON_FILES)
  except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

main()