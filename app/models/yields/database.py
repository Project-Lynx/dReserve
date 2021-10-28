from app.models.database_meta import DB_Meta


class Yields_DB(DB_Meta):
    """Model for interacting with yields database."""

    def __init__(self) -> None:
        """Set up database variables."""
        super().__init__('yields')

    def fetch(self, query: list, dates: list = []) -> tuple:
        """Method to fetch data for a given query and/or dates from database"""
        self.__connect__()
        if True in query:
            if len(dates) > 1:
                self.cur.execute(query[0], (tuple(i for i in dates), ))
            else:
                self.cur.execute(query[0], (dates[0], ))
        else:
            self.cur.execute(query[0])

        result = self.cur.fetchall()
        print(result)
        self.__disconnect__()
        return result
