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
                                       South_Africa, South_Korea)


def parse_nation_name(nation: str) -> str:
    """Parse nation string to be Uppercase First letter & lowercase rest."""
    if " " in nation:
        split = nation.split(" ")
        return f"{split[0][0].upper()}{split[0][1:].lower()} {split[1][0].upper()}{split[1][1:].lower()}"

    return f"{nation[0].upper()}{nation[1:].lower()}"


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
                                         Slovenia, South_Africa, South_Korea]]:
    """Convert nation name to product class."""
    nation_parsed = parse_nation_name(nation)
    if nation_parsed not in hashmap:
        raise ValueError(f"Invalid nation: {nation} check the documentation for valid nations!")
    return hashmap[nation_parsed]
