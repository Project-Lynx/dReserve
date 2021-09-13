import requests as req
from bs4 import BeautifulSoup as bs

from app.models.yields import Meta as yields_model
from app.util import dates

model = yields_model()

url = "http://www.worldgovernmentbonds.com/bond-historical-data/japan/1-month/"
response = req.request("GET", url)
parsed = bs(response.text, "lxml")

target_data = parsed.findAll("tbody")[-1]
date_item = parsed.find("p", {'class': "w3-small w3-right"}).text
date_pre = list(date_item.split(" "))
day = date_pre[2]
month_pre = date_pre[3]
month = dates.convert_shorthand_month(month_pre)
year = date_pre[4]
date_final = f"{year}-{month}-{day}"

count = 0
_temp_list_ = [date_final]

for i in target_data:
    if hasattr(i, 'bs4.element.Tag'):
        if "%" in i.text:
            count += 1
            if count not in [4, 8, 10, 12, 13]:
                d_list = (i.text).splitlines()
                for j in d_list:
                    if "%" in j:
                        _temp_list_.append(j)
temp_list = [tuple(_temp_list_)]
vals_ph = "(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

model.executemany(
    f"INSERT INTO JGB_table VALUES {vals_ph}",
    temp_list,
)
