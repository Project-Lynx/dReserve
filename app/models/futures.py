from app.config import RDS_HOST, RDS_PORT, RDS_USER, RDS_PWORD

import pymysql

class Meta:
    def __init__(self):
        self.host = RDS_HOST
        self.port = RDS_PORT
        self.user = RDS_USER
        self.pword = RDS_PWORD
        self.db = 'futures'
    
    def __connect__(self):
        self.connect = pymysql.connect(
            host = self.host,
            port = self.port,
            user = self.user,
            password = self.pword,
            database = self.db,
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


    def to_dict(self, PID=None):
        if PID is None:
            query = "SELECT * FROM testing"
        else:
            if isinstance(PID, list):
                query = f"""
                    SELECT * FROM testing WHERE id IN %s""" % str(tuple(int(i) for i in PID))
            else:
                query = f"SELECT * FROM testing WHERE id={PID}"
        
        hashmap = {}
        self.__connect__()
        self.cur.execute(query)
        results = self.cur.fetchall()

        for idx in enumerate(results):
            key = idx[1][10]
            sub_key = str(idx[1][11])[:8]
            if key not in hashmap:
                hashmap[key] = {}
            else:
                if sub_key not in hashmap[key]:
                    hashmap[key][sub_key] = []
                    hashmap[key][sub_key].append({"pid": idx[1][0]})
                    hashmap[key][sub_key].append({"price": idx[1][1]}) 
                    hashmap[key][sub_key].append({"change": idx[1][2]})
                    hashmap[key][sub_key].append({"open": idx[1][3]})
                    hashmap[key][sub_key].append({"close": idx[1][4]})
                    hashmap[key][sub_key].append({"high": idx[1][5]})
                    hashmap[key][sub_key].append({"low": idx[1][6]})
                    hashmap[key][sub_key].append({"highLimit": idx[1][7]})
                    hashmap[key][sub_key].append({"lowLimit": idx[1][8]})
                    hashmap[key][sub_key].append({"volume": idx[1][9]})
                    hashmap[key][sub_key].append({"pChange": idx[1][12]})
                    hashmap[key][sub_key].append({"expiration": idx[1][13]})
                    hashmap[key][sub_key].append({"name": idx[1][14]})
                    hashmap[key][sub_key].append({"url": idx[1][15]})
        self.__disconnect__()

        return hashmap

    def fetch(self, sql_query):
        self.__connect__()
        self.cur.execute(sql_query)
        result = self.cur.fetchall()
        self.__disconnect__()
        
        return result
    
    def execute(self, sql_query):
        self.__connect__()
        self.cur.execute(sql_query)
        self.connect.commit()
        self.__disconnect__()

    def executemany(self, sql_query, data):
        self.__connect__()
        self.cur.executemany(sql_query, data)
        self.connect.commit()
        self.__disconnect__()
