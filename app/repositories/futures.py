from app.models.futures import Meta as futures_model
from app.util import symbols_n_ids


def get_hist(symbol):
    PID = symbols_n_ids.get_CME_pids(symbol)
    data = futures_model().fetch(f'''
        SELECT updated, last FROM testing WHERE id={PID}
    ''')

    output = {}
    for key, value in data:
        output[key[:8]] = value

    return output


def get_quotes(symbols):
    if len(symbols) > 1:
        PID = str(tuple(i for i in symbols_n_ids.get_CME_pids(symbols)))
        data = futures_model().fetch(f'''
            SELECT code, name, last, pChange, url FROM testing WHERE id IN {PID}
        ''')

        output = {}
        for idx in enumerate(data):
            key = idx[1][0]
            output[key] = [
                idx[1][1], idx[1][2], idx[1][3], idx[1][4],
            ]

        return output

    else:
        PID = symbols_n_ids.get_CME_pids(symbols[0])
        data = futures_model().fetch(f'''
            SELECT code, name, last, pChange, url FROM testing WHERE id={PID}
        ''')

        output = {}
        for idx in enumerate(data):
            key = idx[1][0]
            output[key] = [
                idx[1][1], idx[1][2], idx[1][3], idx[1][4],
            ]

        return output
