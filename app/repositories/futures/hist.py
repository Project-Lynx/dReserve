from app.models.futures import Meta as futures_model
from app.util import symbols_n_ids


# Get history for single symbol
def get_hist(symbol: str) -> dict:
    PID = str(symbols_n_ids.get_CME_pids(symbol))
    query = "SELECT code, updated, last FROM testing WHERE id=%s"
    data = futures_model().fetch(query, (PID, ))

    output: dict = {}
    for key, subkey, value in data:
        if output == {}:
            output[key] = {}
        else:
            output[key][subkey[:8]] = value

    return output


# Get history of multiple symbols
def get_hists(symbol: str) -> dict:
    symbols = list(symbol.split(","))
    PIDs = tuple(i for i in symbols_n_ids.get_CME_pids(symbols))
    query_start = "SELECT code, updated, last FROM testing WHERE id IN ("
    query = query_start + ("%s," * len(PIDs))[:-1] + ")"
    data = futures_model().fetch(query, PIDs)

    output: dict = {}
    for key, subkey, value in data:
        if key not in output:
            output[key] = {}
        else:
            output[key][subkey[:8]] = value

    return output


# Handling logic behind get-hist endpoint
def handler(symbols: str) -> dict:
    if "," in symbols:
        return get_hists(symbols)
    else:
        return get_hist(symbols)
