from app.models.futures import Meta as futures_model
from app.util import symbols_n_ids


# Get single quote of symbol
def get_quote(symbol: str) -> dict:
    PID = symbols_n_ids.get_CME_pids(symbol)
    query = "SELECT code, name, last, pChange, url FROM testing WHERE id=%s"
    data = futures_model().fetch(query, (PID, ))

    output: dict = {}
    for idx in enumerate(data):
        key = idx[1][0]
        output[key] = [idx[1][1], idx[1][2], idx[1][3], idx[1][4]]
    return output


# Get quotes of symbols
def get_quotes(symbols: str) -> dict:
    symbol_list = list(symbols.split(","))
    PIDs = tuple(i for i in symbols_n_ids.get_CME_pids(symbol_list))
    query_start = "SELECT code, name, last, pChange, url FROM testing WHERE id IN ("
    query = query_start + ("%s," * len(PIDs))[:-1] + ")"
    data = futures_model().fetch(query, PIDs)

    output: dict = {}
    for idx in enumerate(data):
        key = idx[1][0]
        output[key] = [idx[1][1], idx[1][2], idx[1][3], idx[1][4]]
    return output


# Handle logic behind get-quotes endpoint
def handler(symbols: str) -> dict:
    if "," in symbols:
        return get_quotes(symbols)
    else:
        return get_quote(symbols)
