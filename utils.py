import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


def get_data(col='close'):
    """ Returns a 3 x n_step array """
    # msft = pd.read_csv('data/daily_MSFT.csv', usecols=[col])
    # ibm = pd.read_csv('data/daily_IBM.csv', usecols=[col])
    # qcom = pd.read_csv('data/daily_QCOM.csv', usecols=[col])
    # # recent price are at top; reverse it
    # return np.array([msft[col].values[:500],
    #                  ibm[col].values[:500],
    #                  qcom[col].values[:500]])

    rev = pd.read_csv('data/daily_rev.csv', usecols=[col])
    aapl = pd.read_csv('data/daily_aapl.csv', usecols=[col])
    nvda = pd.read_csv('data/daily_nvda.csv', usecols=[col])
    return np.array([rev[col].values[:200],
                     aapl[col].values[:200],
                     nvda[col].values[:200]])

    # msft = pd.read_csv('data/daily_MSFT.csv', usecols=[col])
    # ibm = pd.read_csv('data/daily_IBM.csv', usecols=[col])
    # qcom = pd.read_csv('data/daily_QCOM.csv', usecols=[col])
    # # recent price are at top; reverse it
    # return np.array([msft[col].values[::-1],
    #                  ibm[col].values[::-1],
    #                  qcom[col].values[::-1]])

    # samsung = pd.read_csv('data/daily_samsung.csv', usecols=[col])
    # kakao = pd.read_csv('data/daily_kakao.csv', usecols=[col])
    # naver = pd.read_csv('data/daily_naver.csv', usecols=[col])
    # # recent price are at top; reverse it
    # return np.array([samsung[col].values[::500],
    #                  kakao[col].values[::500],
    #                  naver[col].values[::500]])


def get_scaler(env):
    """ Takes a env and returns a scaler for its observation space """
    low = [0] * (env.n_stock * 2 + 1)

    high = []
    max_price = env.stock_price_history.max(axis=1)
    min_price = env.stock_price_history.min(axis=1)
    max_cash = env.init_invest * 3  # 3 is a magic number...
    max_stock_owned = max_cash // min_price
    for i in max_stock_owned:
        high.append(i)
    for i in max_price:
        high.append(i)
    high.append(max_cash)

    scaler = StandardScaler()
    scaler.fit([low, high])
    return scaler


def maybe_make_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
