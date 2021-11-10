from typing import Type

import requests as req
from bs4 import BeautifulSoup as bs

from app.models.yields.database import Yields_DB
from app.util import tables


class Meta:
    def __init__(self, table_name: str, db_model: Type[Yields_DB]) -> None:
        self.model = db_model()
        self.table = tables.get_table(table_name)
        self.dataset: list = []

    def get_data(self, url: str) -> bs:
        return bs(req.get(url).text, "lxml")

    def add_to_db(self, query: str, data: list[tuple]) -> None:
        self.model.executemany(query, data)
