import pymysql

from app.models.yields import Meta as yields_model
from app.util import tables


# Get curve of a specified date
def get_curve(product: str, date: str) -> dict:
    table = tables.get_table(product)
    return yields_model().to_dict(table, date)


# Get multiple curves from specified dates
def get_curves(product: str, dates: list) -> dict:
    table = tables.get_table(product)
    return yields_model().to_dict(table, dates)


# Get the most recent curve for a product
def get_mr_curve(product: str) -> dict:
    table = tables.get_table(product)
    return yields_model().to_dict(table, "MOST_RECENT")


# Handle logic to get the right curve(s)
def handle_get_curve(payload: str) -> dict:
    try:
        data_list = list(payload.split(","))
        product = data_list[0]
        dates = data_list[1:]
        if len(dates) == 1:
            if "MOST_RECENT" in dates:
                return get_mr_curve(product)
            else:
                return get_curve(product, dates[-1])
        elif len(dates) > 2:
            if "MOST_RECENT" in dates:
                return get_mr_curve(product) | get_curves(product, dates[1:])
            else:
                return get_curves(product, dates)
        else:
            if "MOST_RECENT" in dates:
                return get_mr_curve(product) | get_curve(product, dates[-1])
            else:
                return get_curves(product, dates)

    except pymysql.err.ProgrammingError:
        raise ValueError("Incorrect Payload, Format must be:\nProduct,Date(YYYY-MM-DD or MOST_RECENT)")


# Convert results from db to hashmap
def to_dict(results: tuple) -> dict:
    hashmap: dict = {}
    for idx in enumerate(results):
        hashmap[str(idx[1][0])] = idx[1][1]
    return hashmap


# Get query for single date
def rate_query(product: str, duration: str, date: str) -> str:
    table = tables.get_table(product)
    if date is not None:
        if date == "MOST_RECENT":
            return f"SELECT date, {duration} FROM {table} ORDER BY id DESC LIMIT 1"
        else:
            return f"SELECT date, {duration} FROM {table} WHERE date='{date}'"


# Get query for multiple dates
def rates_query(product: str, duration: str, dates: list[str]) -> str:
    table = tables.get_table(product)
    keys = str(tuple(i for i in dates))
    query = f"SELECT date, {duration} FROM {table} WHERE date IN {keys}"
    return query


# Get multiple queries for multiple dates
def rate_queries(product: str, duration: str, dates: list) -> list:
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
def get_rate_hist(product: str, duration: str) -> dict:
    table = tables.get_table(product)
    query = f"SELECT date, {duration} FROM {table}"
    result = yields_model().fetch(query)
    return to_dict(result)


# Get data on specified product, duration, and date
def get_rate(product: str, duration: str, date: str) -> dict:
    query = rate_query(product, duration, date)
    results = yields_model().fetch(query)
    return to_dict(results)


# Get data on specified product, duration but multiple dates
def get_rates(product: str, duration: str, dates: list[str]) -> dict:
    if "MOST_RECENT" == dates[0]:
        queries = rate_queries(product, duration, dates)
        most_recent = to_dict(yields_model().fetch(queries[0]))
        dates_data = to_dict(yields_model().fetch(queries[1]))
        return most_recent | dates_data
    else:
        query = rates_query(product, duration, dates)
        results = yields_model().fetch(query)
        return to_dict(results)


# Handle get rate endpoint logic
def handle_get_rate(payload: str) -> dict:
    try:
        data_list = list(payload.split(","))
        product = data_list[0]
        duration = data_list[1]
        if len(data_list) == 2:
            return get_rate_hist(product, duration)
        else:
            dates = data_list[2:]
            if len(dates) <= 1:
                date = str(data_list[2])
                return get_rate(product, duration, date)
            else:
                return get_rates(product, duration, dates)

    except IndexError:
        raise ValueError("Incorrect payload! Should be like for example: \nJGB,M1 or UST,Y10,2008-09-15")
