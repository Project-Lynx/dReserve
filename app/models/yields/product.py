from typing import Type, Union

from app.models.yields.database import DB_Model
from app.util import tables


class Product():
    """Basic representation of a product"""
    def __init__(self, product: str, data: list = [], duration: str = None) -> None:
        self.output: dict = {}
        self.table = tables.get_table(product)
        self.product = product
        self.duration = duration
        self.data = data

        self.product_strategy: Type[Union[UST, JGB, UKGB]]
        if product == "UST":
            self.product_strategy = UST
            self.columns = "m1,m2,m3,m6,y1,y2,y3,y5,y7,y10,y20,y30,date"
        elif product == "JGB":
            self.product_strategy = JGB
            self.columns = "m1,m3,m6,y1,y2,y3,y5,y7,y10,y15,y20,y30,y40,date"
        elif product == "UKGB":
            self.product_strategy = UKGB
            self.columns = "m1,m3,m6,y1,y2,y3,y5,y7,y10,y15,y20,y25,y30,y40,date"
        else:
            raise Exception(ValueError, f"Invalid Product: {self.product} !")

    def export_info(self) -> list:
        """Export internal variables"""
        return [self.table, self.columns, self.product_strategy]

    def fetch_data(self, query: list) -> tuple:
        """Get data from DB"""
        return DB_Model().fetch(query, self.data)

    def rate_to_dict(self, query: list) -> dict:
        """Convert tuple to hashmap"""
        data = self.fetch_data(query)
        for idx in enumerate(data):
            key = str(idx[1][0])
            self.output[key] = idx[1][1]
        return self.output


class UST(Product):
    """UST's Strategy"""
    def __init__(self, data: list = []) -> None:
        super().__init__("UST", data)

    def to_dict(self, query: list) -> dict:
        """Convert data to hashmap specific to UST's."""
        for idx in enumerate(self.fetch_data(query)):
            key = str(idx[1][12])
            self.output[key] = {
               '1 month': idx[1][0], '2 month': idx[1][1], '3 month': idx[1][2],
               '6 month': idx[1][3], '1 year': idx[1][4], '2 Year': idx[1][5],
               '3 year': idx[1][6], '5 year': idx[1][7], '7 year': idx[1][8],
               '10 year': idx[1][9], '20 year': idx[1][10], '30 year': idx[1][11],
            }
        return self.output

    def create_table(self) -> None:
        """Create table specific to UST's"""
        query = """CREATE TABLE IF NOT EXISTS usT_table
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                   m1 varchar(10), m2 varchar(10), m3 varchar(10),
                   m6 varchar(10), y1 varchar(10), y2 varchar(10),
                   y3 varchar(10), y5 varchar(10), y7 varchar(10),
                   y10 varchar(10), y20 varchar(10), y30 varchar(10),
                   date DATE, year YEAR)
                """
        DB_Model().create_table(query)


class JGB(Product):
    """JGB's Strategy"""
    def __init__(self, data: list = []) -> None:
        super().__init__("JGB", data)

    def to_dict(self, query: list) -> dict:
        """Convert data to hashmap specific to JGB's."""
        for idx in enumerate(self.fetch_data(query)):
            key = str(idx[1][13])
            self.output[key] = {
               '1 month': idx[1][0], '3 month': idx[1][1], '6 month': idx[1][2],
               '1 year': idx[1][3], '2 year': idx[1][4], '3 year': idx[1][7],
               '5 year': idx[1][6], '7 year': idx[1][7], '10 year': idx[1][8],
               '15 year': idx[1][9], '20 year': idx[1][10], '30 year': idx[1][11],
               '40 year': idx[1][12],
            }
        return self.output

    def create_table(self) -> None:
        """Create table specific to JGB's."""
        query = """CREATE TABLE IF NOT EXISTS JGB_table
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                   m1 varchar(10), m3 varchar(10), m6 varchar(10),
                   y1 varchar(10), y2 varchar(10), y3 varchar(10),
                   y5 varchar(10), y7 varchar(10), y10 varchar(10),
                   y15 varchar(10), y20 varchar(10), y30 varchar(10),
                   y40 varchar(10), date DATE, year YEAR)
                """
        DB_Model().create_table(query)


class UKGB(Product):
    """UKGB's Strategy"""
    def __init__(self, data: list = []) -> None:
        super().__init__("UKGB", data)

    def to_dict(self, query: list) -> dict:
        """Convert data to hashmap specific to UKGB's."""
        for idx in enumerate(self.fetch_data(query)):
            key = str(idx[1][14])
            self.output[key] = {
               '1 month': idx[1][0], '3 month': idx[1][1], '6 month': idx[1][2],
               '1 year': idx[1][3], '2 year': idx[1][4], '3 year': idx[1][5],
               '5 year': idx[1][6], '7 year': idx[1][7], '10 year': idx[1][8],
               '15 year': idx[1][9], '20 year': idx[1][10], '25 year': idx[1][11],
               '30 year': idx[1][12], '40 year': idx[1][13],
            }
        return self.output

    def create_table(self) -> None:
        """Create table specific to UKGB's."""
        query = """create table if not exists ukgb_table
                   (id int not null auto_increment primary key,
                   m1 varchar(10), m3 varchar(10), m6 varchar(10),
                   y1 varchar(10), y2 varchar(10), y3 varchar(10),
                   y5 varchar(10), y7 varchar(10), y10 varchar(10),
                   y15 varchar(10), y20 varchar(10), y25 varchar(10),
                   y30 varchar(10), y40 varchar(10), date date, year year)
                """
        DB_Model().create_table(query)
