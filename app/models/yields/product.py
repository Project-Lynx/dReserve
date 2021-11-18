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


class Egypt(Product):
    """Egyptian Government Bonds."""
    def __init__(self, data: list = []) -> None:
        super().__init__(product="EgyptGB", data=data)
        self.columns = "on,3m,6m,9m,1y,2y,3y,5y,7y,10y,date"

    def to_dict(self, query: list = []) -> dict:
        for idx in enumerate(self.fetch_data(query)):
            key = str(idx[1][-2])
            self.output[key] = {
                'Overnight': idx[1][0], '3 Month': idx[1][1], '6 Month': idx[1][2],
                '9 Month': idx[1][3], '1 Year': idx[1][4], '2 Year': idx[1][5],
                '3 Year': idx[1][6], '5 Year': idx[1][7], '7 Year': idx[1][8],
                '10 Year': idx[1][9],
            }
        return self.output

    def create_table(self) -> None:
        query = """CREATE TABLE IF NOT EXISTS EgyptGB
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    on varchar(7), 3m varchar(7), 6m varchar(7),
                    9m varchar(7), 1y varchar(7), 2y varchar(7),
                    3y varchar(7), 5y varchar(7), 7y varchar(7),
                    10y varchar(7), date DATE, year YEAR)
                """
        Yields_DB().create_table(query)


class France(Product):
    """French Government Bonds."""
    def __init__(self, data: list = []) -> None:
        super().__init__(product="FranceGB", data=data)
        self.columns = "1m,3m,6m,9m,1y,2y,3y,4y,5y,6y,7y,8y,9y,10y,15y,20y,25y,30y,50y,date"

    def to_dict(self, query: list = []) -> dict:
        for idx in enumerate(self.fetch_data(query)):
            key = str(idx[1][-2])
            self.output[key] = {
                '1 Month': idx[1][0], '3 Month': idx[1][1], '6 Month': idx[1][2],
                '9 Month': idx[1][3], '1 Year': idx[1][4], '2 Year': idx[1][5],
                '3 Year': idx[1][6], '4 Year': idx[1][7], '5 Year': idx[1][8],
                '6 Year': idx[1][9], '7 Year': idx[1][10], '8 Year': idx[1][11],
                '9 Year': idx[1][12], '10 Year': idx[1][13], '15 Year': idx[1][14],
                '20 Year': idx[1][15], '25 Year': idx[1][16], '30 Year': idx[1][17],
                '50 Year': idx[1][18],
            }
        return self.output

    def create_table(self) -> None:
        query = """CREATE TABLE IF NOT EXISTS FranceGB
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    1m varchar(7), 3m varchar(7), 6m varchar(7),
                    9m varchar(7), 1y varchar(7), 2y varchar(7),
                    3y varchar(7), 4y varchar(7), 5y varchar(7),
                    6y varchar(7), 7y varchar(7), 8y varchar(7),
                    9y varchar(7), 10y varchar(7), 15y varchar(7),
                    20y varchar(7), 25y varchar(7), 30y varchar(7),
                    50y varchar(7), date DATE, year YEAR)
                """
        Yields_DB().create_table(query)


class Germany(Product):
    """German Government Bonds."""
    def __init__(self, data: list = []) -> None:
        super().__init__(product="GermanGB", data=data)
        self.columns = "3m,6m,9m,1y,2y,3y,4y,5y,6y,7y,8y,9y,10y,15y,20y,25y,30y,date"

    def to_dict(self, query: list = []) -> dict:
        for idx in enumerate(self.fetch_data(query)):
            key = str(idx[1][-2])
            self.output[key] = {
                '3 Month': idx[1][0], '6 Month': idx[1][1], '9 Month': idx[1][2],
                '1 Year': idx[1][3], '2 Year': idx[1][4], '3 Year': idx[1][5],
                '4 Year': idx[1][6], '5 Year': idx[1][7], '6 Year': idx[1][8],
                '7 Year': idx[1][9], '8 Year': idx[1][10], '9 Year': idx[1][11],
                '10 Year': idx[1][12], '15 Year': idx[1][13], '20 Year': idx[1][14],
                '25 Year': idx[1][15], '30 Year': idx[1][16],
            }
        return self.output

    def create_table(self) -> None:
        query = """CREATE TABLE IF NOT EXISTS GermanGB
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    3m varchar(7), 6m varchar(7), 9m varchar(7),
                    1y varchar(7), 2y varchar(7), 3y varchar(7),
                    4y varchar(7), 5y varchar(7), 6y varchar(7),
                    7y varchar(7), 8y varchar(7), 9y varchar(7),
                    10y varchar(7), 15y varchar(7), 20y varchar(7),
                    25y varchar(7), 30y varchar(7), date DATE, year YEAR)
                """
        Yields_DB().create_table(query)


class Greece(Product):
    """Greek Government Bonds."""
    def __init__(self, data: list = []) -> None:
        super().__init__(product="GreeceGB", data=data)
        self.columns = "1m,3m,6m,5y,10y,15y,20y,25y,date"

    def to_dict(self, query: list = []) -> dict:
        for idx in enumerate(self.fetch_data(query)):
            key = str(idx[1][-2])
            self.output[key] = {
                '1 Month': idx[1][0], '3 Month': idx[1][1], '6 Month': idx[1][2],
                '5 Year': idx[1][3], '10 Year': idx[1][4], '15 Year': idx[1][5],
                '20 Year': idx[1][6], '25 Year': idx[1][7],
            }
        return self.output

    def create_table(self) -> None:
        query = """CREATE TABLE IF NOT EXISTS GreeceGB
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    1m varchar(7), 3m varchar(7), 6m varchar(7),
                    5y varchar(7), 10y varchar(7), 15y varchar(7),
                    20y varchar(7), 25y varchar(7), date DATE, year YEAR)
                """
        Yields_DB().create_table(query)


class Hong_Kong(Product):
    """Hong Kong Government Bonds."""
    def __init__(self, data: list = []) -> None:
        super().__init__(product="HongKongGB", data=data)
        self.columns = "1w,1m,3m,6m,9m,1y,2y,3y,5y,7y,10y,15y,date"

    def to_dict(self, query: list = []) -> dict:
        for idx in enumerate(self.fetch_data(query)):
            key = str(idx[1][-2])
            self.output[key] = {
                '1 Week': idx[1][0], '1 Month': idx[1][1], '3 Month': idx[1][2],
                '6 Month': idx[1][3], '9 Month': idx[1][4], '1 Year': idx[1][5],
                '2 Year': idx[1][6], '3 Year': idx[1][7], '5 Year': idx[1][8],
                '7 Year': idx[1][9], '10 Year': idx[1][10], '15 Year': idx[1][11],
            }
        return self.output

    def create_table(self) -> None:
        query = """CREATE TABLE IF NOT EXISTS HongKongGB
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    1w varchar(7), 1m varchar(7), 3m varchar(7),
                    6m varchar(7), 9m varchar(7), 1y varchar(7),
                    2y varchar(7), 3y varchar(7), 5y varhcar(7),
                    7y varhcar(7), 10y varhcar(7), 15y varhcar(7),
                    date DATE, year YEAR)
                """
        Yields_DB().create_table(query)


class Hungary(Product):
    """Hungarian Government Bonds."""
    def __init__(self, data: list = []) -> None:
        super().__init__(product="HungaryGB", data=data)
        self.columns = "3m,6m,1y,3y,5y,10y,15y,date"

    def to_dict(self, query: list = []) -> dict:
        for idx in enumerate(self.fetch_data(query)):
            key = str(idx[1][-2])
            self.output[key] = {
                '3 Month': idx[1][0], '6 Month': idx[1][1], '1 Year': idx[1][2],
                '3 year': idx[1][3], '5 Year': idx[1][4], '10 Year': idx[1][5],
                '15 Year': idx[1][6],
            }
        return self.output

    def create_table(self) -> None:
        query = """CREATE TABLE IF NOT EXISTS HungaryGB
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    3m varchar(7), 6m varchar(7), 1y varchar(7),
                    3y varchar(7), 5y varchar(7), 10y varchar(7),
                    15y varhcar(7), date DATE, year YEAR)
                """
        Yields_DB().create_table(query)


class Iceland(Product):
    """Iceland Government Bonds."""
    def __init__(self, data: list = []) -> None:
        super().__init__(product="IcelandGB", data=data)
        self.columns = "2y,5y,10y,date"

    def to_dict(self, query: list = []) -> dict:
        for idx in enumerate(self.fetch_data(query)):
            key = str(idx[1][-2])
            self.output[key] = {
                '2 Year': idx[1][0], '5 Year': idx[1][1], '10 Year': idx[1][2],
            }
        return self.output

    def create_table(self) -> None:
        query = """CREATE TABLE IF NOT EXISTS IcelandGB
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    2y varchar(7), 5y varchar(7), 10y varchar(7),
                    date DATE, year YEAR)
                """
        Yields_DB().create_table(query)


class India(Product):
    """India Government Bonds."""
    def __init__(self, data: list = []) -> None:
        super().__init__(product="IndiaGB", data=data)
        self.columns = "3m,6m,1y,2y,3y,4y,5y,6y,7y,8y,9y,10y,11y,12y,13y,14y,15y,19y,24y,30y,date"

    def to_dict(self, query: list = []) -> dict:
        for idx in enumerate(self.fetch_data(query)):
            key = str(idx[1][-2])
            self.output[key] = {
                '3 Month': idx[1][0], '6 Month': idx[1][1], '1 Year': idx[1][2],
                '2 Year': idx[1][3], '3 Year': idx[1][4], '4 Year': idx[1][5],
                '5 Year': idx[1][6], '6 Year': idx[1][7], '7 Year': idx[1][8],
                '8 Year': idx[1][9], '9 Year': idx[1][10], '10 Year': idx[1][11],
                '11 Year': idx[1][12], '12 Year': idx[1][13], '13 Year': idx[1][14],
                '14 Year': idx[1][15], '15 Year': idx[1][16], '19 Year': idx[1][17],
                '24 Year': idx[1][18], '30 Year': idx[1][19],
            }
        return self.output

    def create_table(self) -> None:
        query = """CREATE TABLE IF NOT EXISTS IndiaGB
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    3m varchar(7), 6m varchar(7), 1y varchar(7),
                    2y varchar(7), 3y varchar(7), 4y varchar(7),
                    5y varchar(7), 6y varchar(7), 7y varchar(7),
                    8y varchar(7), 9y varchar(7), 10y varchar(7),
                    11y varchar(7), 12y varchar(7), 13y varchar(7),
                    14y varchar(7), 15y varchar(7), 19y varchar(7),
                    24y varchar(7), 30y varchar(7), date DATE, year YEAR)
                """
        Yields_DB().create_table(query)


class Indonesia(Product):
    """Indonesian Government Bonds."""
    def __init__(self, data: list = []) -> None:
        super().__init__(product="IndonesiaGB", data=data)
        self.columns = "1m,3m,6m,1y,3y,5y,10y,15y,20y,25y,30y,date"

    def to_dict(self, query: list = []) -> dict:
        for idx in enumerate(self.fetch_data(query)):
            key = str(idx[1][-2])
            self.output[key] = {
                '1 Month': idx[1][0], '3 Month': idx[1][1], '6 Month': idx[1][2],
                '1 Year': idx[1][3], '3 Year': idx[1][4], '5 Year': idx[1][5],
                '10 Year': idx[1][6], '15 Year': idx[1][7], '20 Year': idx[1][8],
                '25 Year': idx[1][9], '30 Year': idx[1][10],
            }
        return self.output

    def create_table(self) -> None:
        query = """CREATE TABLE IF NOT EXISTS IndonesiaGB
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    1m varchar(7), 3m varchar(7), 6m varchar(7),
                    1y varchar(7), 3y varchar(7), 5y varchar(7),
                    10y varchar(7), 15y varchar(7), 20y varchar(7),
                    25y varchar(7), 30y varchar(7), date DATE, year YEAR)
                """
        Yields_DB().create_table(query)


class Ireland(Product):
    """Ireland Government Bonds."""
    def __init__(self, data: list = []) -> None:
        super().__init__(product="IrelandGB", data=data)
        self.columns = "3m,6m,1y,3y,4y,5y,6y,7y,8y,10y,15y,20y,30y,date"

    def to_dict(self, query: list = []) -> dict:
        for idx in enumerate(self.fetch_data(query)):
            key = str(idx[1][-2])
            self.output[key] = {
                '3 Month': idx[1][0], '6 Month': idx[1][1], '1 Year': idx[1][2],
                '3 Year': idx[1][3], '4 Year': idx[1][4], '5 Year': idx[1][5],
                '6 Year': idx[1][6], '7 Year': idx[1][7], '8 Year': idx[1][8],
                '10 Year': idx[1][9], '15 Year': idx[1][10], '20 Year': idx[1][11],
                '30 Year': idx[1][12],
            }
        return self.output

    def create_table(self) -> None:
        query = """CREATE TABLE IF NOT EXISTS IrelandGB
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    3m varchar(7), 6m varchar(7), 1y varchar(7),
                    3y varchar(7), 4y varchar(7), 5y varchar(7),
                    6y varchar(7), 7y varchar(7), 8y varchar(7),
                    10y varchar(7), 15y varchar(7), 20y varchar(7),
                    30y varchar(7), date DATE, year YEAR)
                """
        Yields_DB().create_table(query)


class Israel(Product):
    """Israeli Government Bonds."""
    def __init__(self, data: list = []) -> None:
        super().__init__(product="IsraelGB", data=data)
        self.columns = "1m,3m,6m,9m,1y,2y,3y,5y,10y,30y,date"

    def to_dict(self, query: list = []) -> dict:
        for idx in enumerate(self.fetch_data(query)):
            key = str(idx[1][-2])
            self.output[key] = {
                '1 Month': idx[1][0], '3 Month': idx[1][1], '6 Month': idx[1][2],
                '9 Month': idx[1][3], '1 Year': idx[1][4], '2 Year': idx[1][5],
                '3 Year': idx[1][6], '5 Year': idx[1][7], '10 Year': idx[1][8],
                '30 Year': idx[1][9],
            }
        return self.output

    def create_table(self) -> None:
        query = """CREATE TABLE IF NOT EXISTS IsraelGB
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    1m varchar(7), 3m varchar(7), 6m varchar(7),
                    9m varchar(7), 1y varchar(7), 2y varchar(7),
                    3y varchar(7), 5y varchar(7), 10y varchar(7),
                    30y varchar(7), date DATE, year YEAR)
                """
        Yields_DB().create_table(query)


class Italy(Product):
    """Italian Government Bonds."""
    def __init__(self, data: list = []) -> None:
        super().__init__(product="ItalyGB", data=data)
        self.columns = "1m,3m,6m,9m,1y,2y,3y,4y,5y,6y,7y,8y,9y,10y,15y,20y,30y,50y,date"

    def to_dict(self, query: list = []) -> dict:
        for idx in enumerate(self.fetch_data(query)):
            key = str(idx[1][-2])
            self.output[key] = {
                '1 Month': idx[1][0], '3 Month': idx[1][1], '6 Month': idx[1][2],
                '9 Month': idx[1][3], '1 Year': idx[1][4], '2 Year': idx[1][5],
                '3 Year': idx[1][6], '4 Year': idx[1][7], '5 Year': idx[1][8],
                '6 Year': idx[1][9], '7 Year': idx[1][10], '8 Year': idx[1][11],
                '9 Year': idx[1][12], '10 Year': idx[1][13], '15 Year': idx[1][14],
                '20 Year': idx[1][15], '30 Year': idx[1][16], '50 Year': idx[1][17],
            }
        return self.output

    def create_table(self) -> None:
        query = """CREATE TABLE IF NOT EXISTS ItalyGB
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    1m varchar(7), 3m varchar(7), 6m varchar(7),
                    9m varchar(7), 1y varchar(7), 2y varchar(7),
                    3y varchar(7), 4y varchar(7), 5y varchar(7),
                    6y varchar(7), 7y varchar(7), 8y varchar(7),
                    9y varchar(7), 10y varchar(7), 15y varchar(7),
                    20y varchar(7), 30y varchar(7), 50y varchar(7),
                    date DATE, year YEAR)
                """
        Yields_DB().create_table(query)


class Japan(Product):
    """Japanese Government Bonds."""
    def __init__(self, data: list = []) -> None:
        super().__init__(product="JapanGB", data=data)
        self.columns = "1m,3m,6m,9m,1y,2y,3y,4y,5y,6y,7y,8y,9y,10y,15y,20y,30y,40y,date"

    def to_dict(self, query: list = []) -> dict:
        for idx in enumerate(self.fetch_data(query)):
            key = str(idx[1][-2])
            self.output[key] = {
                '1 Month': idx[1][0], '3 Month': idx[1][1], '6 Month': idx[1][2],
                '9 Month': idx[1][3], '1 Year': idx[1][4], '2 Year': idx[1][5],
                '3 Year': idx[1][6], '4 Year': idx[1][7], '5 Year': idx[1][8],
                '6 Year': idx[1][9], '7 Year': idx[1][10], '8 Year': idx[1][11],
                '9 Year': idx[1][12], '10 Year': idx[1][13], '15 Year': idx[1][14],
                '20 Year': idx[1][15], '30 Year': idx[1][16], '40 Year': idx[1][17],
            }
        return self.output

    def create_table(self) -> None:
        query = """CREATE TABLE IF NOT EXISTS JapanGB
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    1m varchar(7), 3m varchar(7), 6m varchar(7),
                    9m varchar(7), 1y varchar(7), 2y varchar(7),
                    3y varchar(7), 4y varchar(7), 5y varchar(7),
                    6y varchar(7), 7y varchar(7), 8y varchar(7),
                    9y varchar(7), 10y varchar(7), 15y varchar(7),
                    20y varchar(7), 30y varchar(7), 40y varchar(7),
                    date DATE, year YEAR)
                """
        Yields_DB().create_table(query)


class Jordan(Product):
    """Jordan Government Bonds."""
    def __init__(self, data: list = []) -> None:
        super().__init__(product="JordanGB", data=data)
        self.columns = "3m,6m,1y,2y,3y,5y,7y,10y,date"

    def to_dict(self, query: list = []) -> dict:
        for idx in enumerate(self.fetch_data(query)):
            key = str(idx[1][-2])
            self.output[key] = {
                '3 Month': idx[1][0], '6 Month': idx[1][1], '1 Year': idx[1][2],
                '2 Year': idx[1][3], '3 Year': idx[1][4], '5 Year': idx[1][5],
                '7 Year': idx[1][6], '10 Year': idx[1][7],
            }
        return self.output

    def create_table(self) -> None:
        query = """CREATE TABLE IF NOT EXISTS JordanGB
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    3m varchar(7), 6m varchar(7), 1y varchar(7),
                    2y varchar(7), 3y varchar(7), 5y varchar(7),
                    7y varchar(7), 10y varchar(7), date DATE, year YEAR)
                """
        Yields_DB().create_table(query)


class Kazakhstan(Product):
    """Kazakhstan Government Bonds."""
    def __init__(self, data: list = []) -> None:
        super().__init__(product="KazakhstanGB", data=data)
        self.columns = "1y,2y,3y,4y,5y,6y,7y,8y,9y,10y,15y,25y,date"

    def to_dict(self, query: list = []) -> dict:
        for idx in enumerate(self.fetch_data(query)):
            key = str(idx[1][-2])
            self.output[key] = {
                '1 Year': idx[1][0], '2 Year': idx[1][1], '3 Year': idx[1][2],
                '4 Year': idx[1][3], '5 Year': idx[1][4], '6 Year': idx[1][5],
                '7 Year': idx[1][6], '8 Year': idx[1][7], '9 Year': idx[1][8],
                '10 Year': idx[1][9], '15 Year': idx[1][10], '25 Year': idx[1][11],
            }
        return self.output

    def create_table(self) -> None:
        query = """CREATE TABLE IF NOT EXISTS KazakhstanGB
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    1y varchar(7), 2y varchar(7), 3y varchar(7),
                    4y varchar(7), 5y varchar(7), 6y varchar(7),
                    3y varchar(7), 4y varchar(7), 5y varchar(7),
                    6y varchar(7), 7y varchar(7), 8y varchar(7),
                    9y varchar(7), 10y varchar(7), 15y varchar(7),
                    25y varchar(7), date DATE, year YEAR)
                """
        Yields_DB().create_table(query)


class Kenya(Product):
    """Kenya Government Bonds."""
    def __init__(self, data: list = []) -> None:
        super().__init__(product="KenyaGB", data=data)
        self.columns = "on,3m,6m,1y,2y,3y,4y,5y,6y,7y,8y,9y,10y,15y,20y,25y,date"

    def to_dict(self, query: list = []) -> dict:
        for idx in enumerate(self.fetch_data(query)):
            key = str(idx[1][-2])
            self.output[key] = {
                'Overnight': idx[1][0], '3 Month': idx[1][1], '6 Month': idx[1][2],
                '1 Year': idx[1][3], '2 Year': idx[1][4], '3 Year': idx[1][5],
                '4 Year': idx[1][6], '5 Year': idx[1][7], '6 Year': idx[1][8],
                '7 Year': idx[1][9], '8 Year': idx[1][10], '9 Year': idx[1][11],
                '10 Year': idx[1][12], '15 Year': idx[1][13], '20 Year': idx[1][14],
                '25 Year': idx[1][15],
            }
        return self.output

    def create_table(self) -> None:
        query = """CREATE TABLE IF NOT EXISTS KenyaGB
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    on varchar(7), 3m varchar(7), 6m varchar(7),
                    1y varchar(7), 2y varchar(7), 3y varchar(7),
                    4y varchar(7), 5y varchar(7), 6y varchar(7),
                    7y varchar(7), 8y varchar(7), 9y varchar(7),
                    10y varchar(7), 15y varchar(7), 20y varchar(7),
                    25y varchar(7), date DATE, year YEAR)
                """
        Yields_DB().create_table(query)


class Malaysia(Product):
    """Malaysian Government Bonds."""
    def __init__(self, data: list = []) -> None:
        super().__init__(product="MalaysiaGB", data=data)
        self.columns = "3w,3m,7m,1y,3y,5y,7y,10y,15y,20y,30y,date"

    def to_dict(self, query: list = []) -> dict:
        for idx in enumerate(self.fetch_data(query)):
            key = str(idx[1][-2])
            self.output[key] = {
                '3 Week': idx[1][0], '3 Month': idx[1][1], '7 Month': idx[1][2],
                '1 Year': idx[1][3], '3 Year': idx[1][4], '5 Year': idx[1][5],
                '7 Year': idx[1][6], '10 Year': idx[1][7], '15 Year': idx[1][8],
                '20 Year': idx[1][9], '30 Year': idx[1][10],
            }
        return self.output

    def create_table(self) -> None:
        query = """CREATE TABLE IF NOT EXISTS MalaysiaGB
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    3w varchar(7), 3m varchar(7), 7m varchar(7),
                    1y varchar(7), 3y varchar(7), 5y varchar(7),
                    7y varchar(7), 10y varchar(7), 15y varchar(7),
                    20y varchar(7), 30y varchar(7), date DATE, year YEAR)
                """
        Yields_DB().create_table(query)


class Malta(Product):
    """Malta Government Bonds."""
    def __init__(self, data: list = []) -> None:
        super().__init__(product="MaltaGB", data=data)
        self.columns = "1m,3m,6m,1y,3y,5y,10y,20y,25y,date"

    def to_dict(self, query: list = []) -> dict:
        for idx in enumerate(self.fetch_data(query)):
            key = str(idx[1][-2])
            self.output[key] = {
                '1 Month': idx[1][0], '3 Month': idx[1][1], '6 Month': idx[1][2],
                '1 Year': idx[1][3], '3 Year': idx[1][4], '5 Year': idx[1][5],
                '10 Year': idx[1][6], '20 Year': idx[1][7], '25 Year': idx[1][8],
            }
        return self.output

    def create_table(self) -> None:
        query = """CREATE TABLE IF NOT EXISTS MaltaGB
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    1m varchar(7), 3m varchar(7), 6m varchar(7),
                    1y varchar(7), 3y varchar(7), 5y varchar(7),
                    10y varchar(7), 20y varchar(7), 25y varchar(7),
                    date DATE, year YEAR)
                """
        Yields_DB().create_table(query)


class Mauritius(Product):
    """Mauritius Government Bonds."""
    def __init__(self, data: list = []) -> None:
        super().__init__(product="MauritiusGB", data=data)
        self.columns = "2m,4m,6m,8m,1y,2y,3y,4y,5y,10y,15y,20y,date"

    def to_dict(self, query: list = []) -> dict:
        for idx in enumerate(self.fetch_data(query)):
            key = str(idx[1][-2])
            self.output[key] = {
                '2 Month': idx[1][0], '4 Month': idx[1][1], '6 Month': idx[1][2],
                '8 Month': idx[1][3], '1 Year': idx[1][4], '2 Year': idx[1][5],
                '3 Year': idx[1][6], '4 Year': idx[1][7], '5 Year': idx[1][8],
                '10 Year': idx[1][9], '15 Year': idx[1][10], '20 Year': idx[1][11],
            }
        return self.output

    def create_table(self) -> None:
        query = """CREATE TABLE IF NOT EXISTS MauritiusGB
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    2m varchar(7), 4m varchar(7), 6m varchar(7),
                    8m varchar(7), 1y varchar(7), 2y varchar(7),
                    3y varchar(7), 4y varchar(7), 5y varchar(7),
                    10y varchar(7), 15y varchar(7), 20y varchar(7),
                    date DATE, year YEAR)
                """
        Yields_DB().create_table(query)


class Mexico(Product):
    """Mexican Government Bonds."""
    def __init__(self, data: list = []) -> None:
        super().__init__(product="MexicoGB", data=data)
        self.columns = "1m,3m,6m,9m,1y,3y,5y,7y,10y,15y,20y,30y,date"

    def to_dict(self, query: list = []) -> dict:
        for idx in enumerate(self.fetch_data(query)):
            key = str(idx[1][-2])
            self.output[key] = {
                '1 Month': idx[1][0], '3 Month': idx[1][1], '6 Month': idx[1][2],
                '9 Month': idx[1][3], '1 Year': idx[1][4], '3 Year': idx[1][5],
                '5 Year': idx[1][6], '7 Year': idx[1][7], '10 Year': idx[1][8],
                '15 Year': idx[1][9], '20 Year': idx[1][10], '30 Year': idx[1][11],
            }
        return self.output

    def create_table(self) -> None:
        query = """CREATE TABLE IF NOT EXISTS MexicoGB
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    1m varchar(7), 3m varchar(7), 6m varchar(7),
                    9m varchar(7), 1y varchar(7), 3y varchar(7),
                    5y varchar(7), 7y varchar(7), 10y varchar(7),
                    15y varchar(7), 20y varchar(7), 30y varchar(7),
                    date DATE, year YEAR)
                """
        Yields_DB().create_table(query)


class Morocco(Product):
    """Moroccan Government Bonds."""
    def __init__(self, data: list = []) -> None:
        super().__init__(product="MoroccoGB", data=data)
        self.columns = "3m,6m,2y,5y,10y,15y,date"

    def to_dict(self, query: list = []) -> dict:
        for idx in enumerate(self.fetch_data(query)):
            key = str(idx[1][-2])
            self.output[key] = {
                '3 Month': idx[1][0], '6 Month': idx[1][1], '2 Year': idx[1][2],
                '5 Year': idx[1][3], '10 Year': idx[1][4], '15 Year': idx[1][5],
            }
        return self.output

    def create_table(self) -> None:
        query = """CREATE TABLE IF NOT EXISTS MoroccoGB
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    3m varchar(7), 6m varchar(7), 2y varchar(7),
                    5y varchar(7), 10y varchar(7), 15y varchar(7),
                    date DATE, year YEAR)
                """
        Yields_DB().create_table(query)


class Namibia(Product):
    """Namibia Government Bonds."""
    def __init__(self, data: list = []) -> None:
        super().__init__(product="NamibiaGB", data=data)
        self.columns = "3m,6m,9m,1y,3y,7y,10y,15y,20y,date"

    def to_dict(self, query: list = []) -> dict:
        for idx in enumerate(self.fetch_data(query)):
            key = str(idx[1][-2])
            self.output[key] = {
                '3 Month': idx[1][0], '6 Month': idx[1][1], '9 Month': idx[1][2],
                '1 Year': idx[1][3], '3 Year': idx[1][4], '7 Year': idx[1][5],
                '10 Year': idx[1][6], '15 Year': idx[1][7], '20 Year': idx[1][8],
            }
        return self.output

    def create_table(self) -> None:
        query = """CREATE TABLE IF NOT EXISTS NamibiaGB
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    3m varchar(7), 6m varchar(7), 9m varchar(7),
                    1y varchar(7), 3y varchar(7), 7y varchar(7),
                    10y varchar(7), 15y varchar(7), 20y varchar(7),
                    date DATE, year YEAR)
                """
        Yields_DB().create_table(query)


class Netherlands(Product):
    """Netherlands Government Bonds."""
    def __init__(self, data: list = []) -> None:
        super().__init__(product="NetherlandsGB", data=data)
        self.columns = "1m,3m,6m,2y,3y,4y,5y,6y,7y,8y,9y,10y,15y,20y,25y,30y,date"

    def to_dict(self, query: list = []) -> dict:
        for idx in enumerate(self.fetch_data(query)):
            key = str(idx[1][-2])
            self.output[key] = {
                '1 Month': idx[1][0], '3 Month': idx[1][1], '6 Month': idx[1][2],
                '2 Year': idx[1][3], '3 Year': idx[1][4], '4 Year': idx[1][5],
                '5 Year': idx[1][6], '6 Year': idx[1][7], '7 Year': idx[1][8],
                '8 Year': idx[1][9], '9 Year': idx[1][10], '10 Year': idx[1][11],
                '15 Year': idx[1][12], '20 Year': idx[1][13], '25 Year': idx[1][14],
                '30 Year': idx[1][15],
            }
        return self.output

    def create_table(self) -> None:
        query = """CREATE TABLE IF NOT EXISTS NetherlandsGB
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    1m varchar(7), 3m varchar(7), 6m varchar(7),
                    2y varchar(7), 3y varchar(7), 4y varchar(7),
                    5y varchar(7), 6y varchar(7), 7y varchar(7),
                    8y varchar(7), 9y varchar(7), 10y varchar(7),
                    15y varchar(7), 20y varchar(7), 25y varchar(7),
                    30y varchar(7), date DATE, year YEAR)
                """
        Yields_DB().create_table(query)


class Nigeria(Product):
    """Nigerian Government Bonds."""
    def __init__(self, data: list = []) -> None:
        super().__init__(product="NigeriaGB", data=data)
        self.columns = "3m,6m,1y,2y,4y,7y,10y,20y,date"

    def to_dict(self, query: list = []) -> dict:
        for idx in enumerate(self.fetch_data(query)):
            key = str(idx[1][-2])
            self.output[key] = {
                '3 Month': idx[1][0], '6 Month': idx[1][1], '1 Year': idx[1][2],
                '2 Year': idx[1][3], '4 Year': idx[1][4], '7 Year': idx[1][5],
                '10 Year': idx[1][6], '20 Year': idx[1][7],
            }
        return self.output

    def create_table(self) -> None:
        query = """CREATE TABLE IF NOT EXISTS NigeriaGB
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    3m varchar(7), 6m varchar(7), 1y varchar(7),
                    2y varchar(7), 4y varchar(7), 7y varchar(7),
                    10y varchar(7), 20y varchar(7), date DATE, year YEAR)
                """
        Yields_DB().create_table(query)


class Norway(Product):
    """Norway Government Bonds."""
    def __init__(self, data: list = []) -> None:
        super().__init__(product="NorwayGB", data=data)
        self.columns = "3m,6m,9m,1y,3y,5y,10y,date"

    def to_dict(self, query: list = []) -> dict:
        for idx in enumerate(self.fetch_data(query)):
            key = str(idx[1][-2])
            self.output[key] = {
                '3 Month': idx[1][0], '6 Month': idx[1][1], '9 Month': idx[1][2],
                '1 Year': idx[1][3], '3 Year': idx[1][4], '5 Year': idx[1][5],
                '10 Year': idx[1][6],
            }
        return self.output

    def create_table(self) -> None:
        query = """CREATE TABLE IF NOT EXISTS NorwayGB
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    3m varchar(7), 6m varchar(7), 9m varchar(7),
                    1y varchar(7), 3y varchar(7), 5y varchar(7),
                    10y varchar(7), date DATE, year YEAR)
                """
        Yields_DB().create_table(query)


class Pakistan(Product):
    """Pakistani Government Bonds."""
    def __init__(self, data: list = []) -> None:
        super().__init__(product="PakistanGB", data=data)
        self.columns = "3m,6m,1y,3y,5y,10y,14y,20y,date"

    def to_dict(self, query: list = []) -> dict:
        for idx in enumerate(self.fetch_data(query)):
            key = str(idx[1][-2])
            self.output[key] = {
                '3 Month': idx[1][0], '6 Month': idx[1][1], '1 Year': idx[1][2],
                '3 Year': idx[1][3], '5 Year': idx[1][4], '10 Year': idx[1][5],
                '14 Year': idx[1][6], '20 Year': idx[1][7],
            }
        return self.output

    def create_table(self) -> None:
        query = """CREATE TABLE IF NOT EXISTS PakistanGB
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    3m varchar(7), 6m varchar(7), 1y varchar(7),
                    3y varchar(7), 5y varchar(7), 10y varchar(7),
                    14y varchar(7), 20yvarchar(7), date DATE, year YEAR)
                """
        Yields_DB().create_table(query)


class Peru(Product):
    """Peruvian Government Bonds."""
    def __init__(self, data: list = []) -> None:
        super().__init__(product="PeruGB", data=data)
        self.columns = "2y,5y,10y,15y,20y,30y,date"

    def to_dict(self, query: list = []) -> dict:
        for idx in enumerate(self.fetch_data(query)):
            key = str(idx[1][-2])
            self.output[key] = {
                '2 Year': idx[1][0], '5 Year': idx[1][1], '10 Year': idx[1][2],
                '15 Year': idx[1][3], '20 Year': idx[1][4], '30 Year': idx[1][5],
            }
        return self.output

    def create_table(self) -> None:
        query = """CREATE TABLE IF NOT EXISTS PeruGB
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    2y varchar(7), 5y varchar(7), 10y varchar(7),
                    15y varchar(7), 20y varchar(7), 30y varchar(7),
                    date DATE, year YEAR)
                """
        Yields_DB().create_table(query)


class Philippines(Product):
    """Philippino Government Bonds."""
    def __init__(self, data: list = []) -> None:
        super().__init__(product="PhilippinesGB", data=data)
        self.columns = "1m,3m,6m,1y,2y,3y,4y,5y,7y,10y,20y,date"

    def to_dict(self, query: list = []) -> dict:
        for idx in enumerate(self.fetch_data(query)):
            key = str(idx[1][-2])
            self.output[key] = {
                '1 Month': idx[1][0], '3 Month': idx[1][1], '6 Month': idx[1][2],
                '1 Year': idx[1][3], '2 Year': idx[1][4], '3 Year': idx[1][5],
                '4 Year': idx[1][6], '5 Year': idx[1][7], '7 Year': idx[1][8],
                '10 Year': idx[1][9], '20 Year': idx[1][10],
            }
        return self.output

    def create_table(self) -> None:
        query = """CREATE TABLE IF NOT EXISTS PhilippinesGB
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    1m varchar(7), 3m varchar(7), 6m varchar(7),
                    1y varchar(7), 2y varchar(7), 3y varchar(7),
                    4y varchar(7), 5y varchar(7), 7y varchar(7),
                    10y varchar(7), 20y varchar(7), date DATE, year YEAR)
                """
        Yields_DB().create_table(query)


class Poland(Product):
    """Polish Government Bonds."""
    def __init__(self, data: list = []) -> None:
        super().__init__(product="PolandGB", data=data)
        self.columns = "on,1m,2m,1y,2y,3y,4y,5y,6y,7y,9y,10y,date"

    def to_dict(self, query: list = []) -> dict:
        for idx in enumerate(self.fetch_data(query)):
            key = str(idx[1][-2])
            self.output[key] = {
                'Overnight': idx[1][0], '1 Month': idx[1][1], '2 Month': idx[1][2],
                '1 Year': idx[1][3], '2 Year': idx[1][4], '3 Year': idx[1][5],
                '4 Year': idx[1][6], '5 Year': idx[1][7], '6 Year': idx[1][8],
                '7 Year': idx[1][9], '9 Year': idx[1][10], '10 Year': idx[1][11],
            }
        return self.output

    def create_table(self) -> None:
        query = """CREATE TABLE IF NOT EXISTS PolandGB
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    on varchar(7), 1m varchar(7), 2m varchar(7),
                    1y varchar(7), 2y varchar(7), 3y varchar(7),
                    4y varchar(7), 5y varchar(7), 6y varchar(7),
                    7y varchar(7), 9y varchar(7), 10y varchar(7),
                    date DATE, year YEAR)
                """
        Yields_DB().create_table(query)


class Portugal(Product):
    """Portaguese Government Bonds."""
    def __init__(self, data: list = []) -> None:
        super().__init__(product="PortugalGB", data=data)
        self.columns = "3m,6m,1y,2y,3y,4y,5y,6y,7y,8y,9y,10y,15y,20y,30y,date"

    def to_dict(self, query: list = []) -> dict:
        for idx in enumerate(self.fetch_data(query)):
            key = str(idx[1][-2])
            self.output[key] = {
                '3 Month': idx[1][0], '6 Month': idx[1][1], '1 Year': idx[1][2],
                '2 Year': idx[1][3], '3 Year': idx[1][4], '4 Year': idx[1][5],
                '5 Year': idx[1][6], '6 Year': idx[1][7], '7 Year': idx[1][8],
                '8 Year': idx[1][9], '9 Year': idx[1][10], '10 Year': idx[1][11],
                '15 Year': idx[1][12], '20 Year': idx[1][13], '30 Year': idx[1][14],
            }
        return self.output

    def create_table(self) -> None:
        query = """CREATE TABLE IF NOT EXISTS PortugalGB
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    3m varchar(7), 6m varchar(7), 1y varchar(7),
                    2y varchar(7), 3y varchar(7), 4y varchar(7),
                    5y varchar(7), 6y varchar(7), 7y varchar(7),
                    8y varchar(7), 9y varchar(7), 10y varchar(7),
                    15y varchar(7), 20y varchar(7), 30y varchar(7),
                    date DATE, year YEAR)
                """
        Yields_DB().create_table(query)


class Qatar(Product):
    """Qatar Government Bonds."""
    def __init__(self, data: list = []) -> None:
        super().__init__(product="QatarGB", data=data)
        self.columns = "2y,3y,5y,10y,30y,date"

    def to_dict(self, query: list = []) -> dict:
        for idx in enumerate(self.fetch_data(query)):
            key = str(idx[1][-2])
            self.output[key] = {
                '2 Year': idx[1][0], '3 Year': idx[1][1], '5 Year': idx[1][2],
                '10 Year': idx[1][3], '30 Year': idx[1][4],
            }
        return self.output

    def create_table(self) -> None:
        query = """CREATE TABLE IF NOT EXISTS QatarGB
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    2y varchar(7), 3y varchar(7), 5y varchar(7),
                    10y varchar(7), 30y varchar(7), date DATE, year YEAR)
                """
        Yields_DB().create_table(query)


class Romania(Product):
    """Romanian Government Bonds."""
    def __init__(self, data: list = []) -> None:
        super().__init__(product="RomaniaGB", data=data)
        self.columns = "6m,1y,2y,3y,4y,5y,7y,10y,date"

    def to_dict(self, query: list = []) -> dict:
        for idx in enumerate(self.fetch_data(query)):
            key = str(idx[1][-2])
            self.output[key] = {
                '6 Month': idx[1][0], '1 Year': idx[1][1], '2 Year': idx[1][2],
                '3 Year': idx[1][3], '4 Year': idx[1][4], '5 Year': idx[1][5],
                '7 Year': idx[1][6], '10 Year': idx[1][7],
            }
        return self.output

    def create_table(self) -> None:
        query = """CREATE TABLE IF NOT EXISTS RomaniaGB
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    6m varchar(7), 1y varchar(7), 2y varchar(7),
                    3y varchar(7), 4y varchar(7), 5y varchar(7),
                    7y varchar(7), 10y varchar(7), date DATE, year YEAR)
                """
        Yields_DB().create_table(query)
