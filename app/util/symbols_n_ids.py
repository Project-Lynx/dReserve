from typing import Union

from app.data.CME_Futures import futures_map


# Convert Futures symbols to product id's
def get_CME_pids(symbols: Union[str, list]) -> Union[str, list]:
    if isinstance(symbols, str):
        return futures_map[symbols]

    if isinstance(symbols, list):
        pids = []
        for symbol in symbols:
            pids.append(futures_map[symbol])

        return pids
