from typing import Type, Union

from app.data.government_bonds import hashmap
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
                                       South_Africa)


def get_class(nation: str) -> Type[Union[Argentina, Australia, Austria,
                                         Bahrain, Bangledesh, Belgium,
                                         Botswana, Brazil, Bulgaria,
                                         Canada, Chile, China, Colombia,
                                         Crotia, Cyprus, Czech_Republic,
                                         Egypt, France, Germany, Greece,
                                         Hong_Kong, Hungary, Iceland,
                                         India, Indonesia, Ireland, Israel,
                                         Italy, Japan, Jordan, Kazakhstan,
                                         Kenya, Malaysia, Malta, Mauritius,
                                         Mexico, Morocco, Namibia, Netherlands,
                                         Nigeria, Norway, Pakistan, Peru,
                                         Philippines, Poland, Portugal, Qatar,
                                         Romania, Russia, Serbia, Singapore,
                                         Slovenia, South_Africa]]:
    """Convert nation name to product class."""

    # Parse nation name to be Uppercase first letter and lowercase rest.
    nation = f"{nation[0].upper()}{nation[1:].lower()}"

    if nation not in hashmap:
        raise ValueError(f"Invalid nation: {nation} check the documentation for valid nations!")
    return hashmap[nation]
