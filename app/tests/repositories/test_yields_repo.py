import unittest
from unittest import TestCase, mock

from app.models.yields.scenario import a_date, multi_dates
from app.repositories.yields.yields_repo import Yields_Repo


class Test_Yields_Repo(TestCase):
    def test_get_data(self) -> None:
        scenario = {"product": "Australia", "dates": None, "duration": None}
        with mock.patch('app.models.yields.scenario.No_Dates.execute') as patched:
            Yields_Repo(scenario).get_data()
            patched.assert_called_with("Australia", None)

        scenario = {"product": "United states", "dates": "current,previous,2021-10-08,2021-08-31", "duration": "y10"}
        with mock.patch('app.models.yields.scenario.Context.execute_strategy') as patched:
            Yields_Repo(scenario).get_data()
            dates_list = ["current", "previous", "2021-10-08", "2021-08-31"]
            expected = multi_dates("United States", dates_list, "y10").__str__().split(" ")[0][1:]
            actual = str(patched.call_args).split(" ")[0][6:]
            self.assertEqual(expected, actual)

        scenario = {"product": "China", "dates": "2021-11-19", "duration": "y30"}
        with mock.patch('app.models.yields.scenario.Context.execute_strategy') as patched:
            Yields_Repo(scenario).get_data()
            expected = a_date("China", ["2021-08-31"], "y30").__str__().split(" ")[0][1:]
            actual = str(patched.call_args).split(" ")[0][6:]
            self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
