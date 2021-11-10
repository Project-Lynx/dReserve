import requests as req
from bs4 import BeautifulSoup as bs

from app.models.yields.database import Yields_DB
from app.util import tables


class Collection:
    def __init__(self) -> None:
        self.model = Yields_DB()
        self.table = tables.get_table("UST")
        self.dataset: list = []

    def get_data(self) -> bs:
        """Fetch data."""
        url = "https://data.treasury.gov/feed.svc/DailyTreasuryYieldCurveRateData"
        return bs(req.get(url).text, "lxml")

    def parse_data(self) -> list[tuple]:
        """Parsing data."""
        data = self.get_data()
        entries = data.findAll("entry")
        entry = entries[-1]

        unclean_date = entry.find("d:new_date").text
        d_end = unclean_date.find("T")
        date = unclean_date[:d_end]
        year = date[:4]

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
        return [
           (m1, m2, m3, m6, y1, y2, y3, y5,
            y7, y10, y20, y30, date, year),
        ]

    def add_to_db(self) -> None:
        cols = "(m1, m2, m3, m6, y1, y2, y3, y5, y7, y10, y20, y30, date, year)"
        vals_ph = "(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        self.model.executemany(
            f"INSERT INTO {self.table} {cols} VALUES {vals_ph}",
            self.parse_data(),
        )
