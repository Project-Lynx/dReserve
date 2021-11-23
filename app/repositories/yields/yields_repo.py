from typing import Union

from app.models.yields.scenario import Context, No_Dates, a_date, multi_dates


class Yields_Repo:
    def __init__(self, payload: dict) -> None:
        self.product = payload['product']
        self.dates_str = payload['dates']
        self.duration = payload['duration']

    def get_data(self) -> Union[dict, None]:
        """Run logic to execute the correct scenario strategy."""
        if self.dates_str is None:
            return No_Dates().execute(self.product, self.duration)

        dates_list = self.dates_str.split(",")
        if len(dates_list) > 1:
            return Context().execute_strategy(multi_dates(self.product, dates_list, self.duration))
        else:
            return Context().execute_strategy(a_date(self.product, dates_list, self.duration))
