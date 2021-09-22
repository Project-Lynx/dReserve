from app.models.futures import Meta as futures_model
from app.util import symbols_n_ids


# Get history for single symbol
def get_hist(symbol: str) -> dict:
    PID = symbols_n_ids.get_CME_pids(symbol)
    data = futures_model().fetch(f'''
        SELECT code, updated, last FROM testing WHERE id={PID}
    ''')

    output: dict = {}
    for key, subkey, value in data:
        if output == {}:
            output[key] = {}
        else:
            output[key][subkey[:8]] = value

    return output


# Get history of multiple symbols
def get_hists(symbol: str) -> dict:
    _symbols = list(symbol.split(","))
    PIDs = str(tuple(i for i in symbols_n_ids.get_CME_pids(_symbols)))
    data = futures_model().fetch(f'''
        SELECT code, updated, last FROM testing WHERE id IN {PIDs}
    ''')

    output: dict = {}
    for key, subkey, value in data:
        if key not in output:
            output[key] = {}
        else:
            output[key][subkey[:8]] = value

    return output


# Handling logic behind get-hist endpoint
def hist_handler(symbols: str) -> dict:
    if "," in symbols:
        return get_hists(symbols)
    else:
        return get_hist(symbols)


# Get single quote of symbol
def get_quote(symbol: str) -> dict:
    PID = symbols_n_ids.get_CME_pids(symbol)
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


# Get quotes of symbols
def get_quotes(symbols: str) -> dict:
    symbol_list = list(symbols.split(","))
    PIDs = str(tuple(i for i in symbols_n_ids.get_CME_pids(symbol_list)))
    data = futures_model().fetch(f'''
        SELECT code, name, last, pChange, url FROM testing WHERE id IN {PIDs}
    ''')

    output: dict = {}
    for idx in enumerate(data):
        key = idx[1][0]
        output[key] = [
            idx[1][1], idx[1][2], idx[1][3], idx[1][4],
        ]

    return output


# Handle logic behind get-quotes endpoint
def handle_quotes(symbols: str) -> dict:
    if "," in symbols:
        return get_quotes(symbols)
    else:
        return get_quote(symbols)
