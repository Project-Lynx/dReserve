def convert_shorthand_month(month: str) -> str:
    if not isinstance(month, str):
        raise TypeError(f"{month} Not Valid! Should be a string like 'Jan' or 'Dec' ")

    if month == 'Jan':
        return '01'
    elif month == 'Feb':
        return '02'
    elif month == 'Mar':
        return '03'
    elif month == 'Apr':
        return '04'
    elif month == 'May':
        return '05'
    elif month == 'Jun':
        return '06'
    elif month == 'Jul':
        return '07'
    elif month == 'Aug':
        return '08'
    elif month == 'Sep':
        return '09'
    elif month == 'Oct':
        return '10'
    elif month == 'Nov':
        return '11'
    elif month == 'Dec':
        return '12'

    else:
        raise ValueError(f"{month} Not Valid! Examples of valid passes: 'Jan'...'Dec'")
