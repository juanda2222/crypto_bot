from os import environ
from binance.client import Client

from FormatHelpersCandles import candles_to_close_times, candles_to_closes, candles_to_highs, candles_to_lows, candles_to_number_of_trades, candles_to_volume
from FormatHelpersGlobalQuotes import global_quotes_to_altcoin_market_cap, global_quotes_to_altcoin_volume, global_quotes_to_btc_dominance, global_quotes_to_time_points, global_quotes_to_total_market_cap, global_quotes_to_total_volume
from Transformations import calculate_boll_from_close_history, calculate_rsi_from_close_history, calculate_sma_from_close_history
from VisualizationHelpers import plot_candle_data, plot_candle_processed_data, plot_global_data, show_plots
from modules.GlobalData import getHistoricGlobalData


SYMBOL_TO_SCRAP = 'BTCUSDT'
INTERVAL_TO_SCRAP = Client.KLINE_INTERVAL_15MINUTE
NUMBER_OF_DATA_POINTS = 500

# example script
def main():
    
    # fetch the candles
    print('>>> Getting latest price candles for {}'.format(SYMBOL_TO_SCRAP))
    client = Client(environ.get('BINANCE_API_KEY'), environ.get('BINANCE_API_SECRET'), tld='us')
    candles = client.get_klines(symbol=SYMBOL_TO_SCRAP, interval=INTERVAL_TO_SCRAP, limit=NUMBER_OF_DATA_POINTS)

    # format the candle data
    closes = candles_to_closes(candles)
    close_times = candles_to_close_times(candles)
    highs = candles_to_highs(candles)
    lows = candles_to_lows(candles)
    volume = candles_to_volume(candles)
    number_of_trades = candles_to_number_of_trades(candles)

    # visualize candle data
    plot_candle_data(close_times, highs, lows, closes, volume, number_of_trades, market_name=SYMBOL_TO_SCRAP)

    # calculate additional indicators
    rsi_6 = calculate_rsi_from_close_history(closes, 6)
    rsi_12 = calculate_rsi_from_close_history(closes, 12)
    rsi_24 = calculate_rsi_from_close_history(closes, 24)
    sma_7 = calculate_sma_from_close_history(closes, 7)
    sma_25 = calculate_sma_from_close_history(closes, 25)
    sma_100 = calculate_sma_from_close_history(closes, 100)
    boll_upper_24, boll_lower_24 = calculate_boll_from_close_history(closes, 24)

    # visualize additional indicators
    plot_candle_processed_data(close_times, rsi_6, rsi_12, rsi_24, sma_7, sma_25, sma_100, boll_upper_24, boll_lower_24, market_name=SYMBOL_TO_SCRAP)

    # fetch the global data
    global_data_quotes = getHistoricGlobalData(interval=INTERVAL_TO_SCRAP, limit=NUMBER_OF_DATA_POINTS)

    # format the global data
    global_times = global_quotes_to_time_points(global_data_quotes)
    total_market_cap = global_quotes_to_total_market_cap(global_data_quotes)
    volume_24h = global_quotes_to_total_volume(global_data_quotes)
    bitcoin_dominance = global_quotes_to_btc_dominance(global_data_quotes)

    # visualize global data
    plot_global_data(global_times, total_market_cap, volume_24h, bitcoin_dominance)

    show_plots()

if __name__ == "__main__":
    main()

