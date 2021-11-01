from typing import Optional, Union

from app.models.database_meta import DB_Meta


class Fed_Model(DB_Meta):
    def __init__(self) -> None:
        """Set up db variables."""
        super().__init__('fed')
        self.query = """CREATE TABLE IF NOT EXISTS fomc_statements
                     (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                     date DATE, year YEAR, statement TEXT)
                     """

    def fetch(self, query: str, data: Optional[tuple] = None) -> tuple:
        """Fetch from database."""
        self.__connect__()
        if data:
            self.cur.execute(query, data)
        else:
            self.cur.execute(query)
        result = self.cur.fetchall()
        self.__disconnect__()
        return result

    def to_dict(self, query: list, dates: Union[str, list] = None) -> dict:
        """Render hashmap of date as key and statement as value."""
        self.__connect__()
        hashmap: dict = {}
        if dates:
            self.cur.execute(query[0], (dates, ))
        else:
            self.cur.execute(query[0])
        results = self.cur.fetchall()

        for idx in enumerate(results):
            key = str(idx[1][0])
            hashmap[key] = idx[1][1]
        return hashmap
