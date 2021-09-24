import unittest

from app.repositories.yields import curve, rate
from app.tests.mocks import hashmaps


class TestYieldsRepo(unittest.TestCase):
    def test_to_dict(self) -> None:
        scenario = ("2019-03-20", "0.69")
        output = rate.to_dict(scenario)
        self.assertIsInstance(output, dict)

    def test_get_query(self) -> None:
        scenario = ["JGB", "Y10", "2019-03-20"]
        output = rate.get_query(
            scenario[0], scenario[1], scenario[2],
        )
        self.assertIsInstance(output, str)

        expected = "SELECT date, Y10 FROM JGB_table WHERE date='2019-03-20'"
        self.assertEqual(expected, output)

    def test_get_multi_query(self) -> None:
        scenario = ["UST", "M3", ["2018-11-28", "2019-03-20"]]
        output = rate.get_multi_query(
            str(scenario[0]), str(scenario[1]), list(scenario[2]),
        )
        self.assertIsInstance(output, str)

        expected = "SELECT date, M3 FROM usT_table WHERE date IN ('2018-11-28', '2019-03-20')"
        self.assertEqual(expected, output)

    def test_get_queries(self) -> None:
        scenario = ["UKGB", "Y30", ["MOST_RECENT", "2018-11-28"]]
        output = rate.get_queries(
            str(scenario[0]), str(scenario[1]), list(scenario[2]),
        )
        self.assertIsInstance(output, list)

        expected = [
            "SELECT date, Y30 FROM ukGB_table ORDER BY id DESC LIMIT 1",
            "SELECT date, Y30 FROM ukGB_table WHERE date='2018-11-28'",
        ]
        self.assertListEqual(expected, output)

    def test_rate_hist(self) -> None:
        scenario = ["JGB", "Y30"]
        output = rate.get_hist(
            scenario[0], scenario[1],
        )
        self.assertIsInstance(output, dict)
        keys = [key for key in output]
        self.assertGreater(len(keys), 3)

    def test_get_rate(self) -> None:
        scenario = ["UST", "Y10", "2019-03-20"]
        output = rate.get_rate(
            scenario[0], scenario[1], scenario[2],
        )
        self.assertIsInstance(output, dict)
        self.assertDictEqual(output, {scenario[2]: "2.54"})

    def test_get_rates(self) -> None:
        scenario = ["UST", "M1", ["MOST_RECENT", "2021-09-13"]]
        output = rate.get_rates(
            str(scenario[0]), str(scenario[1]), list(scenario[2]),
        )
        self.assertIsInstance(output, dict)
        self.assertEqual(
            len([key for key in output]),
            len(scenario[2]),
        )

    def test_rate_handler(self) -> None:
        scenarios = [
            ["JGB", "Y10", "2009-08-21,2010-05-06,2010-10-25"],
            ["UST", "Y5", "MOST_RECENT,2009-08-21,2010-10-25"],
            ["UKGB", "Y30", "MOST_RECENT,2010-05-06"],
            ["JGB", "M3", "MOST_RECENT"],
            ["UST", "M1", "2009-08-21"],
        ]
        for scenario in scenarios:
            output = rate.handler(scenario)
            self.assertIsInstance(output, dict)

    def test_get_curve(self) -> None:
        scenario = ["UKGB", "2018-11-28"]
        output = curve.get_curve(scenario[0], scenario[1])
        self.assertIsInstance(output, dict)

        expected = hashmaps.get_curve_mock
        self.assertDictEqual(expected, output)

    def test_get_curves(self) -> None:
        scenario = ["JGB", ["2015-03-31", "2020-09-09"]]
        output = curve.get_curves(
            str(scenario[0]), list(scenario[1]),
        )
        self.assertIsInstance(output, dict)

        expected = hashmaps.get_curves_mock
        self.assertDictEqual(expected, output)

    def test_get_mr_curve(self) -> None:
        scenario = "UST"
        output = curve.get_mr_curve(scenario)
        self.assertIsInstance(output, dict)

        keys = [key for key in output]
        self.assertEqual(len([key for key in output[keys[0]]]), 13)

    def test_curve_handler(self) -> None:
        scenarios = [
            ["UKGB", "MOST_RECENT,2012-10-30,2020-09-09"],
            ["JGB", "2012-10-30,2021-07-02,2020-09-09"],
            ["UST", "MOST_RECENT,2021-07-02"],
            ["UKGB", "2021-07-02"],
            ["JGB", "MOST_RECENT"],
        ]
        for scenario in scenarios:
            output = curve.handler(list(scenario))
            self.assertIsInstance(output, dict)

        scenario = ["JGB"]
        self.assertRaises(ValueError)


if __name__ in '__main__':
    unittest.main()
