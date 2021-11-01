import json
from typing import Union

import requests as req
from bs4 import BeautifulSoup as bs

from app.models.federal_reserve.database import Fed_Model

url_base = "https://www.federalreserve.gov/"


def get_data() -> list:
    """Fetch data."""
    url = f"{url_base}json/ne-press.json"
    return json.loads(req.get(url).content)[:-1]


def convert_date(date: str) -> str:
    """
    Convert m_d_YYYY date string to standard
    format for the FOMC statement database.

    input: m/d/YYYY formated date string.
    output: YYYY-mm-dd formated date string.
    """
    date_end = date.find(" ")
    _date = date[:date_end].replace("/", "-")
    delim_1 = _date.find("-")
    delim_2 = (_date[delim_1:].find("-") + delim_1 + 1)
    delim_3 = (_date[delim_2:].find("-") + delim_2 + 1)

    month = _date[:delim_1]
    if len(month) == 1:
        month = f"0{month}"
    day = _date[delim_2:(delim_3-1)]
    if len(day) == 1:
        day = f"0{day}"
    year = _date[delim_3:]
    return f"{year}-{month}-{day}"


def check_for_new() -> Union[list[str], None]:
    """
    Check if there's a new fomc statement.

    output:
    ----------------
    if new statement -> link to statement.
    else no new statement -> None.
    """
    query = "SELECT date FROM fomc_statements ORDER BY id DESC LIMIT 1"
    most_recent_date = str(Fed_Model().fetch(query)[0][0])
    for hashmap in get_data():
        title = hashmap['t']
        if "issues FOMC statement" in title:
            date = convert_date(hashmap['d'])
            link = hashmap['l']
            if date != most_recent_date:
                return [date, f"{url_base}{link}"]
            return None
    return None


def get_new_statement() -> Union[list, None]:
    new = check_for_new()
    if new is None:
        return None
    response = bs(req.get(new[1]).text, "lxml")
    return [p.text for p in response.findAll("p")[40:-3]]


def parse_statement() -> str:
    statement = get_new_statement()
    if statement:
        cleaned_paragraphs = []
        for p in statement:
            if '"' in p:
                p = p.replace('"', "'")
            if "â" in p:
                p = p.replace("â", " ")
                p = p.replace("\x80\x91", "")
            cleaned_paragraphs.append(p)
        intro = f"{cleaned_paragraphs[0]}\n\n      "
        body_list = [f"{p}\n      \n      " for p in cleaned_paragraphs[1:-1]]
        body = ''.join(body_list)
        outro = cleaned_paragraphs[-1]
        return f"{intro + body + outro}"
    else:
        return "No new statement!"


def add_to_db() -> None:
    new = check_for_new()
    if new:
        date = new[0]
    else:
        return None
    statement = parse_statement()
    data = [(date, date[:4], statement)]
    Fed_Model().executemany(
       "INSERT INTO fomc_statements (date,year,statement) VALUES (%s,%s,%s)",
       data,
    )
