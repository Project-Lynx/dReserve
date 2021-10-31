import unittest
from typing import Union
from unittest import TestCase, mock

from app.models.federal_reserve.scenario import (Context, Dates_Strategy,
                                                 No_Dates_Strategy, a_date,
                                                 multi_date)

to_dict_patch = 'app.models.federal_reserve.database.Fed_Model.to_dict'
query_base = "SELECT date, statement FROM fomc_statements"


class Test_No_Dates_Strategy(TestCase):
    def setUp(self) -> None:
        super().__init__()
        self.test_class = No_Dates_Strategy

    def test_execute(self) -> None:
        with mock.patch(to_dict_patch) as patched:
            expected_pass = ['SELECT date, statement FROM fomc_statements', False]
            patched.return_value = None
            self.test_class().execute()
            patched.assert_called_with(expected_pass)


class Test_Dates_Strategy(TestCase):
    def setUp(self) -> None:
        super().__init__()
        self.test_class = Dates_Strategy

    def test_get_internals(self) -> None:
        scenarios: list[list[str]] = [
            ["2021-08-09"],
            ["current"],
            ["current,previous"],
            ["current,previous,2020-04-20,2020-03-20"],
        ]
        for scenario in scenarios:
            result = self.test_class(scenario).get_internals()
            self.assertEqual([scenario], result)

    def test_execute(self) -> None:
        scenarios: list[list[Union[list[Union[str, bool]], list]]] = [
            [[f"{query_base}  WHERE date=%s", True], ["2021-10-25"]],
            [[f"{query_base} WHERE date IN %s", True], ["2021-09-01", "2020-04-20"]],
            [[f"({query_base} ORDER BY id ASC LIMIT 1) UNION ({query_base} WHERE date=%s)",
              True], ["2020-01-12"]],
        ]
        with mock.patch(to_dict_patch) as patched:
            patched.return_value = None
            for scenario in scenarios:
                self.test_class(scenario[1]).execute(scenario[0])
                if scenario[0][1] is True:
                    patched.assert_called_with(scenario[0], scenario[1])
                else:
                    patched.assert_called_with(scenario[0])


class test_a_date(TestCase):
    def test_make_query(self) -> None:
        scenarios: dict = {
            'scenario 1': {
                'input': ["current"],
                'expected output': [f"{query_base} ORDER BY id ASC LIMIT 1", False],
            },
            'scenario 2': {
                'input': ["previous"],
                'expected output': [f"{query_base} ORDER BY id ASC LIMIT 1, 1", False],
            },
            'scenario 3': {
                'input': ["2020-04-20"],
                'expected output': [f"{query_base} WHERE date=%s", True],
            },
        }
        _scenarios_ = [scenarios[key] for key in scenarios]
        for _scenario_ in _scenarios_:
            dates = _scenario_['input']
            result = a_date(dates).make_query()
            expected = _scenario_['expected output']
            self.assertEqual(expected, result)


class test_multi_date(TestCase):
    def test_make_query(self) -> None:
        current_query = f"({query_base} ORDER BY id ASC LIMIT 1)"
        previous_query = f"({query_base} ORDER BY id ASC LIMIT 1, 1)"
        scenarios: dict = {
            'scenario 1': {
                'input': ["current", "previous"],
                'expected output': [f"{current_query} UNION {previous_query}", False],
            },
            'scenario 2': {
                'input': ["current", "2020-04-20"],
                'expected output': [f"{current_query} UNION ({query_base} WHERE date IN %s)", True],
            },
            'scenario 3': {
                'input': ["2021-09-25", "2021-09-24", "2021-09-23"],
                'expected output': [f"{query_base} WHERE date IN %s", True],
            },
        }
        _scenarios_ = [scenarios[key] for key in scenarios]
        for _scenario_ in _scenarios_:
            dates = _scenario_['input']
            expected = _scenario_['expected output']
            result = multi_date(dates).make_query()
            self.assertEqual(expected, result)


class test_Context(TestCase):
    def test_execute_strategy(self) -> None:
        with mock.patch('app.models.federal_reserve.scenario.a_date.execute') as patched:
            patched.return_value = None

            expected_query = [f"{query_base} ORDER BY id ASC LIMIT 1", False]
            Context(a_date(["current"])).execute_strategy()
            patched.assert_called_with(expected_query)

        with mock.patch('app.models.federal_reserve.scenario.multi_date.execute') as patched:
            patched.return_value = None
            dates = ["current", "previous", "2020-04-20"]
            expected_a = f"({query_base} ORDER BY id ASC LIMIT 1)"
            expected_b = f"({query_base} ORDER BY id ASC LIMIT 1, 1)"
            expected_c = f"({query_base} WHERE date IN %s)"
            expected_query = [f"{expected_a} UNION {expected_b} UNION {expected_c}", True]

            Context(multi_date(dates)).execute_strategy()
            patched.assert_called_with(expected_query)


if __name__ == "__main__":
    unittest.main()
