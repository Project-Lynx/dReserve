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
def handler(payload: list) -> dict:
    product = payload[0]
    dates = list(payload[1].split(","))

    if len(dates) == 1:
        if "MOST_RECENT" in dates:
            return get_mr_curve(product)
        else:
            return get_curve(product, dates[-1])

    elif len(dates) == 2:
        if "MOST_RECENT" in dates:
            return get_mr_curve(product) | get_curve(product, dates[-1])
        else:
            return get_curves(product, dates)

    else:
        if "MOST_RECENT" in dates:
            return get_mr_curve(product) | get_curves(product, dates[1:])
        else:
            return get_curves(product, dates)
