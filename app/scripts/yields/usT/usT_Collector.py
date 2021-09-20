import requests as req
from bs4 import BeautifulSoup as bs

from app.models.yields import Meta as yields_model
from app.util import tables

# Define Model & Table
model = yields_model()
table = tables.get_table("UST")

# Collect data
url = "https://data.treasury.gov/feed.svc/DailyTreasuryYieldCurveRateData"
response = req.request("GET", url)
parsed = bs(response.text, "lxml")

# Target data
entries = parsed.findAll("entry")
entry = entries[-1]

# Parse dates
_date = entry.find("d:new_date").text
d_end = _date.find("T")
_date = _date[:d_end]
year = _date[:4]

# Parse data to fit model
m1 = entry.find("d:bc_1month").text
m2 = entry.find("d:bc_2month").text
m3 = entry.find("d:bc_3month").text
m6 = entry.find("d:bc_6month").text
y1 = entry.find("d:bc_1year").text
y2 = entry.find("d:bc_2year").text
y3 = entry.find("d:bc_3year").text
y5 = entry.find("d:bc_5year").text
y7 = entry.find("d:bc_7year").text
y10 = entry.find("d:bc_10year").text
y20 = entry.find("d:bc_20year").text
y30 = entry.find("d:bc_30year").text
temp_list = [(
   m1, m2, m3, m6, y1, y2, y3, y5,
   y7, y10, y20, y30, _date, year,
)]

# Adding data to table
cols = "(m1, m2, m3, m6, y1, y2, y3, y5, y7, y10, y20, y30, date, year)"
vals_ph = "(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
model.executemany(
    f"INSERT INTO {table} {cols} VALUES {vals_ph}",
    temp_list,
)
