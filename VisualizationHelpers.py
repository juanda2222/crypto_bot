import matplotlib.pyplot as plt

from Constants import DEFAULT_MARKET_NAME


# helper plot functions
def plot_array(arr, market=DEFAULT_MARKET_NAME):

    # setup the graph
    fig, ax = plt.subplots()
    ax.plot(arr[-100:])
    ax.set(xlabel='time (s)', ylabel='value (USD)', title='{} time chart'.format(market))

def plot_candle_data(close_times, highs, lows, closes, volumes, number_of_trades, market_name=DEFAULT_MARKET_NAME):

    # setup the graph
    fig, ax = plt.subplots(3)

    # setup the value chart
    ax[0].plot(close_times, closes, label='Close Value')
    ax[0].plot(close_times, highs, label='High Value', color='green', linestyle=':')
    ax[0].plot(close_times, lows, label='Lower Value', color='red', linestyle=':')
    ax[0].fill_between(close_times, highs, lows, alpha=0.2)
    ax[0].set(xlabel='time', ylabel='value (USD)', title='{} Time Chart ({} points)'.format(market_name, len(close_times)))

    # setup number of trades chart
    ax[1].plot(close_times, number_of_trades, label='Number of trades')
    ax[1].set(xlabel='time', ylabel='No. Of Trades ', title='{} Trades Chart'.format(market_name))

    # volume 
    ax[2].plot(close_times, volumes, label='Volume')
    ax[2].set(xlabel='time', ylabel='Volume (USD) ', title='{} Volume Chart'.format(market_name))


def plot_candle_processed_data(close_times, rsi_6, rsi_12, rsi_24, sma_7, sma_25, sma_100, boll_upper, boll_lower, market_name = DEFAULT_MARKET_NAME):

    # setup the graph
    fig, ax = plt.subplots(2)

    # setup RSI chart
    ax[0].plot(close_times, rsi_6, label='RSI (6)')
    ax[0].plot(close_times, rsi_12, label='RSI (12)')
    ax[0].plot(close_times, rsi_24, label='RSI (24)')
    ax[0].set(xlabel='time', ylabel='RSI %', title='{} RSI Time Chart ({})'.format(market_name, len(close_times)))

    # Setup the SMA chart
    ax[1].plot(close_times, sma_7, label='RSI (7)')
    ax[1].plot(close_times, sma_25, label='RSI (25)')
    ax[1].plot(close_times, sma_100, label='RSI (100)')
    ax[1].plot(close_times, boll_upper, label='upper BOLL')
    ax[1].plot(close_times, boll_lower, label='lower BOLL')
    ax[1].set(xlabel='time', ylabel='SMA and BOLL (USD) ', title='{} SMA Time Chart ({})'.format(market_name, len(close_times)))


def plot_global_data(global_times, total_market_cap, volume_24h, bitcoin_dominance):
    # setup the graph
    fig, ax = plt.subplots(3)

    # setup Total market cap chart
    ax[0].plot(global_times, total_market_cap, label='Total Market Cap')
    # ax[0].plot(global_times, altcoin_market_cap, label='Altcoin Market Cap')
    ax[0].set(xlabel='time', ylabel='USD', title='Market cap')

    # total volume chart
    ax[1].plot(global_times, volume_24h, label='Total Volume 24h')
    # ax[1].plot(global_times, altcoin_volume_24h, label='Altcoin Volume 24h')
    ax[1].set(xlabel='time', ylabel='USD', title='Volume 24H')

    # bitcoin dominance
    ax[2].plot(global_times, bitcoin_dominance, label='Bitcoin/Alts')
    ax[2].set(xlabel='time', ylabel='%', title='Bitcoin dominance')

    
def show_plots():
    plt.show()