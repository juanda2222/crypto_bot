from datetime import datetime


# Candle format helpers
def candles_to_highs(candle_array):
    return list(map(lambda candle: float(candle[2]), candle_array))

def candles_to_lows(candle_array):
    return list(map(lambda candle: float(candle[3]), candle_array))

def candles_to_closes(candle_array):
    return list(map(lambda candle: float(candle[4]), candle_array))

def candles_to_volume(candle_array):
    return list(map(lambda candle: float(candle[5]), candle_array))

def candles_to_close_times(candle_array):
    return list(map(lambda candle: datetime.fromtimestamp( int(int(candle[6]) / 1000)), candle_array))

def candles_to_number_of_trades(candle_array):
    return list(map(lambda candle: candle[8], candle_array))
