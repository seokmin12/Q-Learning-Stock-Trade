import FinanceDataReader as fdr
from datetime import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd

now = datetime.now()

symbols = ['005930', '035720', '035420', 'rev', 'aapl', 'nvda']
company = ['samsung', 'kakao', 'naver', 'rev', 'aapl', 'nvda']

start = now - relativedelta(months=36)
start = start.strftime('%Y-%m-%d')
end = now.strftime('%Y-%m-%d')


def get_data(symbol, start, end):
    df = fdr.DataReader(symbol, start, end)
    df = df.reset_index()

    df['timestamp'] = df['Date']
    df['open'] = df['Open']
    df['high'] = df['High']
    df['low'] = df['Low']
    df['close'] = df['Close']
    df['volume'] = df['Volume']

    data = df[['timestamp', 'open', 'high', 'low', 'close', 'volume']]
    return data


for symbol in symbols:
    data = get_data(symbol, start, end)
    data.to_csv(f'data/daily_{company[symbols.index(symbol)]}.csv', index=False)
