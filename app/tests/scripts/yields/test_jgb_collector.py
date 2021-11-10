import unittest
from unittest import TestCase, mock

import bs4
from bs4 import BeautifulSoup as bs

from app.scripts.yields.JGB.JGB_Collector import Collection
from app.tests.mocks.web_content import jgb_web_demo


class test_jgb_collector(TestCase):
    def setUp(self) -> None:
        self.model = Collection()
        self.demo = jgb_web_demo
        self.demo_data = [('-0.191%', '-0.112%', '-0.119%', '-0.112%', '-0.119%',
                           '-0.121%', '-0.095%', '-0.084%', '0.055%', '0.278%',
                           '0.457%', '0.679%', '0.719%', '2021-11-9', '2021')]

    def test_get_data(self) -> None:
        with mock.patch("requests.get") as patched:
            patched.return_value.text = self.demo
            url = "http://www.worldgovernmentbonds.com/bond-historical-data/japan/1-month/"
            result = self.model.get_data(url)
            self.assertIsInstance(result, bs4.BeautifulSoup)

    def test_parse_data(self) -> None:
        with mock.patch("app.scripts.yields.JGB.JGB_Collector.Collection.get_data") as patched:
            patched.return_value = bs(self.demo, "lxml")
            result = self.model.parse_data()
            self.assertEqual(result, self.demo_data)

    def test_add_to_db(self) -> None:
        with mock.patch("app.models.database_meta.DB_Meta.executemany") as executemany_patch:
            with mock.patch("app.scripts.yields.JGB.JGB_Collector.Collection.parse_data") as parse_patch:
                parse_patch.return_value = self.demo_data
                cols = "(m1, m3, m6, y1, y2, y3, y5, y7, y10, y15, y20, y30, y40, date, year)"
                vals_ph = "(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                query = f"INSERT INTO JGB_table {cols} VALUES {vals_ph}"

                result = self.model.add_to_db(query, self.demo_data)
                executemany_patch.assert_called_with(query, self.demo_data)
                self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
