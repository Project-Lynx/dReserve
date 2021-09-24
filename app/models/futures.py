from typing import Optional, Union

import pymysql

from app.config import RDS_HOST, RDS_PORT, RDS_PWORD, RDS_USER


class Meta:
    def __init__(self):
        self.host = RDS_HOST
        self.port = RDS_PORT
        self.user = RDS_USER
        self.pword = RDS_PWORD
        self.db = 'futures'

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

    def table_nuke(self):
        self.__connect__()
        query = "DROP TABLE testing"
        self.cur.execute(query)
        self.connect.commit()
        self.__disconnect__()

    def fetch(self, query: str, PID: tuple) -> tuple:
        self.__connect__()
        self.cur.execute(query, PID)
        result = self.cur.fetchall()
        self.__disconnect__()

        return result

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

    def to_dict(self, PID: Optional[Union[str, list]]) -> dict:
        self.__connect__()
        hashmap: dict = {}

        if isinstance(PID, list):
            query_start = "SELECT * FROM testing WHERE id IN ("
            query = query_start + ("%s," * len(PID))[:-1] + ")"
            self.cur.execute(query, tuple(int(i) for i in PID))
        elif isinstance(PID, str):
            query = "SELECT * FROM testing WHERE id=%s"
            self.cur.execute(query, (PID, ))

        results = self.cur.fetchall()

        for idx in enumerate(results):
            key = idx[1][10]
            sub_key = str(idx[1][11])[:8]
            if key not in hashmap:
                hashmap[key] = {}
            else:
                if sub_key not in hashmap[key]:
                    hashmap[key][sub_key] = {
                        "pid": idx[1][0], "price": idx[1][1],
                        "change": idx[1][2], "open": idx[1][3],
                        "close": idx[1][4], "high": idx[1][5],
                        "low": idx[1][6], "highLimit": idx[1][7],
                        "lowLimit": idx[1][8], "volume": idx[1][9],
                        "pChange": idx[1][12], "expiration": idx[1][13],
                        "name": idx[1][14], "url": idx[1][15],
                    }
        self.__disconnect__()

        return hashmap
