from typing import Type, Union

from app.data.government_bonds import hashmap
from app.models.yields.product import (Argentina, Australia, Austria, Bahrain,
                                       Bangledesh, Belgium, Botswana, Brazil,
                                       Bulgaria, Canada, Chile, China,
                                       Colombia, Crotia, Cyprus,
                                       Czech_Republic, Egypt, France, Germany,
                                       Greece, Hong_Kong, Hungary, Iceland,
                                       India)


def get_class(nation: str) -> Type[Union[Argentina, Australia, Austria,
                                         Bahrain, Bangledesh, Belgium,
                                         Botswana, Brazil, Bulgaria,
                                         Canada, Chile, China, Colombia,
                                         Crotia, Cyprus, Czech_Republic,
                                         Egypt, France, Germany, Greece,
                                         Hong_Kong, Hungary, Iceland,
                                         India]]:
    """Convert nation name to product class."""
    if nation not in hashmap:
        raise ValueError(f"Invalid nation: {nation} check the documentation for valid nations!")
    return hashmap[nation]
