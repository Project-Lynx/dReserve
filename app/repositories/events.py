import sqlite3


def get_events(regions):
    events_output = {}

    connec = sqlite3.connect('app/data/econ_events.db')
    cursor = connec.cursor()
    
    for region in regions:
        cursor.execute(f"SELECT * FROM events WHERE region='{region}'")
        data = cursor.fetchall()

        for key, val1, val2, val3, val4 in data:
            events_output[key] = [val1, val2, val3, val4]

    return events_output
