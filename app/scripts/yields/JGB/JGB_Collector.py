import requests as req
from bs4 import BeautifulSoup as bs

from app.models.yields.database import Yields_DB
from app.util import dates, tables


class Collection:
    def __init__(self) -> None:
        self.model = Yields_DB()
        self.table = tables.get_table("JGB")
        self.dataset: list = []

    def get_data(self) -> bs:
        """Fetch data."""
        url = "http://www.worldgovernmentbonds.com/bond-historical-data/japan/1-month/"
        return bs(req.get(url).text, "lxml")

    def parse_data(self) -> list[tuple]:
        """Parsing data."""
        data = self.get_data()

        target_data = data.findAll("tbody")[-1]
        date_item = data.find("p", {'class': "w3-small w3-right"}).text
        date_pre = list(date_item.split(" "))
        day = date_pre[2]
        month = dates.convert_shorthand_month(date_pre[3])
        year = date_pre[4]
        date_final = f"{year}-{month}-{day}"

        count = 0
        for i in target_data:
            if hasattr(i, 'bs4.element.Tag') and "%" in i.text:
                count += 1
                if count not in [4, 8, 10, 12, 13]:
                    d_list = (i.text).splitlines()
                    for j in d_list:
                        if "%" in j:
                            self.dataset.append(j)
        self.dataset.append(date_final)
        self.dataset.append(year)
        return [tuple(self.dataset)]

    def add_to_db(self) -> None:
        """Add to database."""
        cols = "(m1, m3, m6, y1, y2, y3, y5, y7, y10, y15, y20, y30, y40, date, year)"
        vals_ph = "(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        self.model.executemany(
            f"INSERT INTO {self.table} {cols} VALUES {vals_ph}",
            self.parse_data(),
        )
