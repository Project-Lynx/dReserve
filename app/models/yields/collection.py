from typing import Type

import requests as req
from bs4 import BeautifulSoup as bs

from app.models.yields.database import Yields_DB
from app.util import tables


class Meta:
    def __init__(self, url: str, table_name: str, db_model: Type[Yields_DB]) -> None:
        self.url = url
        self.model = db_model()
        self.dataset: list = []
        self.table = tables.get_table(table_name)

    def get_data(self) -> bs:
        """Fetch data from webpage."""
        return bs(req.get(self.url).text, "lxml")

    def add_to_db(self, query: str, data: list[tuple]) -> None:
        """Add data to database."""
        self.model.executemany(query, data)
