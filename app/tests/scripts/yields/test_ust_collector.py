import unittest
from unittest import TestCase, mock

import bs4
from bs4 import BeautifulSoup as bs

from app.scripts.yields.usT.usT_Collector import Collection
from app.tests.mocks.web_content import ust_web_demo


class Test_Collection(TestCase):
    def setUp(self) -> None:
        self.model = Collection()
        self.demo = ust_web_demo
        self.demo_data = [
            ('0.04', '0.05', '0.04', '0.06', '0.14', '0.41', '0.71',
             '1.08', '1.32', '1.46', '1.86', '1.83', '2021-11-09', '2021'),
        ]

    def test_get_data(self) -> None:
        with mock.patch("requests.get") as patched:
            patched.return_value.text = self.demo
            result = self.model.get_data()
            self.assertIsInstance(result, bs4.BeautifulSoup)

    def test_parse_data(self) -> None:
        with mock.patch("app.scripts.yields.usT.usT_Collector.Collection.get_data") as patched:
            patched.return_value = bs(self.demo, "lxml")
            result = self.model.parse_data()
            self.assertEqual(result, self.demo_data)

    def test_add_to_db(self) -> None:
        with mock.patch("app.models.database_meta.DB_Meta.executemany") as executemany_patch:
            with mock.patch("app.scripts.yields.usT.usT_Collector.Collection.parse_data") as parse_patch:
                parse_patch.return_value = self.demo_data
                cols = "(m1, m2, m3, m6, y1, y2, y3, y5, y7, y10, y20, y30, date, year)"
                vals_ph = "(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                query = f"INSERT INTO usT_table {cols} VALUES {vals_ph}"

                self.model.add_to_db(query, self.demo_data)
                executemany_patch.assert_called_with(query, self.demo_data)
                self.assertIsNone(self.model.add_to_db(query, self.demo_data))


if __name__ == '__main__':
    unittest.main()
