def convert_shorthand_month(month: str) -> str:
    output = """
             ERROR, check if month passed is a shorthand.
             Example: Jan, Feb, Mar, Apr, May, Jun, ..., Dec
             """
    
    if month == 'Jan':
        output = '01'
    elif month == 'Feb':
        output = '02'
    elif month == 'Mar':
        output = '03'
    elif month == 'Apr':
        output = '04'
    elif month == 'May':
        output = '05'
    elif month == 'Jun':
        output = '06'
    elif month == 'Jul':
        output = '07'
    elif month == 'Aug':
        output = '08'
    elif month == 'Sep':
        output = '09'
    elif month == 'Oct':
        output = '10'
    elif month == 'Nov':
        output = '11'
    elif month == 'Dec':
        output = '12'

    return output

