import pymysql

from app.config import RDS_HOST, RDS_PORT, RDS_PWORD, RDS_USER


class DB_Meta():

    """Model for interacting with database"""
    def __init__(self, database: str) -> None:
        """Set up database variables."""
        self.host = RDS_HOST
        self.port = RDS_PORT
        self.user = RDS_USER
        self.pword = RDS_PWORD
        self.db = database

    def __connect__(self) -> None:
        """Connect to database."""
        self.connect = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.pword,
            database=self.db,
        )
        self.cur = self.connect.cursor()

    def __disconnect__(self) -> None:
        """Disconnect from database."""
        self.connect.close()

    def table_nuke(self, table: str) -> None:
        """Delete entire table from database."""
        self.__connect__()
        query = f"DROP TABLE {table}"
        self.cur.execute(query)
        self.connect.commit()
        self.__disconnect__()

    def execute(self, query: str) -> None:
        """Execute sql query on database."""
        self.__connect__()
        self.cur.execute(query)
        self.connect.commit()
        self.__disconnect__()

    def executemany(self, query: str, data: list) -> None:
        """Execute sql query with params on database."""
        self.__connect__()
        self.cur.executemany(query, data)
        self.connect.commit()
        self.__disconnect__()

    def create_table(self, query: str) -> None:
        """Create table for database."""
        self.__connect__()
        self.cur.execute(query)
        self.connect.commit()
        self.__disconnect__()
