from typing import Dict, Optional, Union

import pymysql

from app.config import RDS_HOST, RDS_PORT, RDS_PWORD, RDS_USER


class Meta:
    def __init__(self):
        self.host = RDS_HOST
        self.port = RDS_PORT
        self.user = RDS_USER
        self.pword = RDS_PWORD
        self.db = 'yields'

    def __connect__(self):
        self.connect = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.pword,
            database=self.db,
        )
        self.cur = self.connect.cursor()

    def __disconnect__(self):
        self.connect.close()

    def fetch(self, sql_query: str) -> tuple:
        self.__connect__()
        self.cur.execute(sql_query)
        result = self.cur.fetchall()
        self.__disconnect__()

        return result

    def table_nuke(self, table: str):
        self.__connect__()
        query = f"DROP TABLE {table}"
        self.cur.execute(query)
        self.connect.commit()
        self.__disconnect__()

    def execute(self, sql_query: str):
        self.__connect__()
        self.cur.execute(sql_query)
        self.connect.commit()
        self.__disconnect__()

    def executemany(self, sql_query: str, data: list):
        self.__connect__()
        self.cur.executemany(sql_query, data)
        self.connect.commit()
        self.__disconnect__()

    def create_table(self, product: str):
        self.__connect__()

        if product == 'UST':
            query = """CREATE TABLE IF NOT EXISTS usT_table
                       (date varchar(255) PRIMARY KEY,
                       m1 varchar(255), m2 varchar(255), m3 varchar(255),
                       m6 varchar(255), y1 varchar(255), y2 varchar(255),
                       y3 varchar(255), y5 varchar(255), y7 varchar(255),
                       y10 varchar(255), y20 varchar(255), y30 varchar(255))
                    """
        elif product == 'JGB':
            query = """CREATE TABLE IF NOT EXISTS JGB_table
                       (date varchar(255) PRIMARY KEY,
                       y1 varchar(255), y2 varchar(255), y3 varchar(255),
                       y4 varchar(255), y5 varchar(255), y6 varchar(255),
                       y7 varchar(255), y8 varchar(255), y9 varchar(255),
                       y10 varchar(255), y15 varchar(255), y20 varchar(255),
                       y25 varchar(255), y30 varchar(255), y40 varchar(255))
                    """
        elif product == 'UKGB':
            query = """CREATE TABLE IF NOT EXISTS UKGB_table
                       (date varchar(255) PRIMARY KEY,
                       m1 varchar(255), m3 varchar(255), m6 varchar(255),
                       y1 varchar(255), y2 varchar(255), y3 varchar(255),
                       y5 varchar(255), y7 varchar(255), y10 varchar(255),
                       y15 varchar(255), y20 varchar(255), y25 varchar(255),
                       y30 varchar(255), y40 varchar(255))
                    """

        self.cur.execute(query)
        self.connect.commit()
        self.__disconnect__()

    def to_dict(self, table: str, keys: Optional[Union[str, list]] = None) -> Dict:
        self.__connect__()

        hashmap: dict = {}
        query = f"SELECT * FROM {table}"

        if keys is not None:
            if isinstance(keys, str):
                query = query + f" WHERE date='{keys}'"
            elif isinstance(keys, list):
                keys = str(tuple(i for i in keys))
                query = query + f" WHERE date IN {keys}"

        self.cur.execute(query)
        results = self.cur.fetchall()

        if table == 'usT_table':
            for idx in enumerate(results):
                key = idx[1][0]
                hashmap[key] = {
                   '1 month': idx[1][1], '2 month': idx[1][2], '3 month': idx[1][3],
                   '6 month': idx[1][4], '1 year': idx[1][5], '2 Year': idx[1][6],
                   '3 year': idx[1][7], '5 year': idx[1][8], '7 year': idx[1][9],
                   '10 year': idx[1][10], '20 year': idx[1][11], '30 year': idx[1][12],
                }
        elif table == 'JGB_table':
            for idx in enumerate(results):
                key = idx[1][0]
                hashmap[key] = {
                    '1 year': idx[1][1], '2 year': idx[1][2], '3 year': idx[1][3],
                    '4 year': idx[1][4], '5 year': idx[1][5], '6 year': idx[1][6],
                    '7 year': idx[1][7], '8 year': idx[1][8], '9 year': idx[1][9],
                    '10 year': idx[1][10], '15 year': idx[1][11], '20 year': idx[1][12],
                    '25 year': idx[1][13], '30 year': idx[1][14], '40 year': idx[1][15],
                }
        elif table == 'UKGB_table':
            for idx in enumerate(results):
                key = idx[1][0]
                hashmap[key] = {
                    'month 1': idx[1][1], 'month 3': idx[1][2], 'month 6': idx[1][3],
                    'year 1': idx[1][4], 'year 2': idx[1][5], 'year 3': idx[1][6],
                    'year 5': idx[1][7], 'year 7': idx[1][8], 'year 10': idx[1][9],
                    'year 15': idx[1][10], 'year 20': idx[1][11], 'year 25': idx[1][12],
                    'year 30': idx[1][13], 'year 40': idx[1][14],
                }

        return hashmap
