import unittest
from typing import Union
from unittest import TestCase, mock

from app.models.yields.scenario import a_date, multi_dates
from app.repositories.yields.yields_repo import Yields_Repo


class Test_Yields_Repo(TestCase):
    def test_get_data(self) -> None:
        scenarios: list[list[Union[str, None]]] = [
            ["JGB", None, None],
            ["UST", "current,previous,2021-10-08,2021-08-31", "y10"],
            ["UKGB", "2021-08-31", "y30"],
        ]
        for scenario in scenarios:
            if "JGB" in scenario:
                with mock.patch('app.models.yields.scenario.No_Dates.execute') as patched:
                    Yields_Repo().get_data(scenario)
                    patched.assert_called_with("JGB", None)
            else:
                with mock.patch('app.models.yields.scenario.Context.execute_strategy') as patched:
                    Yields_Repo().get_data(scenario)
                    if "UST" in scenario:
                        dates_list = ["current", "previous", "2021-10-08", "2021-08-31"]
                        expected = multi_dates("UST", dates_list, "y10").__str__().split(" ")[0][1:]
                        actual = str(patched.call_args).split(" ")[0][6:]
                        self.assertEqual(expected, actual)
                    else:
                        expected = a_date("UKGB", "2021-08-31", "y30").__str__().split(" ")[0][1:]
                        actual = str(patched.call_args).split(" ")[0][6:]
                        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
