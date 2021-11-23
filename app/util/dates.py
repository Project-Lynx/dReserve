def convert_shorthand_month(month: str) -> str:
    """
    Convert string of shorthand
    month to sting of mm form.

    input: 'Jan' or 'jan'
    output: 01
    """
    if not isinstance(month, str):
        raise TypeError(f"{type(month)} not valid type! Must be string.")

    hashmap = {
        "Jan": '01', "jan": "01",
        "Feb": '02', "feb": "02",
        "Mar": '03', "mar": "03",
        "Apr": '04', "apr": "04",
        "May": '05', "may": "05",
        "Jun": '06', "jun": "06",
        "Jul": '07', "jul": "07",
        "Aug": '08', "aug": "08",
        "Sep": '09', "sep": "09",
        "Oct": '10', "oct": "10",
        "Nov": '11', "nov": "11",
        "Dec": '12', "dec": "12",
    }
    try:
        return hashmap[month]

    except KeyError:
        raise KeyError(f"{month} is not valid! Should be Jan-Dec or jan-dec.")
