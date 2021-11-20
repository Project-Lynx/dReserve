from app.models.yields.database import Yields_DB


class Product():
    """Basic representation of a product"""
    def __init__(self, product: str, columns: str = "") -> None:
        self.output: dict = {}
        self.product = product
        self.columns = columns
        self.vals_ph = f'({(str("%s," * len(columns.split(",")))[:-1])})'
        self.x_path_base = "/html/body/div[5]/section/"
        self.collection_query = f"INSERT INTO {product} ({columns}) VALUES {self.vals_ph}"

    def add_to_db_query(self) -> str:
        """Output query to add collected data to db."""
        print(self.columns)
        print(self.vals_ph)
        return self.collection_query

    def rate_to_dict(self, query: list) -> dict:
        """Convert tuple to hashmap"""
        data = Yields_DB().fetch(query)
        for idx in enumerate(data):
            key = str(idx[1][0])
            self.output[key] = idx[1][1]
        return self.output

    def __internals__(self) -> dict:
        """Output internals as dict."""
        return {
            'product': self.product, 'columns': self.columns,
            'value placeholder': self.vals_ph,
        }


class Argentina(Product):
    """Argentina Government Bonds."""
    def __init__(self) -> None:
        columns = "1y,4y,7y,date"
        super().__init__(product="ArgentinaGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '1 Year': idx[1][0], '4 Year': idx[1][1], '7 Year': idx[1][2],
            }
        print(self.output)
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[1]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[1]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[1]/tbody/tr[3]/td[3]"]

    def create_table(self) -> None:
        """Create table for Argentina Gov Bonds in DB."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    1y varchar(7), 4y varchar(7), 7y varchar(7),
                    date DATE, year YEAR)
                 """
        Yields_DB().create_table(query)


class Australia(Product):
    """Australia Government Bonds."""
    def __init__(self) -> None:
        columns = "1y,2y,3y,4y,5y,6y,7y,8y,9y,10y,12y,15y,20y,30y,date"
        super().__init__(product="AustraliaGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '1 Year': idx[1][0], '2 Year': idx[1][1], '3 Year': idx[1][2],
                '4 Year': idx[1][3], '5 Year': idx[1][4], '6 Year': idx[1][5],
                '7 Year': idx[1][6], '8 Year': idx[1][7], '9 Year': idx[1][8],
                '10 Year': idx[1][9], '12 Year': idx[1][10], '15 Year': idx[1][11],
                '20 Year': idx[1][12], '30 Year': idx[1][13],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[2]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[2]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[2]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[2]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[2]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[2]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[2]/tbody/tr[7]/td[3]",
                f"{self.x_path_base}table[2]/tbody/tr[8]/td[3]",
                f"{self.x_path_base}table[2]/tbody/tr[9]/td[3]",
                f"{self.x_path_base}table[2]/tbody/tr[10]/td[3]",
                f"{self.x_path_base}table[2]/tbody/tr[11]/td[3]",
                f"{self.x_path_base}table[2]/tbody/tr[12]/td[3]",
                f"{self.x_path_base}table[2]/tbody/tr[13]/td[3]",
                f"{self.x_path_base}table[2]/tbody/tr[14]/td[3]"]

    def create_table(self) -> None:
        """Create table for Australia Gov Bonds in DB."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
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
    def __init__(self) -> None:
        columns = "1y,2y,3y,4y,5y,6y,7y,8y,9y,10y,15y,20y,25y,30y,40y,date"
        super().__init__(product="AustriaGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '1 Year': idx[1][0], '2 Year': idx[1][1], '3 Year': idx[1][2],
                '4 Year': idx[1][3], '5 Year': idx[1][4], '6 Year': idx[1][5],
                '7 Year': idx[1][6], '8 Year': idx[1][7], '9 Year': idx[1][8],
                '10 Year': idx[1][9], '15 Year': idx[1][10], '20 Year': idx[1][11],
                '25 Year': idx[1][12], '30 Year': idx[1][13], '40 Year': idx[1][14],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[3]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[3]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[3]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[3]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[3]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[3]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[3]/tbody/tr[7]/td[3]",
                f"{self.x_path_base}table[3]/tbody/tr[8]/td[3]",
                f"{self.x_path_base}table[3]/tbody/tr[9]/td[3]",
                f"{self.x_path_base}table[3]/tbody/tr[10]/td[3]",
                f"{self.x_path_base}table[3]/tbody/tr[11]/td[3]",
                f"{self.x_path_base}table[3]/tbody/tr[12]/td[3]",
                f"{self.x_path_base}table[3]/tbody/tr[13]/td[3]",
                f"{self.x_path_base}table[3]/tbody/tr[14]/td[3]",
                f"{self.x_path_base}table[3]/tbody/tr[15]/td[3]"]

    def create_table(self) -> None:
        """Create table for Austria Gov Bonds in DB."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
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
    def __init__(self) -> None:
        columns = "3m,6m,9m,1y,2y,5y,date"
        super().__init__(product="BahrainGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '3 Month': idx[1][0], '6 Month': idx[1][1], '9 Month': idx[1][2],
                '1 Year': idx[1][3], '2 Year': idx[1][4], '5 Year': idx[1][5],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[4]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[4]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[4]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[4]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[4]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[4]/tbody/tr[6]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    3m varchar(7), 6m varchar(7), 9m varchar(7),
                    1y varchar(7), 2y varchar(7), 5y varchar(7),
                    date DATE, year YEAR)
                 """
        Yields_DB().create_table(query)


class Bangledesh(Product):
    def __init__(self) -> None:
        columns = "3m,6m,1y,2y,5y,10y,15y,20y,date"
        super().__init__(product="BangledeshGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '3 Month': idx[1][0], '6 Month': idx[1][1], '1 Year': idx[1][2],
                '2 Year': idx[1][3], '5 Year': idx[1][4], '10 Year': idx[1][5],
                '15 Year': idx[1][6], '20 Year': idx[1][7],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[5]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[5]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[5]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[5]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[5]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[5]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[5]/tbody/tr[7]/td[3]",
                f"{self.x_path_base}table[5]/tbody/tr[8]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    3m varchar(7), 6m varchar(7), 1y varchar(7),
                    2y varchar(7), 5y varchar(7), 10y varchar(7),
                    15y varchar(7), 20y varchar(7), date DATE,
                    year YEAR)
                 """
        Yields_DB().create_table(query)


class Belgium(Product):
    """Belgium Government Bonds."""
    def __init__(self) -> None:
        columns = "1m,3m,6m,9m,1y,2y,3y,4y,5y,6y,8y,9y,10y,15y,20y,date"
        super().__init__(product="BelgiumGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '1 Month': idx[1][0], '3 Month': idx[1][1], '6 Month': idx[1][2],
                '9 Month': idx[1][3], '1 Year': idx[1][4], '2 Year': idx[1][5],
                '3 Year': idx[1][6], '4 Year': idx[1][7], '5 Year': idx[1][8],
                '6 Year': idx[1][9], '8 Year': idx[1][10], '9 Year': idx[1][11],
                '10 Year': idx[1][12], '15 Year': idx[1][13], '20 Year': idx[1][14],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[6]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[6]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[6]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[6]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[6]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[6]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[6]/tbody/tr[7]/td[3]",
                f"{self.x_path_base}table[6]/tbody/tr[8]/td[3]",
                f"{self.x_path_base}table[6]/tbody/tr[9]/td[3]",
                f"{self.x_path_base}table[6]/tbody/tr[10]/td[3]",
                f"{self.x_path_base}table[6]/tbody/tr[11]/td[3]",
                f"{self.x_path_base}table[6]/tbody/tr[12]/td[3]",
                f"{self.x_path_base}table[6]/tbody/tr[13]/td[3]",
                f"{self.x_path_base}table[6]/tbody/tr[14]/td[3]",
                f"{self.x_path_base}table[6]/tbody/tr[15]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
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
    def __init__(self) -> None:
        columns = "6m,3y,5y,20y,date"
        super().__init__(product="BotswanaGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '6 Month': idx[1][0], '3 Year': idx[1][1], '5 Year': idx[1][2],
                '20 Year': idx[1][3],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[7]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[7]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[7]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[7]/tbody/tr[4]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    6m varchar(7), 3y varchar(7), 5y varchar(7),
                    20y varchar(7), date DATE, year YEAR)
                 """
        Yields_DB().create_table(query)


class Brazil(Product):
    """Brazil Government Bonds."""
    def __init__(self) -> None:
        columns = "3m,6m,9m,1y,2y,3y,5y,8y,10y,date"
        super().__init__(product="BrazilGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '3 Month': idx[1][0], '6 Month': idx[1][1], '9 Month': idx[1][2],
                '1 Year': idx[1][3], '2 Year': idx[1][4], '3 Year': idx[1][5],
                '5 Year': idx[1][6], '8 Year': idx[1][7], '10 Year': idx[1][8],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[8]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[8]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[8]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[8]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[8]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[8]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[8]/tbody/tr[7]/td[3]",
                f"{self.x_path_base}table[8]/tbody/tr[8]/td[3]",
                f"{self.x_path_base}table[8]/tbody/tr[9]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    3m varchar(7), 6m varchar(7), 9m varchar(7),
                    1y varchar(7), 2y varchar(7), 3y varchar(7),
                    5y varchar(7), 8y varchar(7), 10y varchar(7),
                    date DATE, year YEAR)
                 """
        Yields_DB().create_table(query)


class Bulgaria(Product):
    """Bulgaria Government Bonds."""
    def __init__(self) -> None:
        columns = "1m,1y,2y,3y,4y,5y,7y,10y,date"
        super().__init__(product="BulgariaGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '1 Month': idx[1][0], '1 Year': idx[1][1], '2 Year': idx[1][2],
                '3 Year': idx[1][3], '4 Year': idx[1][4], '5 Year': idx[1][5],
                '7 Year': idx[1][6], '10 Year': idx[1][7],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[9]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[9]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[9]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[9]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[9]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[9]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[9]/tbody/tr[7]/td[3]",
                f"{self.x_path_base}table[9]/tbody/tr[8]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    1m varchar(7), 1y varchar(7), 2y varchar(7),
                    3y varchar(7), 4y varchar(7), 5y varchar(7),
                    7y varchar(7), 10y varchar(7), date DATE,
                    year YEAR)
                 """
        Yields_DB().create_table(query)


class Canada(Product):
    """Canadian Government Bonds."""
    def __init__(self) -> None:
        columns = "1m,2m,3m,6m,1y,2y,3y,4y,5y,7y,10y,20y,30y,date"
        super().__init__(product="CanadaGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '1 Month': idx[1][0], '2 Month': idx[1][1], '3 Month': idx[1][2],
                '6 Month': idx[1][3], '1 Year': idx[1][4], '2 Year': idx[1][5],
                '3 Year': idx[1][6], '4 Year': idx[1][7], '5 Year': idx[1][8],
                '7 Year': idx[1][9], '10 Year': idx[1][10], '20 Year': idx[1][11],
                '30 Year': idx[1][12],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[10]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[10]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[10]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[10]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[10]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[10]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[10]/tbody/tr[7]/td[3]",
                f"{self.x_path_base}table[10]/tbody/tr[8]/td[3]",
                f"{self.x_path_base}table[10]/tbody/tr[9]/td[3]",
                f"{self.x_path_base}table[10]/tbody/tr[10]/td[3]",
                f"{self.x_path_base}table[10]/tbody/tr[11]/td[3]",
                f"{self.x_path_base}table[10]/tbody/tr[12]/td[3]",
                f"{self.x_path_base}table[10]/tbody/tr[13]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
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
    def __init__(self) -> None:
        columns = "1y,2y,3y,4y,5y,8y,10y,date"
        super().__init__(product="ChileGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '1 Year': idx[1][0], '2 Year': idx[1][1], '3 Year': idx[1][2],
                '4 Year': idx[1][3], '5 Year': idx[1][4], '8 Year': idx[1][5],
                '10 Year': idx[1][6],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[11]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[11]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[11]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[11]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[11]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[11]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[11]/tbody/tr[7]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    1y varchar(7), 2y varchar(7), 3y varchar(7),
                    4y varchar(7), 5y varchar(7), 8y varchar(7),
                    10y varchar(7), date DATE, year YEAR)
                """
        Yields_DB().create_table(query)


class China(Product):
    """Chinese Government Bonds."""
    def __init__(self) -> None:
        columns = "1y,2y,3y,5y,7y,10y,15y,20y,30y,date"
        super().__init__(product="ChinaGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '1 Year': idx[1][0], '2 Year': idx[1][1], '3 Year': idx[1][2],
                '5 Year': idx[1][3], '7 Year': idx[1][4], '10 Year': idx[1][5],
                '15 Year': idx[1][6], '20 Year': idx[1][7], '30 Year': idx[1][8],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[12]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[12]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[12]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[12]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[12]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[12]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[12]/tbody/tr[7]/td[3]",
                f"{self.x_path_base}table[12]/tbody/tr[8]/td[3]",
                f"{self.x_path_base}table[12]/tbody/tr[9]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    1y varchar(7), 2y varchar(7), 3y varchar(7),
                    5y varchar(7), 7y varchar(7), 10y varchar(7),
                    15y varchar(7), 20y varchar(7), 30y varchar(7),
                    date DATE, year YEAR)
                 """
        Yields_DB().create_table(query)


class Colombia(Product):
    """Colombian Government Bonds."""
    def __init__(self) -> None:
        columns = "1y,4y,5y,10y,15y,date"
        super().__init__(product="ColombiaGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '1 Year': idx[1][0], '4 Year': idx[1][1], '5 Year': idx[1][2],
                '10 Year': idx[1][3], '15 Year': idx[1][4],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[13]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[13]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[13]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[13]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[13]/tbody/tr[5]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    1y varchar(7), 4y varchar(7), 5y varchar(7),
                    10y varchar(7), 15y varchar(7), date DATE,
                    year YEAR)
                 """
        Yields_DB().create_table(query)


class Crotia(Product):
    """Croatian Government Bonds."""
    def __init__(self) -> None:
        columns = "1y,3y,5y,10y,date"
        super().__init__(product="CroatiaGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '1 Year': idx[1][0], '3 Year': idx[1][1], '5 Year': idx[1][2],
                '10 Year': idx[1][3],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[14]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[14]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[14]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[14]/tbody/tr[4]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    1y varchar(7), 3y varchar(7), 5y varchar(7),
                    10y varchar(7), date DATE, year YEAR)
                 """
        Yields_DB().create_table(query)


class Cyprus(Product):
    """Cyprus Government Bonds."""
    def __init__(self) -> None:
        columns = "1y,3y,5y,7y,10y,date"
        super().__init__(product="CyprusGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '2 Year': idx[1][0], '3 Year': idx[1][1], '5 Year': idx[1][2],
                '7 Year': idx[1][3], '10 Year': idx[1][4],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[15]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[15]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[15]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[15]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[15]/tbody/tr[5]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    1y varchar(7), 3y varchar(7), 5y varchar(7),
                    7y varchar(7), 10y varchar(7), date DATE,
                    year YEAR)
                 """
        Yields_DB().create_table(query)


class Czech_Republic(Product):
    """Czech Republic Government Bonds."""
    def __init__(self) -> None:
        columns = "1y,2y,3y,4y,5y,6y,7y,8y,9y,10y,15y,20y,50y,date"
        super().__init__(product="CzechRepublicGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '1 Year': idx[1][0], '2 Year': idx[1][1], '3 Year': idx[1][2],
                '4 Year': idx[1][3], '5 Year': idx[1][4], '6 Year': idx[1][5],
                '7 Year': idx[1][6], '8 Year': idx[1][7], '9 Year': idx[1][8],
                '10 Year': idx[1][9], '15 Year': idx[1][10], '20 Year': idx[1][11],
                '50 Year': idx[1][12],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[16]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[16]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[16]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[16]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[16]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[16]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[16]/tbody/tr[7]/td[3]",
                f"{self.x_path_base}table[16]/tbody/tr[8]/td[3]",
                f"{self.x_path_base}table[16]/tbody/tr[9]/td[3]",
                f"{self.x_path_base}table[16]/tbody/tr[10]/td[3]",
                f"{self.x_path_base}table[16]/tbody/tr[11]/td[3]",
                f"{self.x_path_base}table[16]/tbody/tr[12]/td[3]",
                f"{self.x_path_base}table[16]/tbody/tr[13]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
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
    def __init__(self) -> None:
        columns = "24h,3m,6m,9m,1y,2y,3y,5y,7y,10y,date"
        super().__init__(product="EgyptGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '24h': idx[1][0], '3 Month': idx[1][1], '6 Month': idx[1][2],
                '9 Month': idx[1][3], '1 Year': idx[1][4], '2 Year': idx[1][5],
                '3 Year': idx[1][6], '5 Year': idx[1][7], '7 Year': idx[1][8],
                '10 Year': idx[1][9],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[17]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[17]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[17]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[17]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[17]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[17]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[17]/tbody/tr[7]/td[3]",
                f"{self.x_path_base}table[17]/tbody/tr[8]/td[3]",
                f"{self.x_path_base}table[17]/tbody/tr[9]/td[3]",
                f"{self.x_path_base}table[17]/tbody/tr[10]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    24h varchar(7), 3m varchar(7), 6m varchar(7),
                    9m varchar(7), 1y varchar(7), 2y varchar(7),
                    3y varchar(7), 5y varchar(7), 7y varchar(7),
                    10y varchar(7), date DATE, year YEAR)
                 """
        Yields_DB().create_table(query)


class France(Product):
    """French Government Bonds."""
    def __init__(self) -> None:
        columns = "1m,3m,6m,9m,1y,2y,3y,4y,5y,6y,7y,8y,9y,10y,15y,20y,25y,30y,50y,date"
        super().__init__(product="FranceGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
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

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[18]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[18]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[18]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[18]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[18]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[18]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[18]/tbody/tr[7]/td[3]",
                f"{self.x_path_base}table[18]/tbody/tr[8]/td[3]",
                f"{self.x_path_base}table[18]/tbody/tr[9]/td[3]",
                f"{self.x_path_base}table[18]/tbody/tr[10]/td[3]",
                f"{self.x_path_base}table[18]/tbody/tr[11]/td[3]",
                f"{self.x_path_base}table[18]/tbody/tr[12]/td[3]",
                f"{self.x_path_base}table[18]/tbody/tr[13]/td[3]",
                f"{self.x_path_base}table[18]/tbody/tr[14]/td[3]",
                f"{self.x_path_base}table[18]/tbody/tr[15]/td[3]",
                f"{self.x_path_base}table[18]/tbody/tr[16]/td[3]",
                f"{self.x_path_base}table[18]/tbody/tr[17]/td[3]",
                f"{self.x_path_base}table[18]/tbody/tr[18]/td[3]",
                f"{self.x_path_base}table[18]/tbody/tr[19]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
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
    def __init__(self) -> None:
        columns = "3m,6m,9m,1y,2y,3y,4y,5y,6y,7y,8y,9y,10y,15y,20y,25y,30y,date"
        super().__init__(product="GermanyGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '3 Month': idx[1][0], '6 Month': idx[1][1], '9 Month': idx[1][2],
                '1 Year': idx[1][3], '2 Year': idx[1][4], '3 Year': idx[1][5],
                '4 Year': idx[1][6], '5 Year': idx[1][7], '6 Year': idx[1][8],
                '7 Year': idx[1][9], '8 Year': idx[1][10], '9 Year': idx[1][11],
                '10 Year': idx[1][12], '15 Year': idx[1][13], '20 Year': idx[1][14],
                '25 Year': idx[1][15], '30 Year': idx[1][16],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[19]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[19]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[19]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[19]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[19]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[19]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[19]/tbody/tr[7]/td[3]",
                f"{self.x_path_base}table[19]/tbody/tr[8]/td[3]",
                f"{self.x_path_base}table[19]/tbody/tr[9]/td[3]",
                f"{self.x_path_base}table[19]/tbody/tr[10]/td[3]",
                f"{self.x_path_base}table[19]/tbody/tr[11]/td[3]",
                f"{self.x_path_base}table[19]/tbody/tr[12]/td[3]",
                f"{self.x_path_base}table[19]/tbody/tr[13]/td[3]",
                f"{self.x_path_base}table[19]/tbody/tr[14]/td[3]",
                f"{self.x_path_base}table[19]/tbody/tr[15]/td[3]",
                f"{self.x_path_base}table[19]/tbody/tr[16]/td[3]",
                f"{self.x_path_base}table[19]/tbody/tr[17]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
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
    def __init__(self) -> None:
        columns = "1m,3m,6m,5y,10y,15y,20y,25y,date"
        super().__init__(product="GreeceGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '1 Month': idx[1][0], '3 Month': idx[1][1], '6 Month': idx[1][2],
                '5 Year': idx[1][3], '10 Year': idx[1][4], '15 Year': idx[1][5],
                '20 Year': idx[1][6], '25 Year': idx[1][7],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[20]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[20]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[20]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[20]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[20]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[20]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[20]/tbody/tr[7]/td[3]",
                f"{self.x_path_base}table[20]/tbody/tr[8]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    1m varchar(7), 3m varchar(7), 6m varchar(7),
                    5y varchar(7), 10y varchar(7), 15y varchar(7),
                    20y varchar(7), 25y varchar(7), date DATE, year YEAR)
                 """
        Yields_DB().create_table(query)


class Hong_Kong(Product):
    """Hong Kong Government Bonds."""
    def __init__(self) -> None:
        columns = "1w,1m,3m,6m,9m,1y,2y,3y,5y,7y,10y,15y,date"
        super().__init__(product="HongKongGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '1 Week': idx[1][0], '1 Month': idx[1][1], '3 Month': idx[1][2],
                '6 Month': idx[1][3], '9 Month': idx[1][4], '1 Year': idx[1][5],
                '2 Year': idx[1][6], '3 Year': idx[1][7], '5 Year': idx[1][8],
                '7 Year': idx[1][9], '10 Year': idx[1][10], '15 Year': idx[1][11],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[21]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[21]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[21]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[21]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[21]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[21]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[21]/tbody/tr[7]/td[3]",
                f"{self.x_path_base}table[21]/tbody/tr[8]/td[3]",
                f"{self.x_path_base}table[21]/tbody/tr[9]/td[3]",
                f"{self.x_path_base}table[21]/tbody/tr[10]/td[3]",
                f"{self.x_path_base}table[21]/tbody/tr[11]/td[3]",
                f"{self.x_path_base}table[21]/tbody/tr[12]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    1w varchar(7), 1m varchar(7), 3m varchar(7),
                    6m varchar(7), 9m varchar(7), 1y varchar(7),
                    2y varchar(7), 3y varchar(7), 5y varchar(7),
                    7y varchar(7), 10y varchar(7), 15y varchar(7),
                    date DATE, year YEAR)
                 """
        Yields_DB().create_table(query)


class Hungary(Product):
    """Hungarian Government Bonds."""
    def __init__(self) -> None:
        columns = "3m,6m,1y,3y,5y,10y,15y,date"
        super().__init__(product="HungaryGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '3 Month': idx[1][0], '6 Month': idx[1][1], '1 Year': idx[1][2],
                '3 year': idx[1][3], '5 Year': idx[1][4], '10 Year': idx[1][5],
                '15 Year': idx[1][6],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[22]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[22]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[22]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[22]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[22]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[22]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[22]/tbody/tr[7]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    3m varchar(7), 6m varchar(7), 1y varchar(7),
                    3y varchar(7), 5y varchar(7), 10y varchar(7),
                    15y varchar(7), date DATE, year YEAR)
                 """
        Yields_DB().create_table(query)


class Iceland(Product):
    """Iceland Government Bonds."""
    def __init__(self) -> None:
        columns = "2y,5y,10y,date"
        super().__init__(product="IcelandGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '2 Year': idx[1][0], '5 Year': idx[1][1], '10 Year': idx[1][2],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[23]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[23]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[23]/tbody/tr[3]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    2y varchar(7), 5y varchar(7), 10y varchar(7),
                    date DATE, year YEAR)
                 """
        Yields_DB().create_table(query)


class India(Product):
    """India Government Bonds."""
    def __init__(self) -> None:
        columns = columns = "3m,6m,1y,2y,3y,4y,5y,6y,7y,8y,9y,10y,11y,12y,13y,14y,15y,19y,24y,30y,date"
        super().__init__(product="IndiaGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
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

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[24]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[24]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[24]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[24]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[24]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[24]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[24]/tbody/tr[7]/td[3]",
                f"{self.x_path_base}table[24]/tbody/tr[8]/td[3]",
                f"{self.x_path_base}table[24]/tbody/tr[9]/td[3]",
                f"{self.x_path_base}table[24]/tbody/tr[10]/td[3]",
                f"{self.x_path_base}table[24]/tbody/tr[11]/td[3]",
                f"{self.x_path_base}table[24]/tbody/tr[12]/td[3]",
                f"{self.x_path_base}table[24]/tbody/tr[13]/td[3]",
                f"{self.x_path_base}table[24]/tbody/tr[14]/td[3]",
                f"{self.x_path_base}table[24]/tbody/tr[15]/td[3]",
                f"{self.x_path_base}table[24]/tbody/tr[16]/td[3]",
                f"{self.x_path_base}table[24]/tbody/tr[17]/td[3]",
                f"{self.x_path_base}table[24]/tbody/tr[18]/td[3]",
                f"{self.x_path_base}table[24]/tbody/tr[19]/td[3]",
                f"{self.x_path_base}table[24]/tbody/tr[20]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
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
    def __init__(self) -> None:
        columns = "1m,3m,6m,1y,3y,5y,10y,15y,20y,25y,30y,date"
        super().__init__(product="IndonesiaGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '1 Month': idx[1][0], '3 Month': idx[1][1], '6 Month': idx[1][2],
                '1 Year': idx[1][3], '3 Year': idx[1][4], '5 Year': idx[1][5],
                '10 Year': idx[1][6], '15 Year': idx[1][7], '20 Year': idx[1][8],
                '25 Year': idx[1][9], '30 Year': idx[1][10],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[25]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[25]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[25]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[25]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[25]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[25]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[25]/tbody/tr[7]/td[3]",
                f"{self.x_path_base}table[25]/tbody/tr[8]/td[3]",
                f"{self.x_path_base}table[25]/tbody/tr[9]/td[3]",
                f"{self.x_path_base}table[25]/tbody/tr[10]/td[3]",
                f"{self.x_path_base}table[25]/tbody/tr[11]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    1m varchar(7), 3m varchar(7), 6m varchar(7),
                    1y varchar(7), 3y varchar(7), 5y varchar(7),
                    10y varchar(7), 15y varchar(7), 20y varchar(7),
                    25y varchar(7), 30y varchar(7), date DATE, year YEAR)
                 """
        Yields_DB().create_table(query)


class Ireland(Product):
    """Ireland Government Bonds."""
    def __init__(self) -> None:
        columns = "3m,6m,1y,3y,4y,5y,6y,7y,8y,10y,15y,20y,30y,date"
        super().__init__(product="IrelandGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '3 Month': idx[1][0], '6 Month': idx[1][1], '1 Year': idx[1][2],
                '3 Year': idx[1][3], '4 Year': idx[1][4], '5 Year': idx[1][5],
                '6 Year': idx[1][6], '7 Year': idx[1][7], '8 Year': idx[1][8],
                '10 Year': idx[1][9], '15 Year': idx[1][10], '20 Year': idx[1][11],
                '30 Year': idx[1][12],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[26]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[26]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[26]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[26]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[26]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[26]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[26]/tbody/tr[7]/td[3]",
                f"{self.x_path_base}table[26]/tbody/tr[8]/td[3]",
                f"{self.x_path_base}table[26]/tbody/tr[9]/td[3]",
                f"{self.x_path_base}table[26]/tbody/tr[10]/td[3]",
                f"{self.x_path_base}table[26]/tbody/tr[11]/td[3]",
                f"{self.x_path_base}table[26]/tbody/tr[12]/td[3]",
                f"{self.x_path_base}table[26]/tbody/tr[13]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
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
    def __init__(self) -> None:
        table = "IsraelGB"
        columns = "1m,3m,6m,9m,1y,2y,3y,5y,10y,30y,date"
        super().__init__(product=table, columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '1 Month': idx[1][0], '3 Month': idx[1][1], '6 Month': idx[1][2],
                '9 Month': idx[1][3], '1 Year': idx[1][4], '2 Year': idx[1][5],
                '3 Year': idx[1][6], '5 Year': idx[1][7], '10 Year': idx[1][8],
                '30 Year': idx[1][9],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[27]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[27]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[27]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[27]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[27]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[27]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[27]/tbody/tr[7]/td[3]",
                f"{self.x_path_base}table[27]/tbody/tr[8]/td[3]",
                f"{self.x_path_base}table[27]/tbody/tr[9]/td[3]",
                f"{self.x_path_base}table[27]/tbody/tr[10]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    1m varchar(7), 3m varchar(7), 6m varchar(7),
                    9m varchar(7), 1y varchar(7), 2y varchar(7),
                    3y varchar(7), 5y varchar(7), 10y varchar(7),
                    30y varchar(7), date DATE, year YEAR)
                 """
        Yields_DB().create_table(query)


class Italy(Product):
    """Italian Government Bonds."""
    def __init__(self) -> None:
        table = "ItalyGB"
        columns = "1m,3m,6m,9m,1y,2y,3y,4y,5y,6y,7y,8y,9y,10y,15y,20y,30y,50y,date"
        super().__init__(product=table, columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '1 Month': idx[1][0], '3 Month': idx[1][1], '6 Month': idx[1][2],
                '9 Month': idx[1][3], '1 Year': idx[1][4], '2 Year': idx[1][5],
                '3 Year': idx[1][6], '4 Year': idx[1][7], '5 Year': idx[1][8],
                '6 Year': idx[1][9], '7 Year': idx[1][10], '8 Year': idx[1][11],
                '9 Year': idx[1][12], '10 Year': idx[1][13], '15 Year': idx[1][14],
                '20 Year': idx[1][15], '30 Year': idx[1][16], '50 Year': idx[1][17],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[28]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[28]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[28]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[28]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[28]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[28]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[28]/tbody/tr[7]/td[3]",
                f"{self.x_path_base}table[28]/tbody/tr[8]/td[3]",
                f"{self.x_path_base}table[28]/tbody/tr[9]/td[3]",
                f"{self.x_path_base}table[28]/tbody/tr[10]/td[3]",
                f"{self.x_path_base}table[28]/tbody/tr[11]/td[3]",
                f"{self.x_path_base}table[28]/tbody/tr[12]/td[3]",
                f"{self.x_path_base}table[28]/tbody/tr[13]/td[3]",
                f"{self.x_path_base}table[28]/tbody/tr[14]/td[3]",
                f"{self.x_path_base}table[28]/tbody/tr[15]/td[3]",
                f"{self.x_path_base}table[28]/tbody/tr[16]/td[3]",
                f"{self.x_path_base}table[28]/tbody/tr[17]/td[3]",
                f"{self.x_path_base}table[28]/tbody/tr[18]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
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
    def __init__(self) -> None:
        columns = "1m,3m,6m,9m,1y,2y,3y,4y,5y,6y,7y,8y,9y,10y,15y,20y,30y,40y,date"
        super().__init__(product="JapanGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '1 Month': idx[1][0], '3 Month': idx[1][1], '6 Month': idx[1][2],
                '9 Month': idx[1][3], '1 Year': idx[1][4], '2 Year': idx[1][5],
                '3 Year': idx[1][6], '4 Year': idx[1][7], '5 Year': idx[1][8],
                '6 Year': idx[1][9], '7 Year': idx[1][10], '8 Year': idx[1][11],
                '9 Year': idx[1][12], '10 Year': idx[1][13], '15 Year': idx[1][14],
                '20 Year': idx[1][15], '30 Year': idx[1][16], '40 Year': idx[1][17],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[29]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[29]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[29]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[29]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[29]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[29]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[29]/tbody/tr[7]/td[3]",
                f"{self.x_path_base}table[29]/tbody/tr[8]/td[3]",
                f"{self.x_path_base}table[29]/tbody/tr[9]/td[3]",
                f"{self.x_path_base}table[29]/tbody/tr[10]/td[3]",
                f"{self.x_path_base}table[29]/tbody/tr[11]/td[3]",
                f"{self.x_path_base}table[29]/tbody/tr[12]/td[3]",
                f"{self.x_path_base}table[29]/tbody/tr[13]/td[3]",
                f"{self.x_path_base}table[29]/tbody/tr[14]/td[3]",
                f"{self.x_path_base}table[29]/tbody/tr[15]/td[3]",
                f"{self.x_path_base}table[29]/tbody/tr[16]/td[3]",
                f"{self.x_path_base}table[29]/tbody/tr[17]/td[3]",
                f"{self.x_path_base}table[29]/tbody/tr[18]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
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
    def __init__(self) -> None:
        columns = "3m,6m,1y,2y,3y,5y,7y,10y,date"
        super().__init__(product="JordanGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '3 Month': idx[1][0], '6 Month': idx[1][1], '1 Year': idx[1][2],
                '2 Year': idx[1][3], '3 Year': idx[1][4], '5 Year': idx[1][5],
                '7 Year': idx[1][6], '10 Year': idx[1][7],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[30]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[30]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[30]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[30]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[30]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[30]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[30]/tbody/tr[7]/td[3]",
                f"{self.x_path_base}table[30]/tbody/tr[8]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = """CREATE TABLE IF NOT EXISTS JordanGB
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    3m varchar(7), 6m varchar(7), 1y varchar(7),
                    2y varchar(7), 3y varchar(7), 5y varchar(7),
                    7y varchar(7), 10y varchar(7), date DATE, year YEAR)
                """
        Yields_DB().create_table(query)


class Kazakhstan(Product):
    """Kazakhstan Government Bonds."""
    def __init__(self) -> None:
        columns = "1y,2y,3y,4y,5y,6y,7y,8y,9y,10y,15y,25y,date"
        super().__init__(product="KazakhstanGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '1 Year': idx[1][0], '2 Year': idx[1][1], '3 Year': idx[1][2],
                '4 Year': idx[1][3], '5 Year': idx[1][4], '6 Year': idx[1][5],
                '7 Year': idx[1][6], '8 Year': idx[1][7], '9 Year': idx[1][8],
                '10 Year': idx[1][9], '15 Year': idx[1][10], '25 Year': idx[1][11],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[31]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[31]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[31]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[31]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[31]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[31]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[31]/tbody/tr[7]/td[3]",
                f"{self.x_path_base}table[31]/tbody/tr[8]/td[3]",
                f"{self.x_path_base}table[31]/tbody/tr[9]/td[3]",
                f"{self.x_path_base}table[31]/tbody/tr[10]/td[3]",
                f"{self.x_path_base}table[31]/tbody/tr[11]/td[3]",
                f"{self.x_path_base}table[31]/tbody/tr[12]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    1y varchar(7), 2y varchar(7), 3y varchar(7),
                    4y varchar(7), 5y varchar(7), 6y varchar(7),
                    7y varchar(7), 8y varchar(7), 9y varchar(7),
                    10y varchar(7), 15y varchar(7), 25y varchar(7),
                    date DATE, year YEAR)
                """
        Yields_DB().create_table(query)


class Kenya(Product):
    """Kenya Government Bonds."""
    def __init__(self) -> None:
        columns = "24h,3m,6m,1y,2y,3y,4y,5y,6y,7y,8y,9y,10y,15y,20y,25y,date"
        super().__init__(product="KenyaGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                'Overnight': idx[1][0], '3 Month': idx[1][1], '6 Month': idx[1][2],
                '1 Year': idx[1][3], '2 Year': idx[1][4], '3 Year': idx[1][5],
                '4 Year': idx[1][6], '5 Year': idx[1][7], '6 Year': idx[1][8],
                '7 Year': idx[1][9], '8 Year': idx[1][10], '9 Year': idx[1][11],
                '10 Year': idx[1][12], '15 Year': idx[1][13], '20 Year': idx[1][14],
                '25 Year': idx[1][15],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[32]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[32]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[32]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[32]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[32]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[32]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[32]/tbody/tr[7]/td[3]",
                f"{self.x_path_base}table[32]/tbody/tr[8]/td[3]",
                f"{self.x_path_base}table[32]/tbody/tr[9]/td[3]",
                f"{self.x_path_base}table[32]/tbody/tr[10]/td[3]",
                f"{self.x_path_base}table[32]/tbody/tr[11]/td[3]",
                f"{self.x_path_base}table[32]/tbody/tr[12]/td[3]",
                f"{self.x_path_base}table[32]/tbody/tr[13]/td[3]",
                f"{self.x_path_base}table[32]/tbody/tr[14]/td[3]",
                f"{self.x_path_base}table[32]/tbody/tr[15]/td[3]",
                f"{self.x_path_base}table[32]/tbody/tr[16]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    24h varchar(7), 3m varchar(7), 6m varchar(7),
                    1y varchar(7), 2y varchar(7), 3y varchar(7),
                    4y varchar(7), 5y varchar(7), 6y varchar(7),
                    7y varchar(7), 8y varchar(7), 9y varchar(7),
                    10y varchar(7), 15y varchar(7), 20y varchar(7),
                    25y varchar(7), date DATE, year YEAR)
                 """
        Yields_DB().create_table(query)


class Malaysia(Product):
    """Malaysian Government Bonds."""
    def __init__(self) -> None:
        columns = "3w,3m,7m,1y,3y,5y,7y,10y,15y,20y,30y,date"
        super().__init__(product="MalaysiaGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '3 Week': idx[1][0], '3 Month': idx[1][1], '7 Month': idx[1][2],
                '1 Year': idx[1][3], '3 Year': idx[1][4], '5 Year': idx[1][5],
                '7 Year': idx[1][6], '10 Year': idx[1][7], '15 Year': idx[1][8],
                '20 Year': idx[1][9], '30 Year': idx[1][10],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[33]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[33]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[33]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[33]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[33]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[33]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[33]/tbody/tr[7]/td[3]",
                f"{self.x_path_base}table[33]/tbody/tr[8]/td[3]",
                f"{self.x_path_base}table[33]/tbody/tr[9]/td[3]",
                f"{self.x_path_base}table[33]/tbody/tr[10]/td[3]",
                f"{self.x_path_base}table[33]/tbody/tr[11]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    3w varchar(7), 3m varchar(7), 7m varchar(7),
                    1y varchar(7), 3y varchar(7), 5y varchar(7),
                    7y varchar(7), 10y varchar(7), 15y varchar(7),
                    20y varchar(7), 30y varchar(7), date DATE, year YEAR)
                 """
        Yields_DB().create_table(query)


class Malta(Product):
    """Malta Government Bonds."""
    def __init__(self) -> None:
        columns = "1m,3m,6m,1y,3y,5y,10y,20y,25y,date"
        super().__init__(product="MaltaGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '1 Month': idx[1][0], '3 Month': idx[1][1], '6 Month': idx[1][2],
                '1 Year': idx[1][3], '3 Year': idx[1][4], '5 Year': idx[1][5],
                '10 Year': idx[1][6], '20 Year': idx[1][7], '25 Year': idx[1][8],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[34]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[34]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[34]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[34]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[34]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[34]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[34]/tbody/tr[7]/td[3]",
                f"{self.x_path_base}table[34]/tbody/tr[8]/td[3]",
                f"{self.x_path_base}table[34]/tbody/tr[9]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    1m varchar(7), 3m varchar(7), 6m varchar(7),
                    1y varchar(7), 3y varchar(7), 5y varchar(7),
                    10y varchar(7), 20y varchar(7), 25y varchar(7),
                    date DATE, year YEAR)
                 """
        Yields_DB().create_table(query)


class Mauritius(Product):
    """Mauritius Government Bonds."""
    def __init__(self) -> None:
        columns = "2m,4m,6m,8m,1y,2y,3y,4y,5y,10y,15y,20y,date"
        super().__init__(product="MauritiusGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '2 Month': idx[1][0], '4 Month': idx[1][1], '6 Month': idx[1][2],
                '8 Month': idx[1][3], '1 Year': idx[1][4], '2 Year': idx[1][5],
                '3 Year': idx[1][6], '4 Year': idx[1][7], '5 Year': idx[1][8],
                '10 Year': idx[1][9], '15 Year': idx[1][10], '20 Year': idx[1][11],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[35]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[35]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[35]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[35]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[35]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[35]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[35]/tbody/tr[7]/td[3]",
                f"{self.x_path_base}table[35]/tbody/tr[8]/td[3]",
                f"{self.x_path_base}table[35]/tbody/tr[9]/td[3]",
                f"{self.x_path_base}table[35]/tbody/tr[10]/td[3]",
                f"{self.x_path_base}table[35]/tbody/tr[11]/td[3]",
                f"{self.x_path_base}table[35]/tbody/tr[12]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
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
    def __init__(self) -> None:
        columns = "1m,3m,6m,9m,1y,3y,5y,7y,10y,15y,20y,30y,date"
        super().__init__(product="MexicoGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '1 Month': idx[1][0], '3 Month': idx[1][1], '6 Month': idx[1][2],
                '9 Month': idx[1][3], '1 Year': idx[1][4], '3 Year': idx[1][5],
                '5 Year': idx[1][6], '7 Year': idx[1][7], '10 Year': idx[1][8],
                '15 Year': idx[1][9], '20 Year': idx[1][10], '30 Year': idx[1][11],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[36]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[36]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[36]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[36]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[36]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[36]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[36]/tbody/tr[7]/td[3]",
                f"{self.x_path_base}table[36]/tbody/tr[8]/td[3]",
                f"{self.x_path_base}table[36]/tbody/tr[9]/td[3]",
                f"{self.x_path_base}table[36]/tbody/tr[10]/td[3]",
                f"{self.x_path_base}table[36]/tbody/tr[11]/td[3]",
                f"{self.x_path_base}table[36]/tbody/tr[12]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
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
    def __init__(self) -> None:
        columns = "3m,6m,2y,5y,10y,15y,date"
        super().__init__(product="MoroccoGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '3 Month': idx[1][0], '6 Month': idx[1][1], '2 Year': idx[1][2],
                '5 Year': idx[1][3], '10 Year': idx[1][4], '15 Year': idx[1][5],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[37]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[37]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[37]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[37]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[37]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[37]/tbody/tr[6]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    3m varchar(7), 6m varchar(7), 2y varchar(7),
                    5y varchar(7), 10y varchar(7), 15y varchar(7),
                    date DATE, year YEAR)
                 """
        Yields_DB().create_table(query)


class Namibia(Product):
    """Namibia Government Bonds."""
    def __init__(self) -> None:
        columns = "3m,6m,9m,1y,3y,7y,10y,15y,20y,date"
        super().__init__(product="NamibiaGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '3 Month': idx[1][0], '6 Month': idx[1][1], '9 Month': idx[1][2],
                '1 Year': idx[1][3], '3 Year': idx[1][4], '7 Year': idx[1][5],
                '10 Year': idx[1][6], '15 Year': idx[1][7], '20 Year': idx[1][8],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[38]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[38]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[38]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[38]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[38]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[38]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[38]/tbody/tr[7]/td[3]",
                f"{self.x_path_base}table[38]/tbody/tr[8]/td[3]",
                f"{self.x_path_base}table[38]/tbody/tr[9]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    3m varchar(7), 6m varchar(7), 9m varchar(7),
                    1y varchar(7), 3y varchar(7), 7y varchar(7),
                    10y varchar(7), 15y varchar(7), 20y varchar(7),
                    date DATE, year YEAR)
                 """
        Yields_DB().create_table(query)


class Netherlands(Product):
    """Netherlands Government Bonds."""
    def __init__(self) -> None:
        columns = "1m,3m,6m,2y,3y,4y,5y,6y,7y,8y,9y,10y,15y,20y,25y,30y,date"
        super().__init__(product="NetherlandsGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '1 Month': idx[1][0], '3 Month': idx[1][1], '6 Month': idx[1][2],
                '2 Year': idx[1][3], '3 Year': idx[1][4], '4 Year': idx[1][5],
                '5 Year': idx[1][6], '6 Year': idx[1][7], '7 Year': idx[1][8],
                '8 Year': idx[1][9], '9 Year': idx[1][10], '10 Year': idx[1][11],
                '15 Year': idx[1][12], '20 Year': idx[1][13], '25 Year': idx[1][14],
                '30 Year': idx[1][15],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[39]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[39]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[39]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[39]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[39]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[39]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[39]/tbody/tr[7]/td[3]",
                f"{self.x_path_base}table[39]/tbody/tr[8]/td[3]",
                f"{self.x_path_base}table[39]/tbody/tr[9]/td[3]",
                f"{self.x_path_base}table[39]/tbody/tr[10]/td[3]",
                f"{self.x_path_base}table[39]/tbody/tr[11]/td[3]",
                f"{self.x_path_base}table[39]/tbody/tr[12]/td[3]",
                f"{self.x_path_base}table[39]/tbody/tr[13]/td[3]",
                f"{self.x_path_base}table[39]/tbody/tr[14]/td[3]",
                f"{self.x_path_base}table[39]/tbody/tr[15]/td[3]",
                f"{self.x_path_base}table[39]/tbody/tr[16]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    1m varchar(7), 3m varchar(7), 6m varchar(7),
                    2y varchar(7), 3y varchar(7), 4y varchar(7),
                    5y varchar(7), 6y varchar(7), 7y varchar(7),
                    8y varchar(7), 9y varchar(7), 10y varchar(7),
                    15y varchar(7), 20y varchar(7), 25y varchar(7),
                    30y varchar(7), date DATE, year YEAR)
                 """
        Yields_DB().create_table(query)


class New_Zealand(Product):
    """New Zealand Government Bonds."""
    def __init__(self) -> None:
        columns = "1m,2m,3m,4m,5m,6m,2y,5y,7y,10y,15y,20y,date"
        super().__init__(product="NewZealandGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '1 Month': idx[1][0], '2 Month': idx[1][1], '3 Month': idx[1][2],
                '4 Month': idx[1][3], '5 Month': idx[1][4], '6 Month': idx[1][5],
                '2 Year': idx[1][6], '5 Year': idx[1][7], '7 Year': idx[1][8],
                '10 Year': idx[1][9], '15 Year': idx[1][10], '20 Year': idx[1][11],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[40]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[40]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[40]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[40]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[40]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[40]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[40]/tbody/tr[7]/td[3]",
                f"{self.x_path_base}table[40]/tbody/tr[8]/td[3]",
                f"{self.x_path_base}table[40]/tbody/tr[9]/td[3]",
                f"{self.x_path_base}table[40]/tbody/tr[10]/td[3]",
                f"{self.x_path_base}table[40]/tbody/tr[11]/td[3]",
                f"{self.x_path_base}table[40]/tbody/tr[12]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    1m varchar(7), 2m varchar(7), 3m varchar(7),
                    4m varchar(7), 5m varchar(7), 6m varchar(7),
                    2y varchar(7), 5y varchar(7), 7y varchar(7),
                    10y varchar(7), 15y varchar(7), 20y varchar(7),
                    date DATE, year YEAR)
                 """
        Yields_DB().create_table(query)


class Nigeria(Product):
    """Nigerian Government Bonds."""
    def __init__(self) -> None:
        columns = "3m,6m,1y,2y,4y,7y,10y,20y,date"
        super().__init__(product="NigeriaGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '3 Month': idx[1][0], '6 Month': idx[1][1], '1 Year': idx[1][2],
                '2 Year': idx[1][3], '4 Year': idx[1][4], '7 Year': idx[1][5],
                '10 Year': idx[1][6], '20 Year': idx[1][7],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[41]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[41]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[41]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[41]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[41]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[41]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[41]/tbody/tr[7]/td[3]",
                f"{self.x_path_base}table[41]/tbody/tr[8]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    3m varchar(7), 6m varchar(7), 1y varchar(7),
                    2y varchar(7), 4y varchar(7), 7y varchar(7),
                    10y varchar(7), 20y varchar(7), date DATE, year YEAR)
                 """
        Yields_DB().create_table(query)


class Norway(Product):
    """Norway Government Bonds."""
    def __init__(self) -> None:
        columns = "3m,6m,9m,1y,3y,5y,10y,date"
        super().__init__(product="NorwayGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '3 Month': idx[1][0], '6 Month': idx[1][1], '9 Month': idx[1][2],
                '1 Year': idx[1][3], '3 Year': idx[1][4], '5 Year': idx[1][5],
                '10 Year': idx[1][6],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[42]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[42]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[42]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[42]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[42]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[42]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[42]/tbody/tr[7]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    3m varchar(7), 6m varchar(7), 9m varchar(7),
                    1y varchar(7), 3y varchar(7), 5y varchar(7),
                    10y varchar(7), date DATE, year YEAR)
                 """
        Yields_DB().create_table(query)


class Pakistan(Product):
    """Pakistani Government Bonds."""
    def __init__(self) -> None:
        columns = "3m,6m,1y,3y,5y,10y,14y,20y,date"
        super().__init__(product="PakistanGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '3 Month': idx[1][0], '6 Month': idx[1][1], '1 Year': idx[1][2],
                '3 Year': idx[1][3], '5 Year': idx[1][4], '10 Year': idx[1][5],
                '14 Year': idx[1][6], '20 Year': idx[1][7],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[43]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[43]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[43]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[43]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[43]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[43]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[43]/tbody/tr[7]/td[3]",
                f"{self.x_path_base}table[43]/tbody/tr[8]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    3m varchar(7), 6m varchar(7), 1y varchar(7),
                    3y varchar(7), 5y varchar(7), 10y varchar(7),
                    14y varchar(7), 20y varchar(7), date DATE, year YEAR)
                 """
        Yields_DB().create_table(query)


class Peru(Product):
    """Peruvian Government Bonds."""
    def __init__(self) -> None:
        columns = "2y,5y,10y,15y,20y,30y,date"
        super().__init__(product="PeruGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '2 Year': idx[1][0], '5 Year': idx[1][1], '10 Year': idx[1][2],
                '15 Year': idx[1][3], '20 Year': idx[1][4], '30 Year': idx[1][5],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[44]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[44]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[44]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[44]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[44]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[44]/tbody/tr[6]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    2y varchar(7), 5y varchar(7), 10y varchar(7),
                    15y varchar(7), 20y varchar(7), 30y varchar(7),
                    date DATE, year YEAR)
                 """
        Yields_DB().create_table(query)


class Philippines(Product):
    """Philippino Government Bonds."""
    def __init__(self) -> None:
        columns = "1m,3m,6m,1y,2y,3y,4y,5y,7y,10y,20y,date"
        super().__init__(product="PhilippinesGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '1 Month': idx[1][0], '3 Month': idx[1][1], '6 Month': idx[1][2],
                '1 Year': idx[1][3], '2 Year': idx[1][4], '3 Year': idx[1][5],
                '4 Year': idx[1][6], '5 Year': idx[1][7], '7 Year': idx[1][8],
                '10 Year': idx[1][9], '20 Year': idx[1][10],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[45]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[45]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[45]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[45]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[45]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[45]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[45]/tbody/tr[7]/td[3]",
                f"{self.x_path_base}table[45]/tbody/tr[8]/td[3]",
                f"{self.x_path_base}table[45]/tbody/tr[9]/td[3]",
                f"{self.x_path_base}table[45]/tbody/tr[10]/td[3]",
                f"{self.x_path_base}table[45]/tbody/tr[11]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    1m varchar(7), 3m varchar(7), 6m varchar(7),
                    1y varchar(7), 2y varchar(7), 3y varchar(7),
                    4y varchar(7), 5y varchar(7), 7y varchar(7),
                    10y varchar(7), 20y varchar(7), date DATE, year YEAR)
                 """
        Yields_DB().create_table(query)


class Poland(Product):
    """Polish Government Bonds."""
    def __init__(self) -> None:
        columns = "24h,1m,2m,1y,2y,3y,4y,5y,6y,7y,9y,10y,date"
        super().__init__(product="PolandGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                'Overnight': idx[1][0], '1 Month': idx[1][1], '2 Month': idx[1][2],
                '1 Year': idx[1][3], '2 Year': idx[1][4], '3 Year': idx[1][5],
                '4 Year': idx[1][6], '5 Year': idx[1][7], '6 Year': idx[1][8],
                '7 Year': idx[1][9], '9 Year': idx[1][10], '10 Year': idx[1][11],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[46]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[46]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[46]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[46]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[46]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[46]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[46]/tbody/tr[7]/td[3]",
                f"{self.x_path_base}table[46]/tbody/tr[8]/td[3]",
                f"{self.x_path_base}table[46]/tbody/tr[9]/td[3]",
                f"{self.x_path_base}table[46]/tbody/tr[10]/td[3]",
                f"{self.x_path_base}table[46]/tbody/tr[11]/td[3]",
                f"{self.x_path_base}table[46]/tbody/tr[12]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    24h varchar(7), 1m varchar(7), 2m varchar(7),
                    1y varchar(7), 2y varchar(7), 3y varchar(7),
                    4y varchar(7), 5y varchar(7), 6y varchar(7),
                    7y varchar(7), 9y varchar(7), 10y varchar(7),
                    date DATE, year YEAR)
                 """
        Yields_DB().create_table(query)


class Portugal(Product):
    """Portaguese Government Bonds."""
    def __init__(self) -> None:
        columns = "3m,6m,1y,2y,3y,4y,5y,6y,7y,8y,9y,10y,15y,20y,30y,date"
        super().__init__(product="PortugalGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '3 Month': idx[1][0], '6 Month': idx[1][1], '1 Year': idx[1][2],
                '2 Year': idx[1][3], '3 Year': idx[1][4], '4 Year': idx[1][5],
                '5 Year': idx[1][6], '6 Year': idx[1][7], '7 Year': idx[1][8],
                '8 Year': idx[1][9], '9 Year': idx[1][10], '10 Year': idx[1][11],
                '15 Year': idx[1][12], '20 Year': idx[1][13], '30 Year': idx[1][14],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[47]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[47]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[47]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[47]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[47]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[47]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[47]/tbody/tr[7]/td[3]",
                f"{self.x_path_base}table[47]/tbody/tr[8]/td[3]",
                f"{self.x_path_base}table[47]/tbody/tr[9]/td[3]",
                f"{self.x_path_base}table[47]/tbody/tr[10]/td[3]",
                f"{self.x_path_base}table[47]/tbody/tr[11]/td[3]",
                f"{self.x_path_base}table[47]/tbody/tr[12]/td[3]",
                f"{self.x_path_base}table[47]/tbody/tr[13]/td[3]",
                f"{self.x_path_base}table[47]/tbody/tr[14]/td[3]",
                f"{self.x_path_base}table[47]/tbody/tr[15]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
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
    def __init__(self) -> None:
        columns = "2y,3y,5y,10y,30y,date"
        super().__init__(product="QatarGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '2 Year': idx[1][0], '3 Year': idx[1][1], '5 Year': idx[1][2],
                '10 Year': idx[1][3], '30 Year': idx[1][4],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[48]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[48]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[48]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[48]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[48]/tbody/tr[5]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    2y varchar(7), 3y varchar(7), 5y varchar(7),
                    10y varchar(7), 30y varchar(7), date DATE, year YEAR)
                 """
        Yields_DB().create_table(query)


class Romania(Product):
    """Romanian Government Bonds."""
    def __init__(self) -> None:
        columns = "6m,1y,2y,3y,4y,5y,7y,10y,date"
        super().__init__(product="RomaniaGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '6 Month': idx[1][0], '1 Year': idx[1][1], '2 Year': idx[1][2],
                '3 Year': idx[1][3], '4 Year': idx[1][4], '5 Year': idx[1][5],
                '7 Year': idx[1][6], '10 Year': idx[1][7],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[49]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[49]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[49]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[49]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[49]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[49]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[49]/tbody/tr[7]/td[3]",
                f"{self.x_path_base}table[49]/tbody/tr[8]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    6m varchar(7), 1y varchar(7), 2y varchar(7),
                    3y varchar(7), 4y varchar(7), 5y varchar(7),
                    7y varchar(7), 10y varchar(7), date DATE, year YEAR)
                 """
        Yields_DB().create_table(query)


class Russia(Product):
    """Russian Government Bonds."""
    def __init__(self) -> None:
        columns = "24h,1w,2w,1m,2m,3m,6m,1y,2y,3y,5y,7y,10y,15y,20y,date"
        super().__init__(product="RussiaGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                'Overnight': idx[1][0], '1 Week': idx[1][1], '2 Week': idx[1][2],
                '1 Month': idx[1][3], '2 Month': idx[1][4], '3 Month': idx[1][5],
                '6 Month': idx[1][6], '1 Year': idx[1][7], '2 Year': idx[1][8],
                '3 Year': idx[1][9], '5 Year': idx[1][10], '7 Year': idx[1][11],
                '10 Year': idx[1][12], '15 Year': idx[1][13], '20 Year': idx[1][14],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[50]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[50]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[50]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[50]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[50]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[50]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[50]/tbody/tr[7]/td[3]",
                f"{self.x_path_base}table[50]/tbody/tr[8]/td[3]",
                f"{self.x_path_base}table[50]/tbody/tr[9]/td[3]",
                f"{self.x_path_base}table[50]/tbody/tr[10]/td[3]",
                f"{self.x_path_base}table[50]/tbody/tr[11]/td[3]",
                f"{self.x_path_base}table[50]/tbody/tr[12]/td[3]",
                f"{self.x_path_base}table[50]/tbody/tr[13]/td[3]",
                f"{self.x_path_base}table[50]/tbody/tr[14]/td[3]",
                f"{self.x_path_base}table[50]/tbody/tr[15]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    24h varchar(7), 1w varchar(7), 2w varchar(7),
                    1m varchar(7), 2m varchar(7), 3m varchar(7),
                    6m varchar(7), 1y varchar(7), 2y varchar(7),
                    3y varchar(7), 5y varchar(7), 7y varchar(7),
                    10y varchar(7), 15y varchar(7), 20y varchar(7),
                    date DATE, year YEAR)
                 """
        Yields_DB().create_table(query)


class Serbia(Product):
    """Serbian Government Bonds."""
    def __init__(self) -> None:
        columns = "1y,2y,3y,5y,7y,10y,date"
        super().__init__(product="SerbiaGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '1 Year': idx[1][0], '2 Year': idx[1][1], '3 Year': idx[1][2],
                '5 Year': idx[1][3], '7 Year': idx[1][4], '10 Year': idx[1][5],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[51]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[51]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[51]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[51]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[51]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[51]/tbody/tr[6]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    1y varchar(7), 2y varchar(7), 3y varchar(7),
                    5y varchar(7), 7y varchar(7), 10y varchar(7),
                    date DATE, year YEAR)
                 """
        Yields_DB().create_table(query)


class Singapore(Product):
    """Singapore Government Bonds."""
    def __init__(self) -> None:
        columns = "1m,3m,6m,1y,2y,5y,10y,15y,20y,30y,date"
        super().__init__(product="SingaporeGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '1 Month': idx[1][0], '3 Month': idx[1][1], '6 Month': idx[1][2],
                '1 Year': idx[1][3], '2 Year': idx[1][4], '5 Year': idx[1][5],
                '10 Year': idx[1][6], '15 Year': idx[1][7], '20 Year': idx[1][8],
                '30 Year': idx[1][9],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[52]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[52]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[52]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[52]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[52]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[52]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[52]/tbody/tr[7]/td[3]",
                f"{self.x_path_base}table[52]/tbody/tr[8]/td[3]",
                f"{self.x_path_base}table[52]/tbody/tr[9]/td[3]",
                f"{self.x_path_base}table[52]/tbody/tr[10]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    1m varchar(7), 3m varchar(7), 6m varchar(7),
                    1y varchar(7), 2y varchar(7), 5y varchar(7),
                    10y varchar(7), 15y varchar(7), 20y varchar(7),
                    30y varchar(7), date DATE, year YEAR)
                 """
        Yields_DB().create_table(query)


class Slovakia(Product):
    """Slovakian Government Bonds."""
    def __init__(self) -> None:
        columns = "2y,5y,6y,8y,9y,10y,13y,18y,30y,50y,date"
        super().__init__(product="SlovakiaGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '2 Year': idx[1][0], '5 Year': idx[1][1], '6 Year': idx[1][2],
                '8 Year': idx[1][3], '9 Year': idx[1][4], '10 Year': idx[1][5],
                '13 Year': idx[1][6], '18 Year': idx[1][7], '30 Year': idx[1][8],
                '50 Year': idx[1][9],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[53]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[53]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[53]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[53]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[53]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[53]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[53]/tbody/tr[7]/td[3]",
                f"{self.x_path_base}table[53]/tbody/tr[8]/td[3]",
                f"{self.x_path_base}table[53]/tbody/tr[9]/td[3]",
                f"{self.x_path_base}table[53]/tbody/tr[10]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    2y varchar(7), 5y varchar(7), 6y varchar(7),
                    8y varchar(7), 9y varchar(7), 10y varchar(7),
                    13y varchar(7), 18y varchar(7), 30y varchar(7),
                    date DATE, year YEAR)
                 """
        Yields_DB().create_table(query)


class Slovenia(Product):
    """Slovenian Government Bonds."""
    def __init__(self) -> None:
        columns = "1y,2y,3y,5y,7y,8y,10y,15y,20y,25y,date"
        super().__init__(product="SloveniaGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '1 Year': idx[1][0], '2 Year': idx[1][1], '3 Year': idx[1][2],
                '5 Year': idx[1][3], '7 Year': idx[1][4], '8 Year': idx[1][5],
                '10 Year': idx[1][6], '15 Year': idx[1][7], '20 Year': idx[1][8],
                '25 Year': idx[1][9],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[54]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[54]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[54]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[54]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[54]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[54]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[54]/tbody/tr[7]/td[3]",
                f"{self.x_path_base}table[54]/tbody/tr[8]/td[3]",
                f"{self.x_path_base}table[54]/tbody/tr[9]/td[3]",
                f"{self.x_path_base}table[54]/tbody/tr[10]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    1y varchar(7), 2y varchar(7), 3y varchar(7),
                    5y varchar(7), 7y varchar(7), 8y varchar(7),
                    10y varchar(7), 15y varchar(7), 20y varchar(7),
                    25y varchar(7), date DATE, year YEAR)
                 """
        Yields_DB().create_table(query)


class South_Africa(Product):
    """South African Government Bonds."""
    def __init__(self) -> None:
        columns = "3m,2y,5y,10y,12y,20y,25y,30y,date"
        super().__init__(product="SouthAfricaGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '3 Month': idx[1][0], '2 Year': idx[1][1], '5 Year': idx[1][2],
                '10 Year': idx[1][3], '12 Year': idx[1][4], '20 Year': idx[1][5],
                '25 Year': idx[1][6], '30 Year': idx[1][7],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[55]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[55]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[55]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[55]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[55]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[55]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[55]/tbody/tr[7]/td[3]",
                f"{self.x_path_base}table[55]/tbody/tr[8]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    3m varchar(7), 2y varchar(7), 5y varchar(7),
                    10y varchar(7), 12y varchar(7), 20y varchar(7),
                    25y varchar(7), 30y varchar(7), date DATE, year YEAR)
                 """
        Yields_DB().create_table(query)


class South_Korea(Product):
    """South Korean Government Bonds."""
    def __init__(self) -> None:
        columns = "1y,2y,3y,4y,5y,10y,20y,30y,50y,date"
        super().__init__(product="SouthKoreaGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '1 Year': idx[1][0], '2 Year': idx[1][1], '3 Year': idx[1][2],
                '4 Year': idx[1][3], '5 Year': idx[1][4], '10 Year': idx[1][5],
                '20 Year': idx[1][6], '30 Year': idx[1][7], '50 Year': idx[1][8],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[56]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[56]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[56]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[56]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[56]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[56]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[56]/tbody/tr[7]/td[3]",
                f"{self.x_path_base}table[56]/tbody/tr[8]/td[3]",
                f"{self.x_path_base}table[56]/tbody/tr[9]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    1y varchar(7), 2y varchar(7), 3y varchar(7),
                    4y varchar(7), 5y varchar(7), 10y varchar(7),
                    20y varchar(7), 30y varchar(7), 50y varchar(7),
                    date DATE, year YEAR)
                 """
        Yields_DB().create_table(query)


class Spain(Product):
    """Spanish Government Bonds."""
    def __init__(self) -> None:
        columns = "1m,3m,6m,9m,1y,2y,3y,4y,5y,6y,7y,8y,9y,10y,15y,20y,25y,30y,date"
        super().__init__(product="SpainGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '1 Month': idx[1][0], '3 Month': idx[1][1], '6 Month': idx[1][2],
                '9 Month': idx[1][3], '1 Year': idx[1][4], '2 Year': idx[1][5],
                '3 Year': idx[1][6], '4 Year': idx[1][7], '5 Year': idx[1][8],
                '6 Year': idx[1][9], '7 Year': idx[1][10], '8 Year': idx[1][11],
                '9 Year': idx[1][12], '10 Year': idx[1][13], '15 Year': idx[1][14],
                '20 Year': idx[1][15], '25 Year': idx[1][16], '30 Year': idx[1][17],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[57]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[57]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[57]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[57]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[57]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[57]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[57]/tbody/tr[7]/td[3]",
                f"{self.x_path_base}table[57]/tbody/tr[8]/td[3]",
                f"{self.x_path_base}table[57]/tbody/tr[9]/td[3]",
                f"{self.x_path_base}table[57]/tbody/tr[10]/td[3]",
                f"{self.x_path_base}table[57]/tbody/tr[11]/td[3]",
                f"{self.x_path_base}table[57]/tbody/tr[12]/td[3]",
                f"{self.x_path_base}table[57]/tbody/tr[13]/td[3]",
                f"{self.x_path_base}table[57]/tbody/tr[14]/td[3]",
                f"{self.x_path_base}table[57]/tbody/tr[15]/td[3]",
                f"{self.x_path_base}table[57]/tbody/tr[16]/td[3]",
                f"{self.x_path_base}table[57]/tbody/tr[17]/td[3]",
                f"{self.x_path_base}table[57]/tbody/tr[18]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    1m varchar(7), 3m varchar(7), 6m varchar(7),
                    9m varchar(7), 1y varchar(7), 2y varchar(7),
                    3y varchar(7), 4y varchar(7), 5y varchar(7),
                    6y varchar(7), 7y varchar(7), 8y varchar(7),
                    9y varchar(7), 10y varchar(7), 15y varchar(7),
                    20y varchar(7), 25y varchar(7), 30y varchar(7),
                    date DATE, year YEAR)
                 """
        Yields_DB().create_table(query)


class Sri_Lanka(Product):
    """Sri Lanka Government Bonds."""
    def __init__(self) -> None:
        columns = "3m,6m,1y,2y,3y,4y,5y,6y,7y,8y,9y,10y,15y,date"
        super().__init__(product="SriLankaGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '3 Month': idx[1][0], '6 Month': idx[1][1], '1 Year': idx[1][2],
                '2 Year': idx[1][3], '3 Year': idx[1][4], '4 Year': idx[1][5],
                '5 Year': idx[1][6], '6 Year': idx[1][7], '7 Year': idx[1][8],
                '8 Year': idx[1][9], '9 Year': idx[1][10], '10 Year': idx[1][11],
                '15 Year': idx[1][12],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[58]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[58]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[58]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[58]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[58]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[58]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[58]/tbody/tr[7]/td[3]",
                f"{self.x_path_base}table[58]/tbody/tr[8]/td[3]",
                f"{self.x_path_base}table[58]/tbody/tr[9]/td[3]",
                f"{self.x_path_base}table[58]/tbody/tr[10]/td[3]",
                f"{self.x_path_base}table[58]/tbody/tr[11]/td[3]",
                f"{self.x_path_base}table[58]/tbody/tr[12]/td[3]",
                f"{self.x_path_base}table[58]/tbody/tr[13]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    3m varchar(7), 6m varchar(7), 1y varchar(7),
                    2y varchar(7), 3y varchar(7), 4y varchar(7),
                    5y varchar(7), 6y varchar(7), 7y varchar(7),
                    8y varchar(7), 9y varchar(7), 10y varchar(7),
                    15y varchar(7), date DATE, year YEAR)
                 """
        Yields_DB().create_table(query)


class Switzerland(Product):
    """Swiss Government Bonds."""
    def __init__(self) -> None:
        columns = "24h,1w,1m,2m,3m,6m,1y,2y,3y,4y,5y,6y,7y,8y,9y,10y,15y,20y,30y,50y,date"
        super().__init__(product="SwitzerlandGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                'Overnight': idx[1][0], '1 Week': idx[1][1], '1 Month': idx[1][2],
                '2 Month': idx[1][3], '3 Month': idx[1][4], '6 Month': idx[1][5],
                '1 Year': idx[1][6], '2 Year': idx[1][7], '3 Year': idx[1][8],
                '4 Year': idx[1][9], '5 Year': idx[1][10], '6 Year': idx[1][11],
                '7 Year': idx[1][12], '8 Year': idx[1][13], '9 Year': idx[1][14],
                '10 Year': idx[1][15], '15 Year': idx[1][16], '20 Year': idx[1][17],
                '30 Year': idx[1][18], '50 Year': idx[1][19],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[59]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[59]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[59]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[59]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[59]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[59]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[59]/tbody/tr[7]/td[3]",
                f"{self.x_path_base}table[59]/tbody/tr[8]/td[3]",
                f"{self.x_path_base}table[59]/tbody/tr[9]/td[3]",
                f"{self.x_path_base}table[59]/tbody/tr[10]/td[3]",
                f"{self.x_path_base}table[59]/tbody/tr[11]/td[3]",
                f"{self.x_path_base}table[59]/tbody/tr[12]/td[3]",
                f"{self.x_path_base}table[59]/tbody/tr[13]/td[3]",
                f"{self.x_path_base}table[59]/tbody/tr[14]/td[3]",
                f"{self.x_path_base}table[59]/tbody/tr[15]/td[3]",
                f"{self.x_path_base}table[59]/tbody/tr[16]/td[3]",
                f"{self.x_path_base}table[59]/tbody/tr[17]/td[3]",
                f"{self.x_path_base}table[59]/tbody/tr[18]/td[3]",
                f"{self.x_path_base}table[59]/tbody/tr[19]/td[3]",
                f"{self.x_path_base}table[59]/tbody/tr[20]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    24h varchar(7), 1w varchar(7), 1m varchar(7),
                    2m varchar(7), 3m varchar(7), 6m varchar(7),
                    1y varchar(7), 2y varchar(7), 3y varchar(7),
                    4y varchar(7), 5y varchar(7), 6y varchar(7),
                    7y varchar(7), 8y varchar(7), 9y varchar(7),
                    10y varchar(7), 15y varchar(7), 20y varchar(7),
                    30y varchar(7), 50y varchar(7), date DATE, year YEAR)
                 """
        Yields_DB().create_table(query)


class Taiwan(Product):
    """Taiwanese Government Bonds."""
    def __init__(self) -> None:
        columns = "2y,5y,10y,20y,30y,date"
        super().__init__(product="TaiwanGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '2 Year': idx[1][0], '5 Year': idx[1][1], '10 Year': idx[1][2],
                '20 Year': idx[1][3], '30 Year': idx[1][4],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[60]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[60]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[60]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[60]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[60]/tbody/tr[5]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    2y varchar(7), 5y varchar(7), 10y varchar(7),
                    20y varchar(7), 30y varchar(7), date DATE, year YEAR)
                 """
        Yields_DB().create_table(query)


class Thailand(Product):
    """Thai Government Bonds."""
    def __init__(self) -> None:
        columns = "1y,2y,3y,5y,7y,10y,12y,14y,15y,16y,20y,date"
        super().__init__(product="ThailandGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '1 Year': idx[1][0], '2 Year': idx[1][1], '3 Year': idx[1][2],
                '5 Year': idx[1][3], '7 Year': idx[1][4], '10 Year': idx[1][5],
                '12 Year': idx[1][6], '14 Year': idx[1][7], '15 Year': idx[1][8],
                '16 Year': idx[1][9], '20 Year': idx[1][10],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[61]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[61]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[61]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[61]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[61]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[61]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[61]/tbody/tr[7]/td[3]",
                f"{self.x_path_base}table[61]/tbody/tr[8]/td[3]",
                f"{self.x_path_base}table[61]/tbody/tr[9]/td[3]",
                f"{self.x_path_base}table[61]/tbody/tr[10]/td[3]",
                f"{self.x_path_base}table[61]/tbody/tr[11]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    1y varchar(7), 2y varchar(7), 3y varchar(7),
                    5y varchar(7), 7y varchar(7), 10y varchar(7),
                    12y varchar(7), 14y varchar(7), 15y varchar(7),
                    16y varchar(7), 20y varchar(7), date DATE, year YEAR)
                 """
        Yields_DB().create_table(query)


class Turkey(Product):
    """Turkish Government Bonds."""
    def __init__(self) -> None:
        columns = "3m,6m,9m,1y,2y,3y,5y,10y,date"
        super().__init__(product="TurkeyGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '3 Month': idx[1][0], '6 Month': idx[1][1], '9 Month': idx[1][2],
                '1 Year': idx[1][3], '2 Year': idx[1][4], '3 Year': idx[1][5],
                '5 Year': idx[1][6], '10 Year': idx[1][7],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[62]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[62]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[62]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[62]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[62]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[62]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[62]/tbody/tr[7]/td[3]",
                f"{self.x_path_base}table[62]/tbody/tr[8]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    3m varchar(7), 6m varchar(7), 9m varchar(7),
                    1y varchar(7), 2y varchar(7), 3y varchar(7),
                    5y varchar(7), 10y varchar(7), date DATE, year YEAR)
                 """
        Yields_DB().create_table(query)


class Uganda(Product):
    """Uganda Government Bonds."""
    def __init__(self) -> None:
        columns = "3m,6m,1y,2y,3y,5y,10y,15y,date"
        super().__init__(product="UgandaGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '3 Month': idx[1][0], '6 Month': idx[1][1], '1 Year': idx[1][2],
                '2 Year': idx[1][3], '3 Year': idx[1][4], '5 Year': idx[1][5],
                '10 Year': idx[1][6], '15 Year': idx[1][7],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[63]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[63]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[63]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[63]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[63]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[63]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[63]/tbody/tr[7]/td[3]",
                f"{self.x_path_base}table[63]/tbody/tr[8]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    3m varchar(7), 6m varchar(7), 1y varchar(7),
                    2y varchar(7), 3y varchar(7), 5y varchar(7),
                    10y varchar(7), 15y varchar(7), date DATE, year YEAR)
                 """
        Yields_DB().create_table(query)


class Ukraine(Product):
    """Ukrainian Government Bonds."""
    def __init__(self) -> None:
        columns = "1y,2y,3y,date"
        super().__init__(product="UkraineGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '1 Year': idx[1][0], '2 Year': idx[1][1], '3 Year': idx[1][2],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[64]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[64]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[64]/tbody/tr[3]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    1y varchar(7), 2y varchar(7), 3y varchar(7),
                    date DATE, year YEAR)
                 """
        Yields_DB().create_table(query)


class United_Kingdom(Product):
    """UK Government Bonds."""
    def __init__(self) -> None:
        columns = "1m,3m,6m,1y,2y,3y,4y,5y,6y,7y,8y,9y,10y,12y,15y,20y,25y,30y,40y,50y,date"
        super().__init__(product="UnitedKingdomGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '1 Month': idx[1][0], '3 Month': idx[1][1], '6 Month': idx[1][2],
                '1 Year': idx[1][3], '2 Year': idx[1][4], '3 Year': idx[1][5],
                '4 Year': idx[1][6], '5 Year': idx[1][7], '6 Year': idx[1][8],
                '7 Year': idx[1][9], '8 Year': idx[1][11], '9 Year': idx[1][12],
                '10 Year': idx[1][12], '12 Year': idx[1][13], '15 Year': idx[1][14],
                '20 Year': idx[1][15], '25 Year': idx[1][16], '30 Year': idx[1][17],
                '40 Year': idx[1][18], '50 Year': idx[1][19],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[65]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[65]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[65]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[65]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[65]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[65]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[65]/tbody/tr[7]/td[3]",
                f"{self.x_path_base}table[65]/tbody/tr[8]/td[3]",
                f"{self.x_path_base}table[65]/tbody/tr[9]/td[3]",
                f"{self.x_path_base}table[65]/tbody/tr[10]/td[3]",
                f"{self.x_path_base}table[65]/tbody/tr[11]/td[3]",
                f"{self.x_path_base}table[65]/tbody/tr[12]/td[3]",
                f"{self.x_path_base}table[65]/tbody/tr[13]/td[3]",
                f"{self.x_path_base}table[65]/tbody/tr[14]/td[3]",
                f"{self.x_path_base}table[65]/tbody/tr[15]/td[3]",
                f"{self.x_path_base}table[65]/tbody/tr[16]/td[3]",
                f"{self.x_path_base}table[65]/tbody/tr[17]/td[3]",
                f"{self.x_path_base}table[65]/tbody/tr[18]/td[3]",
                f"{self.x_path_base}table[65]/tbody/tr[19]/td[3]",
                f"{self.x_path_base}table[65]/tbody/tr[20]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    1m varchar(7), 3m varchar(7), 6m varchar(7),
                    1y varchar(7), 2y varchar(7), 3y varchar(7),
                    4y varchar(7), 5y varchar(7), 6y varchar(7),
                    7y varchar(7), 8y varchar(7), 9y varchar(7),
                    10y varchar(7), 12y varchar(7), 15y varchar(7),
                    20y varchar(7), 25y varchar(7), 30y varchar(7),
                    40y varchar(7), 50y varchar(7), date DATE, year YEAR)
                 """
        Yields_DB().create_table(query)


class United_States(Product):
    """US Government Bonds."""
    def __init__(self) -> None:
        columns = "1m,3m,6m,1y,2y,3y,5y,7y,10y,20y,30y,date"
        super().__init__(product="UnitedStatesGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '1 Month': idx[1][0], '3 Month': idx[1][1], '6 Month': idx[1][2],
                '1 Year': idx[1][3], '2 Year': idx[1][4], '3 Year': idx[1][5],
                '5 Year': idx[1][6], '7 Year': idx[1][7], '10 Year': idx[1][8],
                '20 Year': idx[1][9], '30 Year': idx[1][10],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[66]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[66]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[66]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[66]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[66]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[66]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[66]/tbody/tr[7]/td[3]",
                f"{self.x_path_base}table[66]/tbody/tr[8]/td[3]",
                f"{self.x_path_base}table[66]/tbody/tr[9]/td[3]",
                f"{self.x_path_base}table[66]/tbody/tr[10]/td[3]",
                f"{self.x_path_base}table[66]/tbody/tr[11]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    1m varchar(7), 3m varchar(7), 6m varchar(7),
                    1y varchar(7), 2y varchar(7), 3y varchar(7),
                    5y varchar(7), 7y varchar(7), 10y varchar(7),
                    20y varchar(7), 30y varchar(7), date DATE, year YEAR)
                 """
        Yields_DB().create_table(query)


class Vietnam(Product):
    """Vietnamese Government Bonds."""
    def __init__(self) -> None:
        columns = "1y,2y,3y,5y,7y,10y,15y,20y,25y,date"
        super().__init__(product="VietnamGB", columns=columns)

    def to_dict(self, query: list) -> dict:
        """Convert and output data to hashmap."""
        for idx in enumerate(Yields_DB().fetch(query)):
            key = str(idx[1][-1])
            self.output[key] = {
                '1 Year': idx[1][0], '2 Year': idx[1][1], '3 Year': idx[1][2],
                '5 Year': idx[1][3], '7 Year': idx[1][4], '10 Year': idx[1][5],
                '15 Year': idx[1][6], '20 Year': idx[1][7], '25 Year': idx[1][8],
            }
        return self.output

    def x_paths(self) -> list[str]:
        """Output paths to collect data."""
        return [f"{self.x_path_base}table[67]/tbody/tr[1]/td[3]",
                f"{self.x_path_base}table[67]/tbody/tr[2]/td[3]",
                f"{self.x_path_base}table[67]/tbody/tr[3]/td[3]",
                f"{self.x_path_base}table[67]/tbody/tr[4]/td[3]",
                f"{self.x_path_base}table[67]/tbody/tr[5]/td[3]",
                f"{self.x_path_base}table[67]/tbody/tr[6]/td[3]",
                f"{self.x_path_base}table[67]/tbody/tr[7]/td[3]",
                f"{self.x_path_base}table[67]/tbody/tr[8]/td[3]",
                f"{self.x_path_base}table[67]/tbody/tr[9]/td[3]"]

    def create_table(self) -> None:
        """Create table in database if not already exits."""
        query = f"""CREATE TABLE IF NOT EXISTS {self.product}
                   (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    1y varchar(7), 2y varchar(7), 3y varchar(7),
                    5y varchar(7), 7y varchar(7), 10y varchar(7),
                    15y varchar(7), 20y varchar(7), 25y varchar(7),
                    date DATE, year YEAR)
                 """
        Yields_DB().create_table(query)
