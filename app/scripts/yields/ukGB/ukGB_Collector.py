import requests as req
from bs4 import BeautifulSoup as bs

from app.models.yields.database import Yields_DB
from app.util import dates, tables


class Collection:
    def __init__(self) -> None:
        self.model = Yields_DB()
        self.table = tables.get_table("UKGB")
        self.dataset: list = []

    def get_data(self) -> bs:
        """Fetch data."""
        url = "http://www.worldgovernmentbonds.com/bond-historical-data/united-kingdom/1-month/"
        return bs(req.get(url).text, "lxml")

    def parse_data(self) -> list[tuple]:
        """Parsing data."""
        data = self.get_data().findAll("td", {'class': "w3-center"})
        date = self.get_data().find("p", {'class': "w3-small w3-right"}).text
        date_list = list(date.split())
        day = date_list[2]
        month = dates.convert_shorthand_month(date_list[3])
        year = date_list[4]
        date_final = f"{year}-{month}-{day}"

        target_data = data[-80:]
        count = 0
        for i in target_data:
            if "%" in i.text:
                count += 1
                if count not in [7, 9, 11, 12, 14, 20]:
                    self.dataset.append(i.text[:-1])
        self.dataset.append(date_final)
        self.dataset.append(year)
        return [tuple(self.dataset)]

    def add_to_db(self) -> None:
        """Add to database."""
        cols = "(m1, m3, m6, y1, y2, y3, y5, y7, y10, y15, y20, y25, y30, y40, date, year)"
        vals_ph = "(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        self.model.executemany(
            f"INSERT INTO {self.table} {cols} VALUES {vals_ph}",
            self.parse_data(),
        )
