import requests as req
from bs4 import BeautifulSoup as bs

from app.models.yields import Meta as yields_model
from app.util import dates

model = yields_model()

url = "http://www.worldgovernmentbonds.com/bond-historical-data/united-kingdom/1-month/"
response = req.request("GET", url)
parsed = bs(response.text, "lxml")

data = parsed.findAll("td", {'class': "w3-center"})
date = parsed.find("p", {'class': "w3-small w3-right"}).text
d_start = date.find(":")+2
d_end = date.find("G")-7
date = date[d_start:d_end]
date_list = list(date.split(" "))
day = date_list[0]
month = date_list[1]
month = dates.convert_shorthand_month(month)
year = date_list[2]

date = f"{year}-{month}-{day}"

target_data = data[-80:]


_list_ = [date]
count = 0
for i in target_data:
    if "%" in i.text:
        count += 1
        if count not in [7, 9, 11, 12, 14, 20]:
            _list_.append(i.text[:-1])
temp_list = [tuple(_list_)]

vals_ph = "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s"

model.executemany(
    f"INSERT INTO UKGB_table VALUES ({vals_ph})",
    temp_list,
)
