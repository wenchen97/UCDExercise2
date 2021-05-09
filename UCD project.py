import requests

data=requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=000002.SHZ&outputsize=full&apikey=4ANOQOZOSF8G8OZP")

print(data.status_code)

import numpy as np
import pandas as pd

df=pd.read_csv("D:\daily_adjusted_000002.SHZ.csv")

print(df.head())
