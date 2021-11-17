from typing import Union

from app.util.convert_product import get_class


class No_Dates:
    """Strategy Interface for when no dates are passed."""
    def execute(self, product: str, duration: str = "") -> None:
        """Execute no dates strategy."""
        product_class = get_class(product)
        product_data = product_class().export_info()
        table = product_data['table']
        columns = product_data['columns']

        if duration:
            query = [f"SELECT date,{duration} FROM {table}", False]
            product_class().rate_to_dict(query)
        else:
            query = [f"SELECT {columns} FROM {table}", False]
            product_class().to_dict(query)


class Dates_Strategy:
    """Strategy Interface for when dates are passed."""
    def __init__(self, product: str, dates: list, duration: str = "") -> None:
        self.dates = dates
        self.duration = duration
        self.product = product
        self.current_query_end = "ORDER BY id DESC LIMIT 1"
        self.previous_query_end = "ORDER BY id DESC LIMIT 1, 1"
        self.product_class = get_class(product)

        internals = self.product_class().export_info()

        if duration:
            self.query_base = f"SELECT date,{duration} FROM {internals['table']} "
        else:
            self.query_base = f"SELECT {internals['columns']} FROM {internals['table']} "

    def get_internals(self) -> dict:
        """Export internal variables."""
        return {
            'product': self.product,
            'dates': self.dates,
            'duration': self.duration,
        }

    def execute(self, query: list) -> dict:
        """Execute Strategy."""
        if self.duration:
            return self.product_class().rate_to_dict(query)
        else:
            return self.product_class(self.dates).to_dict(query)


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

        if isinstance(strategy, a_date):
            return strategy.execute(a_date(
                internals['product'], internals['dates'], internals['duration'],
            ).make_query())

        else:
            return strategy.execute(multi_dates(
                internals['product'], internals['dates'], internals['duration'],
            ).make_query())
