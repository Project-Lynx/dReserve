import pymysql

from app.config import RDS_HOST, RDS_PORT, RDS_PWORD, RDS_USER


class Meta:
    def __init__(self):
        self.host = RDS_HOST
        self.port = RDS_PORT
        self.user = RDS_USER
        self.pword = RDS_PWORD
        self.db = 'events'

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

    def create_table(self):
        self.__connect__()
        query = """CREATE TABLE IF NOT EXISTS event_table
                (name varchar(255), region varchar(255), time varchar(255),
                actual varchar(255), expectation varchar(255))
                """
        self.cur.execute(query)
        self.connect.commit()
        self.__disconnect__()

    def table_nuke(self):
        self.__connect__()
        query = "DROP TABLE event_table"
        self.cur.execute(query)
        self.connect.commit()
        self.__disconnect__()

    def fetch(self, sql_query: str) -> tuple:
        self.__connect__()
        self.cur.execute(sql_query)
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

    def to_dict(self, region: list) -> dict:
        self.__connect__()
        hashmap: dict = {}

        regions = tuple(i for i in region)
        query_start = "SELECT * FROM event_table WHERE region IN ("
        query = query_start + ("%s," * len(regions))[:-1] + ")"
        self.cur.execute(query, regions)
        results = self.cur.fetchall()

        for idx in enumerate(results):
            key = idx[0] + 1
            hashmap[key] = [idx[1][0], idx[1][1], idx[1][2], idx[1][3], idx[1][4]]

        return hashmap
