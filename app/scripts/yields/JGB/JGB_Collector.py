from app.models.yields.collection import Meta
from app.models.yields.database import Yields_DB
from app.util import dates


class Collection(Meta):
    def __init__(self) -> None:
        url = "http://www.worldgovernmentbonds.com/bond-historical-data/japan/1-month/"
        super().__init__(url, "JGB", Yields_DB)

    def parse_data(self) -> list[tuple]:
        """Parsing data."""
        data = self.get_data()
        target_data = data.findAll("tbody")[-1]

        date_item = data.find("p", {'class': "w3-small w3-right"}).text
        date_pre = list(date_item.split(" "))
        day = date_pre[2]
        month = dates.convert_shorthand_month(date_pre[3])
        year = date_pre[4]
        date_final = f"{year}-{month}-{day}"

        count = 0
        for i in target_data:
            if hasattr(i, 'bs4.element.Tag') and "%" in i.text:
                count += 1
                if count not in [4, 8, 10, 12, 13]:
                    d_list = (i.text).splitlines()
                    for j in d_list:
                        if "%" in j:
                            self.dataset.append(j)
        self.dataset.append(date_final)
        self.dataset.append(year)
        return [tuple(self.dataset)]
