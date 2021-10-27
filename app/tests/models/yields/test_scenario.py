import unittest
from unittest import TestCase, mock

from app.models.yields.scenario import (Context, Dates_Strategy, No_Dates,
                                        a_date, multi_dates)


class Test_Context(TestCase):
    def test_execute_strategy(self) -> None:
        with mock.patch('app.models.yields.product.UST.to_dict') as patched:
            Context().execute_strategy(a_date("UST", ["current"]))
            patched.assert_called()

        with mock.patch('app.models.yields.product.Product.rate_to_dict') as patched:
            Context().execute_strategy(a_date("JGB", ["2021-06-24"], "y30"))
            expected_query = ["SELECT date,y30 FROM JGB_table WHERE date=%s", True]
            patched.assert_called_with(expected_query)

        with mock.patch('app.models.yields.product.UKGB.to_dict') as patched:
            Context().execute_strategy(multi_dates("UKGB", ["current", "previous"]))
            cols = "m1,m3,m6,y1,y2,y3,y5,y7,y10,y15,y20,y25,y30,y40,date"
            expected_a = f"(SELECT {cols} FROM ukGB_table ORDER BY id DESC LIMIT 1)"
            expected_b = f"(SELECT {cols} FROM ukGB_table ORDER BY id DESC LIMIT 1, 1)"
            expected_query = [f"{expected_a} UNION {expected_b}", False]
            patched.assert_called_with(expected_query)


class Test_Dates_Strategy(TestCase):
    def test_get_internals(self) -> None:
        scenario = ["UST", ["current", "previous"], "y30"]
        product = scenario[0]
        dates = scenario[1]
        duration = scenario[2]
        result = Dates_Strategy(
            product,
            dates,
            duration,
        ).get_internals()
        self.assertEqual(scenario, result)

        scenario = ["JGB", ["current"], ""]
        product = scenario[0]
        dates = scenario[1]
        duration = scenario[2]
        result = Dates_Strategy(
            product,
            dates,
            duration,
        ).get_internals()
        self.assertEqual(scenario, result)

    def test_execute(self) -> None:
        with mock.patch('app.models.yields.product.UST.to_dict') as patched:
            scenario_class = Dates_Strategy("UST", ["Current"])
            cols = "m1,m2,m3,m6,y1,y2,y3,y5,y7,y10,y20,y30,date"
            scenario_query = [f"SELECT {cols} FROM usT_table ORDER BY id DESC LIMIT 1", False]
            scenario_class.execute(scenario_query)
            patched.assert_called_with(scenario_query)

        with mock.patch('app.models.yields.product.Product.rate_to_dict') as patched:
            scenario_class = Dates_Strategy("JGB", ["current"], "y30")
            scenario_query = ["SELECT date,y30 FROM JGB_table ORDER BY id DESC LIMIT 1", False]
            scenario_class.execute(scenario_query)
            patched.assert_called_with(scenario_query)


class Test_multi_dates(TestCase):
    def test_make_query(self) -> None:
        result = multi_dates("JGB", ["current", "previous"], "y30").make_query()
        expected_a = "(SELECT date,y30 FROM JGB_table ORDER BY id DESC LIMIT 1)"
        expected_b = "(SELECT date,y30 FROM JGB_table ORDER BY id DESC LIMIT 1, 1)"
        expected = [f"{expected_a} UNION {expected_b}", False]
        self.assertEqual(result, expected)

        result = multi_dates("UKGB", ["previous", "2021-7-29"]).make_query()
        cols = "m1,m3,m6,y1,y2,y3,y5,y7,y10,y15,y20,y25,y30,y40,date"
        expected_a = f"(SELECT {cols} FROM ukGB_table ORDER BY id DESC LIMIT 1, 1)"
        expected_b = f"(SELECT {cols} FROM ukGB_table WHERE date IN %s)"
        expected = [f"{expected_a} UNION {expected_b}", True]
        self.assertEqual(result, expected)


class Test_No_Dates(TestCase):
    def test_execute(self) -> None:
        scenarios: list[list[str]] = [
            ["UST", ""],
            ["UKGB", "y30"],
        ]
        for scenario in scenarios:
            if scenario[1] is None:
                with mock.patch('app.models.yields.product.Product.fetch_data') as fetch_data_patch:
                    with mock.patch('app.models.yields.product.UST.to_dict') as UST_to_dict_patch:
                        cols = "m1,m2,m3,m6,y1,y2,y3,y5,y7,y10,y20,y30,date"
                        expected_query = [f"SELECT {cols} FROM usT_table", False]
                        fetch_data_patch.return_value = (
                            ('0.02', '0.07', '0.05', '0.07', '0.09', '0.32', '0.59',
                             '1.05', '1.39', '1.61', '2.11', '2.16', '2021-10-8'),
                        )
                        UST_to_dict_patch.return_value = None
                        No_Dates().execute(scenario[0])
                        UST_to_dict_patch.assert_called_with(expected_query)

            else:
                with mock.patch('app.models.yields.product.Product.fetch_data') as fetch_data_patch:
                    with mock.patch('app.models.yields.product.Product.rate_to_dict') as rate_to_dict_patch:
                        expected_query = [f"SELECT date,{scenario[1]} FROM ukGB_table", False]
                        fetch_data_patch.return_value = (('2021-10-8', '1.61'),)
                        No_Dates().execute(scenario[0], scenario[1])
                        rate_to_dict_patch.assert_called_with(expected_query)


class Test_a_date(TestCase):
    def test_make_query(self) -> None:
        result = a_date("UST", ["previous"], "m1").make_query()
        expected = ["SELECT date,m1 FROM usT_table ORDER BY id DESC LIMIT 1, 1", False]
        self.assertEqual(expected, result)

        result = a_date("JGB", ["current"]).make_query()
        cols = "m1,m3,m6,y1,y2,y3,y5,y7,y10,y15,y20,y30,y40,date"
        expected = [f"SELECT {cols} FROM JGB_table ORDER BY id DESC LIMIT 1", False]
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
