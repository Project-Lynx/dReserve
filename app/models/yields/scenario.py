from typing import Union

from app.models.yields.product import Product


class No_Dates:
    """Strategy Interface for when no dates are passed."""
    def execute(self, product: str, duration: str = None) -> None:
        """Execute no dates strategy."""
        _Product_ = Product(product, duration=duration)
        product_data = _Product_.export_info()
        table = product_data[0]
        columns = product_data[1]
        strategy = product_data[2]

        if duration:
            query = [f"SELECT date,{duration} FROM {table}", False]
            _Product_.rate_to_dict(query)
        else:
            query = [f"SELECT {columns} FROM {table}", False]
            strategy().to_dict(query)


class Dates_Strategy(Product):
    """Strategy Interface for when dates are passed."""
    def __init__(self, product: str, dates: list, duration: str = None) -> None:
        self.dates = dates
        self.duration = duration
        self.current_query_end = "ORDER BY id DESC LIMIT 1"
        self.previous_query_end = "ORDER BY id DESC LIMIT 1, 1"
        if duration:
            super().__init__(product, data=dates, duration=duration)
            self.query_base = f"SELECT date,{duration} FROM {self.table} "
        else:
            super().__init__(product, data=dates)
            self.query_base = f"SELECT {self.columns} FROM {self.table} "

    def get_internals(self) -> list:
        """Export internal variables."""
        return [self.product, self.dates, self.duration]

    def execute(self, query: list) -> dict:
        """Execute Strategy."""
        if self.duration:
            return self.rate_to_dict(query)
        else:
            return self.product_strategy(self.dates).to_dict(query)


class a_date(Dates_Strategy):
    """Strategy for when a given date."""
    def __init__(self, product: str, dates: list, duration: str = None) -> None:
        if duration:
            super().__init__(product, dates=dates, duration=duration)
        else:
            super().__init__(product, dates)

    def make_query(self) -> list[Union[str, bool]]:
        """Logic to create query."""
        if "current" in self.dates:
            return [self.query_base + self.current_query_end, False]
        elif "previous" in self.dates:
            return [self.query_base + self.previous_query_end, False]
        else:
            return [self.query_base + "WHERE date=%s", True]


class multi_dates(Dates_Strategy):
    """Strategy for when multiple dates given."""
    def __init__(self, product: str, dates: list, duration: str = None) -> None:
        if duration:
            super().__init__(product, dates, duration)
        else:
            super().__init__(product, dates)

    def make_query(self) -> list[object]:
        """Logic to create query."""
        if "current" in self.dates and "previous" in self.dates and len(self.dates) == 2:
            return [f'({self.query_base + self.current_query_end})' + " UNION " +
                    f'({self.query_base + self.previous_query_end})', False]
        elif "current" in self.dates and "previous" in self.dates and len(self.dates) > 2:
            return [f'({self.query_base + self.current_query_end})' + " UNION " +
                    f'({self.query_base + self.previous_query_end})' + " UNION " +
                    f'({self.query_base + "WHERE date IN %s"})', True]
        elif "current" in self.dates:
            return [f'({self.query_base + self.current_query_end})' + " UNION " +
                    f'({self.query_base + "WHERE date IN %s"})', True]
        elif "previous" in self.dates:
            return [f'({self.query_base + self.previous_query_end})' + " UNION " +
                    f'({self.query_base + "WHERE date IN %s"})', True]
        else:
            return [self.query_base + "WHERE date IN %s", True]


class Context:
    """Strategy Handler for yields endpoint."""
    def execute_strategy(self, strategy: Dates_Strategy) -> dict:
        """Execute strategy for a specific scenario."""
        internals = strategy.get_internals()
        product = internals[0]
        dates = internals[1]
        duration = internals[2]

        if type(strategy) == a_date:
            return strategy.execute(a_date(product, dates, duration).make_query())
        else:
            return strategy.execute(multi_dates(product, dates, duration).make_query())
