from typing import Union

from app.models.federal_reserve.database import DB_Model


class Base_Case:
    """Base Case Scenario"""
    def __init__(self) -> None:
        self.query_base = 'SELECT date, statement FROM fomc_statements'
        self.db_model = DB_Model()


class No_Dates_Strategy(Base_Case):
    def __init__(self) -> None:
        super().__init__()

    def execute(self) -> dict:
        query = [self.query_base, False]
        return self.db_model.to_dict(query)


class Dates_Strategy(Base_Case):
    def __init__(self, dates: list) -> None:
        super().__init__()
        self.dates = dates
        self.current_query = f'{self.query_base} ORDER BY id ASC LIMIT 1'
        self.previous_query = f'{self.query_base} ORDER BY id ASC LIMIT 1, 1'

    def get_internals(self) -> list:
        return [self.dates]

    def execute(self, query: list[Union[str, bool]]) -> dict:
        if query[1] is True:
            return self.db_model.to_dict(query, self.dates)
        else:
            return self.db_model.to_dict(query)


class a_date(Dates_Strategy):
    def __init__(self, dates: list) -> None:
        super().__init__(dates)

    def make_query(self) -> list[Union[str, bool]]:
        if "current" in self.dates:
            return [self.current_query, False]

        elif "previous" in self.dates:
            return [self.previous_query, False]

        else:
            return [f"{self.query_base} WHERE date=%s", True]


class multi_date(Dates_Strategy):
    def __init__(self, dates: list) -> None:
        super().__init__(dates)

    def make_query(self) -> list[Union[str, bool]]:
        if "current" in self.dates and "previous" in self.dates and len(self.dates) == 2:
            return [f'({self.current_query}) UNION ({self.previous_query})', False]

        elif "current" in self.dates and "previous" in self.dates and len(self.dates) > 2:
            return [f'({self.current_query}) UNION ({self.previous_query}) UNION ' +
                    f'({self.query_base} WHERE date IN %s)', True]

        elif "current" in self.dates:
            return [f'({self.current_query}) UNION ({self.query_base} WHERE date IN %s)', True]

        elif "previous" in self.dates:
            return [f'({self.previous_query}) UNION ({self.query_base} WHERE date IN %s)', True]

        else:
            return [f'{self.query_base} WHERE date IN %s', True]


class Context:
    """Strategy Handler for FOMC Statements"""
    def __init__(self, strategy: Dates_Strategy) -> None:
        self.strategy = strategy
        self.dates = strategy.get_internals()[0]

    def execute_strategy(self) -> dict:
        if type(self.strategy) == a_date:
            return self.strategy.execute(a_date(self.dates).make_query())
        else:
            return self.strategy.execute(multi_date(self.dates).make_query())
