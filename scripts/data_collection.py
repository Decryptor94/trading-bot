import requests
import pandas as pd
import time

def get_binance_data(symbol, interval, start_time, end_time):
    url = f'https://api.binance.com/api/v3/klines?symbol={symbol}&interval={interval}&startTime={start_time}&endTime={end_time}'
    data = requests.get(url).json()
    df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    return df

# Example usage
if __name__ == "__main__":
    symbol = 'BTCUSDT'
    interval = '1d'
    start_time = int(time.mktime(time.strptime('2021-01-01', '%Y-%m-%d')) * 1000)
    end_time = int(time.mktime(time.strptime('2021-12-31', '%Y-%m-%d')) * 1000)
    df = get_binance_data(symbol, interval, start_time, end_time)
    df.to_csv('data/btc_usdt.csv', index=False)
