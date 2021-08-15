import sqlite3

connec = sqlite3.connect('app/data/econ_events.db')
cursor = connec.cursor()

cursor.execute("DROP TABLE events") 
