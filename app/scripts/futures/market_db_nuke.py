import sqlite3

connec = sqlite3.connect('app/data/market_data.db')
cursor = connec.cursor()

table_names = [
    "ES", "ZN", "GE", "CL", "NG", "DX",
]

for name in table_names:
    cursor.execute(f"DROP TABLE {name}")
