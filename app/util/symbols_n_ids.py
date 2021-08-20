from app.data.CME_Futures import futures_map

"""
    Convert Futures symbols to product id's
"""
def get_CME_pids(symbols):
    if isinstance(symbols, str):
        return futures_map[symbols]

    if isinstance(symbols, list):
        pids = []
        for symbol in symbols:
            pids.append(futures_map[symbol])

        return pids

