
import pandas as pd

from Constants import DEFAULT_RSI_RANGE, DEFAULT_SMA_RANGE


def calculate_rsi_from_close_history(price_history, window_length = DEFAULT_RSI_RANGE):
    df = pd.DataFrame(list(zip(price_history)), columns =['Close value'])

    # calculate the difference for each pair of points
    df['diff'] = df.diff(1)

    # Calculate Avg. Gains/Losses
    df['gain'] = df['diff'].clip(lower=0)
    df['loss'] = df['diff'].clip(upper=0).abs()

    # Get initial Averages
    df['avg_gain'] = df['gain'].rolling(window=window_length, min_periods=window_length).mean()[:window_length+1]
    df['avg_loss'] = df['loss'].rolling(window=window_length, min_periods=window_length).mean()[:window_length+1]

    # Average Gains
    for i, row in enumerate(df['avg_gain'].iloc[window_length+1:]):
        df['avg_gain'].iloc[i + window_length + 1] =\
            (df['avg_gain'].iloc[i + window_length] *
            (window_length - 1) +
            df['gain'].iloc[i + window_length + 1])\
            / window_length
    # Average Losses
    for i, row in enumerate(df['avg_loss'].iloc[window_length+1:]):
        df['avg_loss'].iloc[i + window_length + 1] =\
            (df['avg_loss'].iloc[i + window_length] *
            (window_length - 1) +
            df['loss'].iloc[i + window_length + 1])\
            / window_length

    # Calculate RS Values
    df['rs'] = df['avg_gain'] / df['avg_loss']

    # calculate rsi values
    df['rsi'] = 100 - (100 / (1.0 + df['rs']))

    return list(df['rsi'])

def calculate_sma_from_close_history(price_history, window_length = DEFAULT_SMA_RANGE):
    df = pd.DataFrame(list(zip(price_history)), columns =['Close value'])
    sma = df.rolling(window = window_length).mean()
    return sma

def calculate_boll_from_close_history(price_history, window_length = DEFAULT_RSI_RANGE):
    df = pd.DataFrame(list(zip(price_history)), columns =['Close value'])
    std = df.rolling(window = window_length).std()
    sma = df.rolling(window = window_length).mean()
    upper_bb = sma + std * 2
    lower_bb = sma - std * 2
    return upper_bb, lower_bb