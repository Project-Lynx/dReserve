from app.models.federal_reserve.scenario import (Context, No_Dates_Strategy,
                                                 a_date, multi_date)


class FOMC_Statement_Repo:
    def __init__(self, dates: str = None) -> None:
        """Set up base case variables."""
        self.dates_str = dates

    def get_data(self) -> dict:
        """Run logic to execute the correct scenario strategy."""
        if self.dates_str is None:
            return No_Dates_Strategy().execute()

        dates_list = self.dates_str.split(",")
        if len(dates_list) > 1:
            return Context(multi_date(dates_list)).execute_strategy()
        else:
            return Context(a_date(dates_list)).execute_strategy()
