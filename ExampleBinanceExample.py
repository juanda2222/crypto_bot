from binance.client import Client
from os import environ
from FormatHelpersCandles import candles_to_close_times, candles_to_closes, candles_to_highs, candles_to_lows, candles_to_number_of_trades, candles_to_volume
from Constants import DEFAULT_MARKET_NAME, DEFAULT_SAVE_TO_FILES, DEFAULT_INTERVAL
from FileHelpers import write_to_json_file
from VisualizationHelpers import plot_candle_data

MARKET_TO_FETCH = DEFAULT_MARKET_NAME
SAVE_ON_FILES = False
NUMBER_OF_POINTS = 500 # MAX 1000

# example script
def main():
    client = Client(environ.get('BINANCE_API_KEY'), environ.get('BINANCE_API_SECRET'), tld='us')
    res = client.get_exchange_info()
    
    print('>>>> Getting exchange info...')
    # self explanatory
    write_to_json_file('exchange_info', res, save_on_files=SAVE_ON_FILES)

    print('>>> Getting Bitcoin info...')
    # self explanatory
    info = client.get_symbol_info(MARKET_TO_FETCH)
    write_to_json_file('{}_info'.format(MARKET_TO_FETCH), info, save_on_files=SAVE_ON_FILES)

    print('>>> Getting Bitcoin order book...')
    # {
    #     "lastUpdateId": 1027024,
    #     "bids": [
    #         [
    #         "4.00000000",     // PRICE
    #         "431.00000000"    // QTY
    #         ]
    #     ],
    #     "asks": [
    #         [
    #         "4.00000200",
    #         "12.00000000"
    #         ]
    #     ]
    # }
    order_book = client.get_order_book(symbol=MARKET_TO_FETCH)
    write_to_json_file('{}_order_book'.format(MARKET_TO_FETCH), order_book, save_on_files=SAVE_ON_FILES)
    
    print('>>> Getting Aggregated trades...')
    # [
    #     {
    #         "a": 26129,         // Aggregate tradeId
    #         "p": "0.01633102",  // Price
    #         "q": "4.70443515",  // Quantity
    #         "f": 27781,         // First tradeId
    #         "l": 27781,         // Last tradeId
    #         "T": 1498793709153, // Timestamp
    #         "m": true,          // Was the buyer the maker?
    #         "M": true           // Was the trade the best price match?
    #     }
    # ]
    agg_trades = client.aggregate_trade_iter(symbol=MARKET_TO_FETCH, start_str='30 minutes ago UTC')
    agg_trades = {'trades': list(agg_trades)}
    write_to_json_file('{}_aggregated_trades'.format(MARKET_TO_FETCH), agg_trades, save_on_files=SAVE_ON_FILES)
    
    print('>>> Getting price candles...')
    # [
    #     [
    #         1499040000000,      # Open time
    #         "0.01634790",       # Open
    #         "0.80000000",       # High
    #         "0.01575800",       # Low
    #         "0.01577100",       # Close
    #         "148976.11427815",  # Volume
    #         1499644799999,      # Close time
    #         "2434.19055334",    # Quote asset volume
    #         308,                # Number of trades
    #         "1756.87402397",    # Taker buy base asset volume
    #         "28.46694368",      # Taker buy quote asset volume
    #         "17928899.62484339" # Can be ignored
    #     ]
    # ]
    candles = client.get_klines(symbol=MARKET_TO_FETCH, interval=DEFAULT_INTERVAL, limit=NUMBER_OF_POINTS)
    filtered_candles = candles
    write_to_json_file('{}_candles'.format(MARKET_TO_FETCH), filtered_candles, save_on_files=SAVE_ON_FILES)
    closes = candles_to_closes(filtered_candles)
    close_times = candles_to_close_times(filtered_candles)
    highs = candles_to_highs(filtered_candles)
    lows = candles_to_lows(filtered_candles)
    volume = candles_to_volume(filtered_candles)
    number_of_trades = candles_to_number_of_trades(filtered_candles)
    plot_candle_data(close_times, highs, lows, closes, volume, number_of_trades, market_name=MARKET_TO_FETCH)


    print('>>> Getting historic price candles...')
    # [
    #     [
    #         1499040000000,      # Open time
    #         "0.01634790",       # Open
    #         "0.80000000",       # High
    #         "0.01575800",       # Low
    #         "0.01577100",       # Close
    #         "148976.11427815",  # Volume
    #         1499644799999,      # Close time
    #         "2434.19055334",    # Quote asset volume
    #         308,                # Number of trades
    #         "1756.87402397",    # Taker buy base asset volume
    #         "28.46694368",      # Taker buy quote asset volume
    #         "17928899.62484339" # Can be ignored
    #     ]
    # ]
    historic_candles = client.get_historical_klines(MARKET_TO_FETCH, Client.KLINE_INTERVAL_15MINUTE, start_str="1 Dec, 2020", end_str="1 Jan, 2021", limit=NUMBER_OF_POINTS)
    write_to_json_file('{}_historic_candles'.format(MARKET_TO_FETCH), historic_candles, save_on_files=SAVE_ON_FILES)

if __name__ == "__main__":
    main()
