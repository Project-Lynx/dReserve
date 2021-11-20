from selenium import webdriver

from app.models.yields.database import Yields_DB


class Meta:
    def __init__(self) -> None:
        PATH = f"{'/'.join(__file__.split('/')[:-3])}/util/chromedriver"
        self.driver = webdriver.Chrome(PATH)
        self.model = Yields_DB()
        self.dataset: list = []

    def __close__(self) -> None:
        """Close the web driver."""
        self.driver.close()

    def add_to_db(self, query: str, data: list[tuple]) -> None:
        """Add collected data to database."""
        self.model.executemany(query, data)
