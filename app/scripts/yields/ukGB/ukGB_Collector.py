from app.models.yields.collection import Meta
from app.models.yields.database import Yields_DB
from app.util import dates


class Collection(Meta):
    def __init__(self) -> None:
        super().__init__("UKGB", Yields_DB)

    def parse_data(self) -> list[tuple]:
        """Parsing data."""
        url = "http://www.worldgovernmentbonds.com/bond-historical-data/united-kingdom/1-month/"
        data = self.get_data(url).findAll("td", {'class': "w3-center"})
        date = self.get_data(url).find("p", {'class': "w3-small w3-right"}).text
        date_list = list(date.split())
        day = date_list[2]
        month = dates.convert_shorthand_month(date_list[3])
        year = date_list[4]
        date_final = f"{year}-{month}-{day}"

        target_data = data[-80:]
        count = 0
        for i in target_data:
            if "%" in i.text:
                count += 1
                if count not in [7, 9, 11, 12, 14, 20]:
                    self.dataset.append(i.text[:-1])
        self.dataset.append(date_final)
        self.dataset.append(year)
        return [tuple(self.dataset)]
