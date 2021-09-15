from typing import Optional, Union

from app.models.yields import Meta as yields_model
from app.util import tables


def get_curve(product: str, mr: Optional[bool] = False,
              dates: Optional[Union[str, list]] = None) -> dict:

    table = tables.get_table(product)

    if mr is True:
        data = yields_model().to_dict(table, mr=True)
    else:
        if dates is not None:
            data = yields_model().to_dict(table, keys=dates)
        else:
            data = yields_model().to_dict(table)

    return data


def get_rate(product: str, duration: str,
             dates: Optional[Union[str, list]] = None) -> dict:

    hashmap: dict = {}

    table = tables.get_table(product)
    query = f"SELECT date, {duration} FROM {table}"

    if dates is not None:
        if isinstance(dates, str):
            query = query + f" WHERE date='{dates}'"
        elif isinstance(dates, list):
            keys = str(tuple(i for i in dates))
            query = query + f" WHERE date IN {keys}"
    results = yields_model().fetch(query)

    if dates is None:
        for idx in enumerate(results):
            hashmap[idx[1][0]] = idx[1][1]

    if isinstance(dates, str):
        results_ = str(results)
        start = results_.find("'") + 1
        end = results_[start:].find("'") + start
        hashmap[dates] = results_[start:end]

    elif isinstance(dates, list):
        for idx in enumerate(results):
            hashmap[dates[idx[0]]] = idx[1][0]

    return hashmap
