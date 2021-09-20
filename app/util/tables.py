def get_table(product: str) -> str:
    table = "ERROR PRODUCT NOT FOUND!"

    if product == "UST":
        table = "usT_table"
    elif product == "JGB":
        table = "JGB_table"
    elif product == "UKGB":
        table = "ukGB_table"

    return table
