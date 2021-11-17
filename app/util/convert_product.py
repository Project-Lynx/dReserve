from app.models.yields.product import (Argentina, Australia, Austria, Bahrain,
                                       Bangledesh, Belgium, Botswana, Brazil,
                                       Bulgaria, Canada, Chile, China,
                                       Colombia, Crotia, Cyprus,
                                       Czech_Republic)

hashmap = {
    "Argentina": Argentina,
    "argentina": Argentina,
    "Australia": Australia,
    "australia": Australia,
    "Austria": Austria,
    "austria": Austria,
    "Bahrain": Bahrain,
    "bahrain": Bahrain,
    "Bangledesh": Bangledesh,
    "bangledesh": Bangledesh,
    "Belgium": Belgium,
    "belgium": Belgium,
    "Botswana": Botswana,
    "botswana": Botswana,
    "Brazil": Brazil,
    "brazil": Brazil,
    "Bulgaria": Bulgaria,
    "bulgaria": Bulgaria,
    "Canada": Canada,
    "canada": Canada,
    "Chile": Chile,
    "chile": Chile,
    "China": China,
    "china": China,
    "Colombia": Colombia,
    "colombia": Colombia,
    "Crotia": Crotia,
    "crotia": Crotia,
    "Cyprus": Cyprus,
    "cyprus": Cyprus,
    "Czech Republic": Czech_Republic,
    "czech republic": Czech_Republic,
}


def get_class(nation: str) -> None:
    if nation not in hashmap:
        raise ValueError(f"Invalid nation: {nation} check the documentation for valid nations!")
    return hashmap[nation]
