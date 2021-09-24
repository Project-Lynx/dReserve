import pymysql

from app.models.yields import Meta as yields_model
from app.util import tables


# Convert results from db to hashmap
def to_dict(results: tuple) -> dict:
    hashmap: dict = {}
    for idx in enumerate(results):
        hashmap[str(idx[1][0])] = idx[1][1]
    return hashmap


# Get query for single date
def get_query(product: str, duration: str, date: str) -> str:
    table = tables.get_table(product)
    if date == "MOST_RECENT":
        return f"SELECT date, {duration} FROM {table} ORDER BY id DESC LIMIT 1"
    else:
        return f"SELECT date, {duration} FROM {table} WHERE date='{date}'"


# Get query for multiple dates
def get_multi_query(product: str, duration: str, dates: list[str]) -> str:
    table = tables.get_table(product)
    keys = str(tuple(i for i in dates))
    query = f"SELECT date, {duration} FROM {table} WHERE date IN {keys}"
    return query


# Get multiple queries for multiple dates
def get_queries(product: str, duration: str, dates: list) -> list:
    table = tables.get_table(product)
    query = f"SELECT date, {duration} FROM {table}"
    mr_query = query + " ORDER BY id DESC LIMIT 1"
    if len(dates) < 3:
        date_query = query + f" WHERE date='{dates[-1]}'"
        return [mr_query, date_query]
    else:
        keys = str(tuple(i for i in dates[1:]))
        dates_query = query + f" WHERE date IN {keys}"
        return [mr_query, dates_query]


# Get historic data on specified product and duration
def get_hist(product: str, duration: str) -> dict:
    table = tables.get_table(product)
    query = f"SELECT date, {duration} FROM {table}"
    result = yields_model().fetch(query)
    return to_dict(result)


# Get data on specified product, duration, and date
def get_rate(product: str, duration: str, date: str) -> dict:
    query = get_query(product, duration, date)
    results = yields_model().fetch(query)
    return to_dict(results)


# Get data on specified product, duration but multiple dates
def get_rates(product: str, duration: str, dates: list[str]) -> dict:
    if "MOST_RECENT" == dates[0]:
        query_list = get_queries(product, duration, dates)
        most_recent = to_dict(yields_model().fetch(query_list[0]))
        dates_data = to_dict(yields_model().fetch(query_list[1]))
        return most_recent | dates_data
    else:
        query = get_multi_query(product, duration, dates)
        results = yields_model().fetch(query)
        return to_dict(results)


# Handle get rate endpoint logic
def handler(payload: list) -> dict:
    try:
        product = payload[0]
        duration = payload[1]
        if payload[-1] is None:
            return get_hist(product, duration)
        else:
            dates = list(payload[-1].split(","))
            if len(dates) <= 1:
                date = str(payload[-1])
                return get_rate(product, duration, date)
            else:
                return get_rates(product, duration, dates)

    except IndexError:
        raise ValueError("Incorrect payload! Should be like for example: \nJGB,M1 or UST,Y10,2008-09-15")
    except pymysql.err.OperationalError:
        raise ValueError("Incorrect payload! Make sure it includes a product, duration and or dates")
