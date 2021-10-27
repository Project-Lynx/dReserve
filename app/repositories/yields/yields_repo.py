from typing import Union

from app.models.yields.scenario import Context, No_Dates, a_date, multi_dates


class Yields_Repo:
    def get_data(self, payload: list) -> Union[dict, None]:
        """Run logic to execute the correct scenario strategy."""
        product = payload[0]
        dates_str = payload[1]
        duration = payload[2]
        if dates_str is None:
            return No_Dates().execute(product, duration)

        dates_list = dates_str.split(",")
        if len(dates_list) > 1:
            return Context().execute_strategy(multi_dates(product, dates_list, duration))
        else:
            return Context().execute_strategy(a_date(product, dates_list, duration))
