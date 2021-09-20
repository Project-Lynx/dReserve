import requests as req
from bs4 import BeautifulSoup as bs

from app.models.yields import Meta as yields_model
from app.util import dates, tables

# Define model & table
model = yields_model()
table = tables.get_table("UKGB")

# Collect data
url = "http://www.worldgovernmentbonds.com/bond-historical-data/united-kingdom/1-month/"
response = req.request("GET", url)
parsed = bs(response.text, "lxml")

# Parse dates to target format
data = parsed.findAll("td", {'class': "w3-center"})
date = parsed.find("p", {'class': "w3-small w3-right"}).text
date_list = list(date.split())
day = date_list[2]
month = dates.convert_shorthand_month(date_list[3])
year = date_list[4]

date_final = f"{year}-{month}-{day}"

# Define collected data
target_data = data[-80:]

# Parse data to fit model
_list_: list = []
count = 0
for i in target_data:
    if "%" in i.text:
        count += 1
        if count not in [7, 9, 11, 12, 14, 20]:
            _list_.append(i.text[:-1])
_list_.append(date_final)
_list_.append(year)
temp_list = [tuple(_list_)]

# Adding data to table
cols = "(m1, m3, m6, y1, y2, y3, y5, y7, y10, y15, y20, y25, y30, y40, date, year)"
vals_ph = "(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
model.executemany(
    f"INSERT INTO {table} {cols} VALUES {vals_ph}",
    temp_list,
)
