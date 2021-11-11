import unittest
from unittest import TestCase, mock

import bs4
from bs4 import BeautifulSoup as bs

from app.scripts.yields.JGB.JGB_Collector import Collection as JGB_Model
from app.scripts.yields.ukGB.ukGB_Collector import Collection as UKGB_Model
from app.scripts.yields.usT.usT_Collector import Collection as UST_Model
from app.tests.mocks.web_content import (jgb_web_demo, ukgb_web_demo,
                                         ust_web_demo)


class collectors(TestCase):
    def setUp(self) -> None:
        self.models = [JGB_Model(), UKGB_Model(), UST_Model()]
        self.demo = [jgb_web_demo, ukgb_web_demo, ust_web_demo]
        self.demo_data = [
            [('-0.191%', '-0.112%', '-0.119%', '-0.112%', '-0.119%',
              '-0.121%', '-0.095%', '-0.084%', '0.055%', '0.278%',
              '0.457%', '0.679%', '0.719%', '2021-11-9', '2021')],
            [('-0.034', '0.027', '0.113', '0.312', '0.441',
              '0.495', '0.590', '0.600', '0.823', '0.962',
              '1.013', '0.999', '0.928', '0.817', '2021-11-9', '2021')],
            [('0.04', '0.05', '0.04', '0.06', '0.14', '0.41', '0.71',
              '1.08', '1.32', '1.46', '1.86', '1.83', '2021-11-09', '2021')],
        ]
        self.n = len(self.models)

    def test_get_data(self) -> None:
        with mock.patch("requests.get") as patched:
            for i in range(self.n):
                patched.return_value.text = self.demo[i]
                result = self.models[i].get_data()
                self.assertIsInstance(result, bs4.BeautifulSoup)

    def test_parse_data(self) -> None:
        for i in range(self.n):
            if isinstance(self.models[i], JGB_Model):
                patch = "app.scripts.yields.JGB.JGB_Collector.Collection.get_data"
            elif isinstance(self.models[i], UKGB_Model):
                patch = "app.scripts.yields.ukGB.ukGB_Collector.Collection.get_data"
            else:
                patch = "app.scripts.yields.usT.usT_Collector.Collection.get_data"
            with mock.patch(patch) as patched:
                patched.return_value = bs(self.demo[i], "lxml")
                result = self.models[i].parse_data()
                self.assertEqual(result, self.demo_data[i])

    def test_add_to_db(self) -> None:
        with mock.patch("app.models.database_meta.DB_Meta.executemany") as executemany_patch:
            for i in range(self.n):
                if isinstance(self.models[i], JGB_Model):
                    patch = "app.scripts.yields.JGB.JGB_Collector.Collection.parse_data"
                    cols = "(m1, m3, m6, y1, y2, y3, y5, y7, y10, y15, y20, y30, y40, date, year)"
                    vals_ph = "(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    table = "JGB_table"
                elif isinstance(self.models[i], UKGB_Model):
                    patch = "app.scripts.yields.JGB.JGB_Collector.Collection.parse_data"
                    cols = "(m1, m3, m6, y1, y2, y3, y5, y7, y10, y15, y20, y25, y30, y40, date, year)"
                    vals_ph = "(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    table = "ukGB_table"
                else:
                    patch = "app.scripts.yields.JGB.JGB_Collector.Collection.parse_data"
                    cols = "(m1, m2, m3, m6, y1, y2, y3, y5, y7, y10, y20, y30, date, year)"
                    vals_ph = "(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    table = "usT_table"

                with mock.patch(patch) as parse_patch:
                    parse_patch.return_value = self.demo_data[i]
                    query = f"INSERT INTO {table} {cols} VALUES {vals_ph}"

                    self.models[i].add_to_db(query, self.demo_data[i])
                    executemany_patch.assert_called_with(query, self.demo_data[i])
                    self.assertIsNone(self.models[i].add_to_db(query, self.demo_data[i]))


if __name__ == "__main__":
    unittest.main()
