import sqlite3


def get_hist(symbol):
    hist_output = {}

    connec = sqlite3.connect('app/data/market_data.db')
    cursor = connec.cursor()
    cursor.execute(f"SELECT timestamp, price FROM {symbol.replace('=F','')}")
    data = cursor.fetchall()

    for key, value in data:
        hist_output[key] = value

    return hist_output


def get_quotes(symbols):
    quote_output = {}

    connec = sqlite3.connect('app/data/market_data.db')
    cursor = connec.cursor()
    for symbol in symbols:
        cursor.execute(f"SELECT * FROM {symbol.replace('=F','')}")
        data = cursor.fetchall()

        for idx in enumerate(data):
            quote_output[symbol] = {'name': idx[1][2]}
            quote_output[symbol]["last"] = idx[1][3]
            quote_output[symbol]["pchange"] = idx[1][4]
            quote_output[symbol]["url"] = idx[1][5]

    return quote_output
