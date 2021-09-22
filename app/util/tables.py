def get_table(product: str) -> str:
    if product == "UST":
        return "usT_table"
    elif product == "JGB":
        return "JGB_table"
    elif product == "UKGB":
        return "ukGB_table"
    else:
        raise ValueError(f"{product} Not Found!")
