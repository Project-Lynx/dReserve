from app.models.yields.collection import Meta
from app.models.yields.database import Yields_DB


class Collection(Meta):
    def __init__(self) -> None:
        super().__init__("UST", Yields_DB)

    def parse_data(self) -> list[tuple]:
        """Parsing data."""
        data = self.get_data("https://data.treasury.gov/feed.svc/DailyTreasuryYieldCurveRateData")
        entries = data.findAll("entry")
        entry = entries[-1]

        unclean_date, d_end = entry.find("d:new_date").text, (entry.find("d:new_date").text).find("T")
        date, year = unclean_date[:d_end], (unclean_date[:d_end])[:4]

        self.dataset = [
            entry.find("d:bc_1month").text, entry.find("d:bc_2month").text,
            entry.find("d:bc_3month").text, entry.find("d:bc_6month").text,
            entry.find("d:bc_1year").text, entry.find("d:bc_2year").text,
            entry.find("d:bc_3year").text, entry.find("d:bc_5year").text,
            entry.find("d:bc_7year").text, entry.find("d:bc_10year").text,
            entry.find("d:bc_20year").text, entry.find("d:bc_30year").text,
        ]

        return [
           (self.dataset[0], self.dataset[1], self.dataset[2], self.dataset[3], self.dataset[4],
            self.dataset[5], self.dataset[6], self.dataset[7], self.dataset[8], self.dataset[9],
            self.dataset[10], self.dataset[11], date, year),
        ]
