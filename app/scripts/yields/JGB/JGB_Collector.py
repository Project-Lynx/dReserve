import requests as req
from bs4 import BeautifulSoup as bs

from app.models.yields import Meta as yields_model
from app.util import dates, tables

# Define model & table
model = yields_model()
table = tables.get_table("JGB")

# Collect data
url = "http://www.worldgovernmentbonds.com/bond-historical-data/japan/1-month/"
response = req.request("GET", url)
parsed = bs(response.text, "lxml")

# Parse dates to target format
target_data = parsed.findAll("tbody")[-1]
date_item = parsed.find("p", {'class': "w3-small w3-right"}).text
date_pre = list(date_item.split(" "))
day = date_pre[2]
month = dates.convert_shorthand_month(date_pre[3])
year = date_pre[4]

date_final = f"{year}-{month}-{day}"

# Parse data to fit model
_list_: list = []
count = 0
for i in target_data:
    if hasattr(i, 'bs4.element.Tag'):
        if "%" in i.text:
            count += 1
            if count not in [4, 8, 10, 12, 13]:
                d_list = (i.text).splitlines()
                for j in d_list:
                    if "%" in j:
                        print(j[:-1])
                        _list_.append(j)
_list_.append(date_final)
_list_.append(year)
temp_list = [tuple(_list_)]

# Adding data to table
cols = "(m1, m3, m6, y1, y2, y3, y5, y7, y10, y15, y20, y30, y40, date, year)"
vals_ph = "(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
model.executemany(
    f"INSERT INTO {table} {cols} VALUES {vals_ph}",
    temp_list,
)
