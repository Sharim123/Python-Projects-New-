import time

import requests
from datetime import datetime

ticker = input(("Enter the ticker symbol: "))
from_date = input("Enter start date in yyyy/mm/dd format: ")
to_date = input("Enter end date in y  yyy/mm/dd format: ")

from_datetime = datetime.strptime(from_date, "%Y/%m/%d")
to_datetime = datetime.strptime(to_date, "%Y/%m/%d")

from_epoch = int(time.mktime(from_datetime.timetuple()))
to_epoch = int(time.mktime(to_datetime.timetuple()))

url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={from_epoch}&period2={to_epoch}&interval=1d&events=history&includeAdjustedClose=true"

headers = {'user-agent': 'my-app/0.0.1'}
content = requests.get(url, headers=headers).content

print(content)


with open("data.csv", 'wb') as file:
    file.write(content)




