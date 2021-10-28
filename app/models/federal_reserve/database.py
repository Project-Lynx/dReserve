from typing import Optional, Union

import pymysql

from app.config import RDS_HOST, RDS_PORT, RDS_PWORD, RDS_USER


class DB_Model:
    """Model for fomc statements table in database"""
    def __init__(self) -> None:
        self.host = RDS_HOST
        self.port = RDS_PORT
        self.user = RDS_USER
        self.pword = RDS_PWORD
        self.db = 'fed'

    def __connect__(self) -> None:
        """Helper method to connect to database"""
        self.connect = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.pword,
            database=self.db,
        )
        self.cur = self.connect.cursor()

    def __disconnect__(self):
        """Helper method to disconnect from table"""
        self.connect.close()

    def create_table(self):
        """Method to create table"""
        self.__connect__()
        query = """CREATE TABLE IF NOT EXISTS fomc_statements
                (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                date DATE, year YEAR, statement TEXT)
                """
        self.cur.execute(query)
        self.connect.commit()
        self.__disconnect__()

    def fetch(self, query: str, data: Optional[tuple] = None) -> tuple:
        """Method to fetch from table"""
        self.__connect__()
        if data:
            self.cur.execute(query, data)
        else:
            self.cur.execute(query)
        result = self.cur.fetchall()
        self.__disconnect__()
        return result

    def table_nuke(self) -> None:
        """Method to delete entire table"""
        self.__connect__()
        query = "DROP TABLE fomc_statements"
        self.cur.execute(query)
        self.connect.commit()
        self.__disconnect__()

    def execute(self, query: str) -> None:
        """Method to execute a query"""
        self.__connect__()
        self.cur.execute(query)
        self.connect.commit()
        self.__disconnect__()

    def executemany(self, query: str, data: list) -> None:
        """Method to execute query with multiple params"""
        self.__connect__()
        self.cur.executemany(query, data)
        self.connect.commit()
        self.__disconnect__()

    def to_dict(self, query: list, dates: Union[str, list] = None) -> dict:
        """Method returns hashmap of date
           as key and statement as value."""
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
