from dateutil import parser


# Candle format helpers
def global_quotes_to_total_market_cap(global_data_quotes):
    return list(map(lambda quote: quote['quote']['USD']['total_market_cap'], global_data_quotes))

# Candle format helpers
def global_quotes_to_altcoin_market_cap(global_data_quotes):
    return list(map(lambda quote: quote['quote']['USD']['altcoin_market_cap'], global_data_quotes))

def global_quotes_to_time_points(global_data_quotes):
    return list(map(lambda quote: parser.parse(quote['timestamp']), global_data_quotes))

def global_quotes_to_total_volume(global_data_quotes):
    return list(map(lambda quote: quote['quote']['USD']['total_volume_24h'], global_data_quotes))

def global_quotes_to_altcoin_volume(global_data_quotes):
    return list(map(lambda quote: quote['quote']['USD']['altcoin_volume_24h'], global_data_quotes))

def global_quotes_to_btc_dominance(global_data_quotes):
    return list(map(lambda quote: quote['btc_dominance'], global_data_quotes))

