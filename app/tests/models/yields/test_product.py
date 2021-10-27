import datetime
import unittest
from unittest import TestCase, mock

from app.models.yields.product import JGB, UKGB, UST, Product


class Test_Product(TestCase):
    def test_export_info(self) -> None:
        result = Product("UST", ["current", "previous"]).export_info()
        cols = "m1,m2,m3,m6,y1,y2,y3,y5,y7,y10,y20,y30,date"
        expected = ["usT_table", cols, UST]
        self.assertEqual(result, expected)

    def test_fetch_data(self) -> None:
        with mock.patch('app.models.yields.database.DB_Model.fetch') as patched:
            patched.return_value = None
            expected_query = ["SELECT date,y30 FROM JGB_table ORDER BY id DESC LIMIT 1", False]
            Product("JGB", ["current"], "y30").fetch_data(expected_query)
            patched.assert_called_with(expected_query, ["current"])

            cols = "m1,m2,m3,m6,y1,y2,y3,y5,y7,y10,y20,y30,date"
            expected_a = f"(SELECT {cols} FROM usT_table ORDER BY id DESC LIMIT 1)"
            expected_b = f"(SELECT {cols} FROM usT_table ORDER BY id DESC LIMIT 1, 1)"
            expected_query = [f"{expected_a} UNION {expected_b}", False]
            Product("UST", ["current", "previous"]).fetch_data(expected_query)
            patched.assert_called_with(expected_query, ["current", "previous"])

    def test_rate_to_dict(self) -> None:
        with mock.patch('app.models.yields.database.DB_Model.fetch') as patched:
            patched.return_value = (
                ('2021-10-8', '0.02'),
            )
            query = ["SELECT date,y10 FROM usT_table ORDER BY id DESC LIMIT 1, 1", False]
            result = Product("UST", ["previous"], "y10").rate_to_dict(query)
            expected = {'2021-10-8': '0.02'}
            self.assertDictEqual(expected, result)

            patched.return_value = (
                ("2021-10-08", "1.61"),
                ("2021-10-07", "1.58"),
            )
            query_a = "(SELECT date,y10 FROM ukGB_table ORDER BY id DESC LIMIT 1)"
            query_b = "(SELECT date,y10 FROM ukGB_table ORDER BY id DESC LIMIT 1, 1)"
            query = [f"{query_a} UNION {query_b}", False]
            result = Product("UKGB", ["current", "previous"], "y10").rate_to_dict(query)
            expected = {"2021-10-08": "1.61", "2021-10-07": "1.58"}
            self.assertDictEqual(expected, result)


class Test_UKGB(TestCase):
    def test_to_dict(self) -> None:
        with mock.patch('app.models.yields.database.DB_Model.fetch') as patched:
            cols = "m1,m3,m6,y1,y2,y3,y5,y7,y10,y15,y20,y25,y30,y40,date"
            query = [f"SELECT {cols} from UKGB_table ORDER BY id DESC LIMIT 1", False]
            patched.return_value = (
                ('-', '-', '-', '0.1', '0.16', '0.21', '0.35', '0.49', '0.71',
                 '0.98', '1.1', '1.12', '1.08', '0.95', datetime.date(2021, 8, 31)),
            )
            result = UKGB(["current"]).to_dict(query)
            expected = {
                "2021-08-31": {
                    "1 month": "-", "3 month": "-", "6 month": "-",
                    "1 year": "0.1", "2 year": "0.16", "3 year": "0.21",
                    "5 year": "0.35", "7 year": "0.49", "10 year": "0.71",
                    "15 year": "0.98", "20 year": "1.1", "25 year": "1.12",
                    "30 year": "1.08", "40 year": "0.95",
                },
            }
            patched.assert_called_with(query, ["current"])
            self.assertDictEqual(expected, result)

    def test_create_table(self) -> None:
        with mock.patch('app.models.yields.database.DB_Model.create_table') as patched:
            query = """create table if not exists ukgb_table
                   (id int not null auto_increment primary key,
                   m1 varchar(10), m3 varchar(10), m6 varchar(10),
                   y1 varchar(10), y2 varchar(10), y3 varchar(10),
                   y5 varchar(10), y7 varchar(10), y10 varchar(10),
                   y15 varchar(10), y20 varchar(10), y25 varchar(10),
                   y30 varchar(10), y40 varchar(10), date date, year year)
                """
            patched.return_value = None
            UKGB(["current", "previous"]).create_table()
            patched.assert_called_with(query)


class Test_JGB(TestCase):
    def test_to_dict(self) -> None:
        with mock.patch('app.models.yields.database.DB_Model.fetch') as patched:
            cols = "m1,m3,m6,y1,y2,y3,y5,y7,y10,y15,y20,y30,y40,date"
            query = [f"SELECT {cols} from UKGB_table ORDER BY id DESC LIMIT 1, 1", False]
            patched.return_value = (
                ('-', '-', '-', '-0.138', '-0.128', '-0.13', '-0.118', '-0.111',
                 '0.025', '0.217', '0.406', '0.653', '0.729', datetime.date(2021, 8, 30)),
            )
            result = JGB(["previous"]).to_dict(query)
            expected = {
                "2021-08-30": {
                    "1 month": "-", "3 month": "-", "6 month": "-", "1 year": "-0.138",
                    "2 year": "-0.128", "3 year": "-0.111", "5 year": "-0.118", "7 year": "-0.111",
                    "10 year": "0.025", "15 year": "0.217", "20 year": "0.406", "30 year": "0.653",
                    "40 year": "0.729",
                },
            }
            patched.assert_called_with(query, ["previous"])
            self.assertDictEqual(expected, result)

    def test_create_table(self) -> None:
        with mock.patch('app.models.yields.database.DB_Model.create_table') as patched:
            query = """CREATE TABLE IF NOT EXISTS JGB_table
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                   m1 varchar(10), m3 varchar(10), m6 varchar(10),
                   y1 varchar(10), y2 varchar(10), y3 varchar(10),
                   y5 varchar(10), y7 varchar(10), y10 varchar(10),
                   y15 varchar(10), y20 varchar(10), y30 varchar(10),
                   y40 varchar(10), date DATE, year YEAR)
                """
            patched.return_value = None
            JGB().create_table()
            patched.assert_called_with(query)


class Test_UST(TestCase):
    def test_to_dict(self) -> None:
        with mock.patch('app.models.yields.database.DB_Model.fetch') as patched:
            cols = "m1,m2,m3,m6,y1,y2,y3,y5,y7,y10,y20,y30,date"
            query = [f"SELECT {cols} from usT_table WHERE date=%s", True]
            patched.return_value = (
                ('0.1', '0.04', '0.04', '0.06', '0.09', '0.28', '0.54', '0.98',
                 '1.32', '1.54', '2.04', '2.1', datetime.date(2021, 10, 5)),
            )
            result = UST(["2021-10-05"]).to_dict(query)
            expected = {
                "2021-10-05": {
                    "1 month": "0.1", "2 month": "0.04", "3 month": "0.04", "6 month": "0.06",
                    "1 year": "0.09", "2 Year": "0.28", "3 year": "0.54", "5 year": "0.98",
                    "7 year": "1.32", "10 year": "1.54", "20 year": "2.04", "30 year": "2.1",
                },
            }
            patched.assert_called_with(query, ["2021-10-05"])
            self.assertDictEqual(expected, result)

    def test_create_table(self) -> None:
        with mock.patch('app.models.yields.database.DB_Model.create_table') as patched:
            query = """CREATE TABLE IF NOT EXISTS usT_table
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                   m1 varchar(10), m2 varchar(10), m3 varchar(10),
                   m6 varchar(10), y1 varchar(10), y2 varchar(10),
                   y3 varchar(10), y5 varchar(10), y7 varchar(10),
                   y10 varchar(10), y20 varchar(10), y30 varchar(10),
                   date DATE, year YEAR)
                """
            patched.return_value = None
            UST().create_table()
            patched.assert_called_with(query)


if __name__ in '__main__':
    unittest.main()
