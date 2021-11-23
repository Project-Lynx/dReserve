import datetime as dt
from typing import Type, Union

from app.models.yields.collection import Meta
from app.models.yields.product import (Argentina, Australia, Austria, Bahrain,
                                       Bangledesh, Belgium, Botswana, Brazil,
                                       Bulgaria, Canada, Chile, China,
                                       Colombia, Crotia, Cyprus,
                                       Czech_Republic, Egypt, France, Germany,
                                       Greece, Hong_Kong, Hungary, Iceland,
                                       India, Indonesia, Ireland, Israel,
                                       Italy, Japan, Jordan, Kazakhstan, Kenya,
                                       Malaysia, Malta, Mauritius, Mexico,
                                       Morocco, Namibia, Netherlands, Nigeria,
                                       Norway, Pakistan, Peru, Philippines,
                                       Poland, Portugal, Qatar, Romania,
                                       Russia, Serbia, Singapore, Slovenia,
                                       South_Africa, South_Korea, Spain,
                                       Sri_Lanka, Switzerland, Taiwan,
                                       Thailand, Turkey, Uganda, Ukraine,
                                       United_Kingdom, United_States, Vietnam)


class Script(Meta):
    def __init__(self) -> None:
        super().__init__()
        self.today = str(dt.datetime.today().strftime("%Y-%m-%d"))
        self.products = [Argentina, Australia, Austria, Bahrain, Bangledesh, Belgium, Botswana,
                         Brazil, Bulgaria, Canada, Chile, China, Colombia, Crotia, Cyprus,
                         Czech_Republic, Egypt, France, Germany, Greece, Hong_Kong, Hungary,
                         Iceland, India, Indonesia, Ireland, Israel, Italy, Japan, Jordan,
                         Kazakhstan, Kenya, Malaysia, Malta, Mauritius, Mexico, Morocco,
                         Namibia, Netherlands, Nigeria, Norway, Pakistan, Peru, Philippines,
                         Poland, Portugal, Qatar, Romania, Russia, Serbia, Singapore, Slovenia,
                         South_Africa, South_Korea, Spain, Sri_Lanka, Switzerland, Taiwan,
                         Thailand, Turkey, Uganda, Ukraine, United_Kingdom, United_States, Vietnam]

    def main(self) -> None:
        """Main method to run script."""
        self.go_to_site()
        for product in self.products:
            self.collect(product=product)
        self.__close__()

    def go_to_site(self) -> None:
        """Navigate to target site."""
        self.driver.get("https://www.investing.com/rates-bonds/world-government-bonds")

    def grab_rates(self, paths: list) -> list[tuple]:
        """Output list of rates for given paths."""
        temp = []
        for path in paths:
            rate = self.driver.find_element_by_xpath(path)
            temp.append(rate.text)
        temp.append(self.today)
        return [tuple(i for i in temp)]

    def collect(self, product: Type[Union[Argentina, Australia, Austria, Bahrain, Bangledesh,
                                          Belgium, Botswana, Brazil, Bulgaria, Canada, Chile,
                                          China, Colombia, Crotia, Cyprus, Czech_Republic, Egypt,
                                          France, Germany, Greece, Hong_Kong, Hungary, Iceland,
                                          India, Indonesia, Ireland, Israel, Italy, Japan, Jordan,
                                          Kazakhstan, Kenya, Malaysia, Malta, Mauritius, Mexico,
                                          Morocco, Namibia, Netherlands, Nigeria, Norway, Pakistan, Peru,
                                          Philippines, Poland, Portugal, Qatar, Romania, Russia, Serbia,
                                          Singapore, Slovenia, South_Africa, South_Korea, Spain, Sri_Lanka,
                                          Switzerland, Taiwan, Thailand, Turkey, Uganda, Ukraine, United_Kingdom,
                                          United_States, Vietnam]]) -> None:
        """Collect data for a given product."""
        product().create_table()
        Product_Rates = self.grab_rates(product().x_paths())
        self.add_to_db(
            query=product().add_to_db_query(),
            data=Product_Rates,
        )


if __name__ == '__main__':
    # Run script
    Script().main()
