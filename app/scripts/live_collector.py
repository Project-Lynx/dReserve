import datetime as dt
import sqlite3
import time

import requests as req
from bs4 import BeautifulSoup as bs


def collection():
    start_time = time.time()

    """
        These symbols can be edited to any futures symbol
        Format:
                xx=F
    """
    symbols = [
        'ES=F', 'ZN=F', 'GE=F', 'DX=F', 'CL=F', 'NG=F',
    ]

    while True:
        time.sleep(900.0 - ((time.time() - start_time) % 900.0))
        for x in symbols:
            connec = sqlite3.connect('app/data/market_data.db')
            cursor = connec.cursor()
            cursor.execute(f"""CREATE TABLE IF NOT EXISTS {x.replace('=F','')}
                               (symbol text, timestamp text, name text, price float NOT NULL,
                               pchange text, url text)""")

            url = f"https://finance.yahoo.com/quote/{x}?p={x}"
            response = req.request("GET", url)
            parsed = bs(response.text, "lxml")

            names = parsed.find_all('h1')
            price = parsed.find('span', {'data-reactid': '32'}).string
            price = float(price.replace(",", ""))
            change = parsed.find('span', {'data-reactid': '33'}).string
            d1 = change.find('(')+1
            d2 = change.find(')')

            for name in names:
                delim = name.string.find('(')-1
                if "Futures," in name.string:
                    name = name.string.replace('Futures,', '')
                    delim = name.find('(')-1
                    name_ = name[:delim]
                else:
                    name_ = name.string[:delim]

            temp_list = []
            timestamp = dt.datetime.now().strftime('%H:%M')
            last = round(price, 2)
            pchange = change[d1:d2]
            url_ = url

            temp_list.append((x.replace("=F", ""), timestamp, name_,
                             float(last), pchange, url_))
            cursor.executemany(f"INSERT INTO {x.replace('=F', '')} VALUES (?,?,?,?,?,?)", temp_list)
            connec.commit()
            connec.close()


collection()
