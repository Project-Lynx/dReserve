import unittest
from unittest import TestCase, mock

from app.repositories.federal_reserve.fomc_statements import \
    FOMC_Statement_Repo

context_patched = 'app.models.federal_reserve.scenario.Context.execute_strategy'
no_dates_patched = 'app.models.federal_reserve.scenario.No_Dates_Strategy.execute'


class Test_FOMC_Statement_Repo(TestCase):
    def test_get_data(self) -> None:
        scenarios = [
            "current", "current,previous",
            "current,2020-04-20,2021-10-25",
        ]
        with mock.patch(context_patched) as patched:
            for scenario in scenarios:
                FOMC_Statement_Repo(scenario).get_data()
                patched.assert_called()

        with mock.patch(no_dates_patched) as patched:
            patched.return_value = None
            FOMC_Statement_Repo().get_data()
            patched.assert_called()


if __name__ in '__main__':
    unittest.main()
