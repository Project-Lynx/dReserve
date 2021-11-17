from app.models.yields.database import Yields_DB
from app.util import tables


class Product():
    """Basic representation of a product"""
    def __init__(self, product: str, data: list = []) -> None:
        self.output: dict = {}
        self.table = tables.get_table(product)
        self.product = product
        self.data = data

    def export_info(self) -> dict:
        """Export internal variables"""
        return {
            'table': self.table,
        }

    def fetch_data(self, query: list) -> tuple:
        """Get data from DB"""
        return Yields_DB().fetch(query, self.data)

    def rate_to_dict(self, query: list) -> dict:
        """Convert tuple to hashmap"""
        data = self.fetch_data(query)
        for idx in enumerate(data):
            key = str(idx[1][0])
            self.output[key] = idx[1][1]
        return self.output


class Argentina(Product):
    """Argentina Government Bonds."""
    def __init__(self, data: list = []) -> None:
        super().__init__(product="ArgentinaGB", data=data)
        self.columns = "1y,4y,7y,date"

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(self.fetch_data(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '1 Year': idx[1][0], '4 Year': idx[1][1], '7 Year': idx[1][2],
            }
        return self.output

    def create_table(self) -> None:
        """Create table for Argentina Gov Bonds in DB."""
        query = """CREATE TABLE IF NOT EXISTS ArgentinaGB
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    1y varchar(7), 4y varchar(7), 7y varchar(7),
                    date DATE, year YEAR)
                """
        Yields_DB().create_table(query)


class Australia(Product):
    """Australia Government Bonds."""
    def __init__(self, data: list = []) -> None:
        super().__init__(product="AustraliaGB", data=data)
        self.columns = "1y,2y,3y,4y,5y,7y,8y,9y,10y,12y,15y,20y,30y,date"

    def to_dict(self, query: list = []) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(self.fetch_data(query)):
            key = str(idx[1][-2])
            self.output[key] = {
                '1 Year': idx[1][0], '2 Year': idx[1][1], '3 Year': idx[1][2],
                '4 Year': idx[1][3], '5 Year': idx[1][4], '6 Year': idx[1][5],
                '7 Year': idx[1][6], '8 Year': idx[1][7], '9 Year': idx[1][8],
                '10 Year': idx[1][9], '12 Year': idx[1][10], '15 Year': idx[1][11],
                '20 Year': idx[1][12], '30 Year': idx[1][13],
            }
        return self.output

    def create_table(self) -> None:
        """Create table for Australia Gov Bonds in DB."""
        query = """CREATE TABLE IF NOT EXISTS AustraliaGB
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    1y varchar(7), 2y varchar(7), 3y varchar(7),
                    4y varchar(7), 5y varchar(7), 6y varchar(7),
                    7y varchar(7), 8y varchar(7), 9y varchar(7),
                    10y varchar(7), 12y varchar(7), 15y varchar(7),
                    20y varchar(7), 30y varchar(7), date DATE, year YEAR)
                """
        Yields_DB().create_table(query)


class Austria(Product):
    """Austria Government Bonds."""
    def __init__(self, data: list = []) -> None:
        super().__init__(product="AustriaGB", data=data)
        self.columns = "1y,2y,3y,4y,5y,6y,7y,8y,9y,10y,15y,20y,25y,30y,40y,date"

    def to_dict(self, query: list = []) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(self.fetch_data(query)):
            key = str(idx[1][-2])
            self.output[key] = {
                '1 Year': idx[1][0], '2 Year': idx[1][1], '3 Year': idx[1][2],
                '4 Year': idx[1][3], '5 Year': idx[1][4], '6 Year': idx[1][5],
                '7 Year': idx[1][6], '8 Year': idx[1][7], '9 Year': idx[1][8],
                '10 Year': idx[1][9], '15 Year': idx[1][10], '20 Year': idx[1][11],
                '25 Year': idx[1][12], '30 Year': idx[1][13], '40 Year': idx[1][14],
            }
        return self.output

    def create_table(self) -> None:
        """Create table for Austria Gov Bonds in DB."""
        query = """CREATE TABLE IF NOT EXISTS AustriaGB
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    1y varchar(7), 2y varchar(7), 3y varchar(7),
                    4y varchar(7), 5y varchar(7), 6y varchar(7),
                    7y varchar(7), 8y varchar(7), 9y varchar(7),
                    10y varchar(7), 15y varchar(7), 20y varchar(7),
                    25y varchar(7), 30y varchar(7), 40y varchar(7),
                    date DATE, year YEAR)
                """
        Yields_DB().create_table(query)


class Bahrain(Product):
    """Bahrain Government Bonds."""
    def __init__(self, data: list = []) -> None:
        super().__init__(product="BahrainGB", data=data)
        self.columns = "3m,6m,9m,1y,2y,5y,date"

    def to_dict(self, query: list = []) -> dict:
        for idx in enumerate(self.fetch_data(query)):
            key = str(idx[1][-2])
            self.output[key] = {
                '3 Month': idx[1][0], '6 Month': idx[1][1], '9 Month': idx[1][2],
                '1 Year': idx[1][3], '2 Year': idx[1][4], '5 Year': idx[1][5],
            }
        return self.output

    def create_table(self) -> None:
        query = """CREATE TABLE IF NOT EXISTS AustriaGB
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    3m varchar(7), 6m varchar(7), 9m varchar(7),
                    1y varchar(7), 2y varchar(7), 5y varchar(7),
                    date DATE, year YEAR)
                """
        Yields_DB().create_table(query)


class Bangledesh(Product):
    def __init__(self, data: list = []) -> None:
        super().__init__(product="BahrainGB", data=data)
        self.columns = "3m,6m,1y,2y,5y,10y,15y,20y,date"

    def to_dict(self, query: list = []) -> dict:
        for idx in enumerate(self.fetch_data(query)):
            key = str(idx[1][-2])
            self.output[key] = {
                '3 Month': idx[1][0], '6 Month': idx[1][1], '1 Year': idx[1][2],
                '2 Year': idx[1][3], '5 Year': idx[1][4], '10 Year': idx[1][5],
                '15 Year': idx[1][6], '20 Year': idx[1][7],
            }
        return self.output

    def create_table(self) -> None:
        query = """CREATE TABLE IF NOT EXISTS AustriaGB
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    3m varchar(7), 6m varchar(7), 1y varchar(7),
                    2y varchar(7), 5y varchar(7), 10y varchar(7),
                    15y varchar(7), 20y varchar(7), date DATE,
                    year YEAR)
                """
        Yields_DB().create_table(query)


class Belgium(Product):
    """Belgium Government Bonds."""
    def __init__(self, data: list = []) -> None:
        super().__init__(product="BelgiumGB", data=data)
        self.columns = "1m,3m,6m,9m,1y,2y,3y,4y,5y,6y,8y,9y,10y,15y,20y,date"

    def to_dict(self, query: list = []) -> dict:
        for idx in enumerate(self.fetch_data(query)):
            key = str(idx[1][-2])
            self.output[key] = {
                '3 Month': idx[1][0], '6 Month': idx[1][1], '1 Year': idx[1][2],
                '2 Year': idx[1][3], '5 Year': idx[1][4], '10 Year': idx[1][5],
                '15 Year': idx[1][6], '20 Year': idx[1][7],
            }
        return self.output

    def create_table(self) -> None:
        query = """CREATE TABLE IF NOT EXISTS BelgiumGB
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    1m varchar(7), 3m varchar(7), 6m varchar(7),
                    9m varchar(7), 1y varchar(7), 2y varchar(7),
                    3y varchar(7), 4y varchar(7), 5y varchar(7),
                    6y varchar(7), 8y varchar(7), 9y varchar(7),
                    10y varchar(7), 15y varchar(7), 20y varchar(7),
                    date DATE, year YEAR)
                """
        Yields_DB().create_table(query)


class Botswana(Product):
    """Botswana Government Bonds."""
    def __init__(self, data: list = []) -> None:
        super().__init__(product="BotswanaGB", data=data)
        self.columns = "6m,3y,5y,20y,date"

    def to_dict(self, query: list = []) -> dict:
        for idx in enumerate(self.fetch_data(query)):
            key = str(idx[1][-2])
            self.output[key] = {
                '6 Month': idx[1][0], '3 Year': idx[1][1], '5 Year': idx[1][2],
                '20 Year': idx[1][3],
            }
        return self.output

    def create_table(self) -> None:
        query = """CREATE TABLE IF NOT EXISTS BotswanaGB
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    6m varchar(7), 3y varchar(7), 5y varchar(7),
                    20y varchar(7), date DATE, year YEAR)
                """
        Yields_DB().create_table(query)


class Brazil(Product):
    """Brazil Government Bonds."""
    def __init__(self, data: list = []) -> None:
        super().__init__(product="BrazilGB", data=data)
        self.columns = "3m,6m,9m,1y,2y,3y,5y,8y,10y,date"

    def to_dict(self, query: list = []) -> dict:
        for idx in enumerate(self.fetch_data(query)):
            key = str(idx[1][-2])
            self.output[key] = {
                '3 Month': idx[1][0], '6 Month': idx[1][1], '9 Month': idx[1][2],
                '1 Year': idx[1][3], '2 Year': idx[1][4], '3 Year': idx[1][5],
                '5 Year': idx[1][6], '8 Year': idx[1][7], '10 Year': idx[1][8],
            }
        return self.output

    def create_table(self) -> None:
        query = """CREATE TABLE IF NOT EXISTS BrazilGB
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    3m varchar(7), 6m varchar(7), 9m varchar(7),
                    1y varchar(7), 2y varchar(7), 3y varchar(7),
                    5y varchar(7), 8y varchar(7), 10y varchar(7),
                    date DATE, year YEAR)
                """
        Yields_DB().create_table(query)


class Bulgaria(Product):
    """Bulgaria Government Bonds."""
    def __init__(self, data: list = []) -> None:
        super().__init__(product="BulgariaGB", data=data)
        self.columns = "1m,1y,2y,3y,4y,5y,7y,10y,date"

    def to_dict(self, query: list = []) -> dict:
        for idx in enumerate(self.fetch_data(query)):
            key = str(idx[1][-2])
            self.output[key] = {
                '1 Month': idx[1][0], '1 Year': idx[1][1], '2 Year': idx[1][2],
                '3 Year': idx[1][3], '4 Year': idx[1][4], '5 Year': idx[1][5],
                '7 Year': idx[1][6], '10 Year': idx[1][7],
            }
        return self.output

    def create_table(self) -> None:
        query = """CREATE TABLE IF NOT EXISTS BulgariaGB
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    1m varchar(7), 1y varchar(7), 2y varchar(7),
                    3y varchar(7), 4y varchar(7), 5y varchar(7),
                    7y varchar(7), 10y varchar(7), date DATE,
                    year YEAR)
                """
        Yields_DB().create_table(query)


class Canada(Product):
    """Canadian Government Bonds."""
    def __init__(self, data: list = []) -> None:
        super().__init__(product="CanadaGB", data=data)
        self.columns = "1m,2m,3m,6m,1y,2y,3y,4y,5y,7y,10y,20y,30y,date"

    def to_dict(self, query: list = []) -> dict:
        for idx in enumerate(self.fetch_data(query)):
            key = str(idx[1][-2])
            self.output[key] = {
                '1 Month': idx[1][0], '2 Month': idx[1][1], '3 Month': idx[1][2],
                '6 Month': idx[1][3], '1 Year': idx[1][4], '2 Year': idx[1][5],
                '3 Year': idx[1][6], '4 Year': idx[1][7], '5 Year': idx[1][8],
                '7 Year': idx[1][9], '10 Year': idx[1][10], '20 Year': idx[1][11],
                '30 Year': idx[1][12],
            }
        return self.output

    def create_table(self) -> None:
        query = """CREATE TABLE IF NOT EXISTS CanadaGB
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    1m varchar(7), 2m varchar(7), 3m varchar(7),
                    6m varchar(7), 1y varchar(7), 2y varchar(7),
                    3y varchar(7), 4y varchar(7), 5y varchar(7),
                    7y varchar(7), 10y varchar(7), 20y varchar(7),
                    30y varchar(7), date DATE, year YEAR)
                """
        Yields_DB().create_table(query)


class Chile(Product):
    """Chilian Government Bonds."""
    def __init__(self, data: list = []) -> None:
        super().__init__(product="ChileGB", data=data)
        self.columns = "1y,2y,3y,4y,5y,8y,10y,date"

    def to_dict(self, query: list = []) -> dict:
        for idx in enumerate(self.fetch_data(query)):
            key = str(idx[1][-2])
            self.output[key] = {
                '1 Year': idx[1][0], '2 Year': idx[1][1], '3 Year': idx[1][2],
                '4 Year': idx[1][3], '5 Year': idx[1][4], '8 Year': idx[1][5],
                '10 Year': idx[1][6],
            }
        return self.output

    def create_table(self) -> None:
        query = """CREATE TABLE IF NOT EXISTS ChileGB
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    1y varchar(7), 2y varchar(7), 3y varchar(7),
                    4y varchar(7), 5y varchar(7), 8y varchar(7),
                    10y varchar(7), date DATE, year YEAR)
                """
        Yields_DB().create_table(query)


class China(Product):
    """Chinese Government Bonds."""
    def __init__(self, data: list = []) -> None:
        super().__init__(product="ChinaGB", data=data)
        self.columns = "1y,2y,3y,5y,7y,10y,15y,20y,30y,date"

    def to_dict(self, query: list = []) -> dict:
        for idx in enumerate(self.fetch_data(query)):
            key = str(idx[1][-2])
            self.output[key] = {
                '1 Year': idx[1][0], '2 Year': idx[1][1], '3 Year': idx[1][2],
                '5 Year': idx[1][3], '7 Year': idx[1][4], '10 Year': idx[1][5],
                '15 Year': idx[1][6], '20 Year': idx[1][7], '30 Year': idx[1][8],
            }
        return self.output

    def create_table(self) -> None:
        query = """CREATE TABLE IF NOT EXISTS ChinaGB
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    1y varchar(7), 2y varchar(7), 3y varchar(7),
                    5y varchar(7), 7y varchar(7), 10y varchar(7),
                    15y varchar(7), 20y varchar(7), 30y varchar(7),
                    date DATE, year YEAR)
                """
        Yields_DB().create_table(query)


class Colombia(Product):
    """Colombian Government Bonds."""
    def __init__(self, data: list = []) -> None:
        super().__init__(product="ColombiaGB", data=data)
        self.columns = "1y,4y,5y,10y,15y,date"

    def to_dict(self, query: list = []) -> dict:
        for idx in enumerate(self.fetch_data(query)):
            key = str(idx[1][-2])
            self.output[key] = {
                '1 Year': idx[1][0], '4 Year': idx[1][1], '5 Year': idx[1][2],
                '10 Year': idx[1][3], '15 Year': idx[1][4],
            }
        return self.output

    def create_table(self) -> None:
        query = """CREATE TABLE IF NOT EXISTS ColombiaGB
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    1y varchar(7), 4y varchar(7), 5y varchar(7),
                    10y varchar(7), 15y varchar(7), date DATE,
                    year YEAR)
                """
        Yields_DB().create_table(query)


class Crotia(Product):
    """Croatian Government Bonds."""
    def __init__(self, data: list = []) -> None:
        super().__init__(product="CroatiaGB", data=data)
        self.columns = "1y,3y,5y,10y,date"

    def to_dict(self, query: list = []) -> dict:
        for idx in enumerate(self.fetch_data(query)):
            key = str(idx[1][-2])
            self.output[key] = {
                '1 Year': idx[1][0], '3 Year': idx[1][1], '5 Year': idx[1][2],
                '10 Year': idx[1][3],
            }
        return self.output

    def create_table(self) -> None:
        query = """CREATE TABLE IF NOT EXISTS CrotiaGB
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    1y varchar(7), 3y varchar(7), 5y varchar(7),
                    10y varchar(7), date DATE, year YEAR)
                """
        Yields_DB().create_table(query)


class Cyprus(Product):
    """Cyprus Government Bonds."""
    def __init__(self, data: list = []) -> None:
        super().__init__(product="CyprusGB", data=data)
        self.columns = "1y,3y,5y,7y,10y,date"

    def to_dict(self, query: list = []) -> dict:
        for idx in enumerate(self.fetch_data(query)):
            key = str(idx[1][-2])
            self.output[key] = {
                '2 Year': idx[1][0], '3 Year': idx[1][1], '5 Year': idx[1][2],
                '7 Year': idx[1][3], '10 Year': idx[1][4],
            }
        return self.output

    def create_table(self) -> None:
        query = """CREATE TABLE IF NOT EXISTS CyprusGB
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    1y varchar(7), 3y varchar(7), 5y varchar(7),
                    7y varchar(7), 10y varchar(7), date DATE,
                    year YEAR)
                """
        Yields_DB().create_table(query)


class Czech_Republic(Product):
    """Czech Republic Government Bonds."""
    def __init__(self, data: list = []) -> None:
        super().__init__(product="CzechRepublicGB", data=data)
        self.columns = "1y,2y,3y,4y,5y,6y,7y,8y,9y,10y,15y,20y,50y,date"

    def to_dict(self, query: list = []) -> dict:
        for idx in enumerate(self.fetch_data(query)):
            key = str(idx[1][-2])
            self.output[key] = {
                '1 Year': idx[1][0], '2 Year': idx[1][1], '3 Year': idx[1][2],
                '4 Year': idx[1][3], '5 Year': idx[1][4], '6 Year': idx[1][5],
                '7 Year': idx[1][6], '8 Year': idx[1][7], '9 Year': idx[1][8],
                '10 Year': idx[1][9], '15 Year': idx[1][10], '20 Year': idx[1][11],
                '50 Year': idx[1][12],
            }
        return self.output

    def create_table(self) -> None:
        query = """CREATE TABLE IF NOT EXISTS CzechRepublicGB
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    1y varchar(7), 2y varchar(7), 3y varchar(7),
                    4y varchar(7), 5y varchar(7), 6y varchar(7),
                    7y varchar(7), 8y varchar(7), 9y varchar(7),
                    10y varchar(7), 15y varchar(7), 20y varchar(7),
                    50y varchar(7), date DATE, year YEAR)
                """
        Yields_DB().create_table(query)
