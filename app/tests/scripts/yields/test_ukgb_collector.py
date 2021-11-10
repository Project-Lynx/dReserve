import unittest
from unittest import TestCase, mock

import bs4
from bs4 import BeautifulSoup as bs

from app.scripts.yields.ukGB.ukGB_Collector import Collection
from app.tests.mocks.web_content import ukgb_web_demo


class test_ukgb_collector(TestCase):
    def setUp(self) -> None:
        self.model = Collection()
        self.demo = ukgb_web_demo
        self.demo_data = [('-0.034', '0.027', '0.113', '0.312', '0.441',
                           '0.495', '0.590', '0.600', '0.823', '0.962',
                           '1.013', '0.999', '0.928', '0.817', '2021-11-9', '2021')]

    def test_get_data(self) -> None:
        with mock.patch("requests.get") as patched:
            patched.return_value.text = self.demo
            result = self.model.get_data()
            self.assertIsInstance(result, bs4.BeautifulSoup)

    def test_parse_data(self) -> None:
        with mock.patch("app.scripts.yields.ukGB.ukGB_Collector.Collection.get_data") as patched:
            patched.return_value = bs(self.demo, "lxml")
            result = self.model.parse_data()
            self.assertEqual(result, self.demo_data)

    def test_add_to_db(self) -> None:
        with mock.patch("app.models.database_meta.DB_Meta.executemany") as executemany_patch:
            with mock.patch("app.scripts.yields.ukGB.ukGB_Collector.Collection.parse_data") as parse_patch:
                parse_patch.return_value = self.demo_data
                cols = "(m1, m3, m6, y1, y2, y3, y5, y7, y10, y15, y20, y25, y30, y40, date, year)"
                vals_ph = "(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                query = f"INSERT INTO ukGB_table {cols} VALUES {vals_ph}"

                self.model.add_to_db(query, self.demo_data)
                executemany_patch.assert_called_with(query, self.demo_data)
                self.assertIsNone(self.model.add_to_db(query, self.demo_data))


if __name__ == '__main__':
    unittest.main()
