from typing import Union

from app.models.federal_reserve.database import Fed_Model


class Base_Case:
    def __init__(self) -> None:
        """Set up base case variables."""
        self.query_base = 'SELECT date, statement FROM fomc_statements'
        self.query_current = f'{self.query_base} ORDER BY id DESC LIMIT 1'
        self.query_previous = f'{self.query_base} ORDER BY id DESC LIMIT 1, 1'
        self.db_model = Fed_Model()


class No_Dates_Strategy(Base_Case):
    def __init__(self) -> None:
        """Set up base case variables."""
        super().__init__()

    def execute(self) -> dict:
        """Execute strategy."""
        query = [self.query_base, False]
        return self.db_model.to_dict(query)


class Dates_Strategy(Base_Case):
    def __init__(self, dates: list) -> None:
        """Set up base case variables."""
        super().__init__()
        self.dates = dates

    def get_internals(self) -> list:
        """Export internal variables."""
        return [self.dates]

    def execute(self, query: list[Union[str, bool]]) -> dict:
        """Execute strategy."""
        if query[1] is True:
            return self.db_model.to_dict(query, self.dates)
        else:
            return self.db_model.to_dict(query)


class a_date(Dates_Strategy):
    def __init__(self, dates: list) -> None:
        """Set up base case variables."""
        super().__init__(dates)

    def make_query(self) -> list[Union[str, bool]]:
        """Create query for a date strategy."""
        if "current" in self.dates:
            return [self.query_current, False]
        elif "previous" in self.dates:
            return [self.query_previous, False]
        else:
            return [f"{self.query_base} WHERE date=%s", True]


class multi_date(Dates_Strategy):
    def __init__(self, dates: list) -> None:
        """Set up base case variables."""
        super().__init__(dates)

    def make_query(self) -> list[Union[str, bool]]:
        """Create query for multi date strategy."""
        if "current" in self.dates and "previous" in self.dates and len(self.dates) == 2:
            return [f'({self.query_current}) UNION ({self.query_previous})', False]

        elif "current" in self.dates and "previous" in self.dates and len(self.dates) > 2:
            return [f'({self.query_current}) UNION ({self.query_previous}) UNION ' +
                    f'({self.query_base} WHERE date IN %s)', True]

        elif "current" in self.dates:
            return [f'({self.query_current}) UNION ({self.query_base} WHERE date IN %s)', True]

        elif "previous" in self.dates:
            return [f'({self.query_previous}) UNION ({self.query_base} WHERE date IN %s)', True]

        else:
            return [f'{self.query_base} WHERE date IN %s', True]


class Context:
    def __init__(self, strategy: Dates_Strategy) -> None:
        """Set up base case variables."""
        self.strategy = strategy
        self.dates = strategy.get_internals()[0]

    def execute_strategy(self) -> dict:
        """Execute dates strategy."""
        if isinstance(self.strategy, a_date):
            return self.strategy.execute(a_date(self.dates).make_query())
        else:
            return self.strategy.execute(multi_date(self.dates).make_query())
