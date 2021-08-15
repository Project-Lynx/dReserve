from bs4 import BeautifulSoup as bs
import requests as req
import sqlite3


payload = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Upgrade-Insecure-Requests': '1', 'DNT': '1', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5', 'Accept-Encoding': 'gzip, deflate',
}

url = "https://finance.yahoo.com/calendar/economic/"

response = req.request("GET", url, headers=payload)
parsed = bs(response.text, "lxml")

data_table = parsed.find("tbody", {'data-reactid': '33'})
data_rows = data_table.find_all("tr")

name = []
region = []
time = []
actual = []
expectation = []

for row in data_rows:
    countrys = row.find_all("td", {'aria-label': "Country"})
    
    for country in countrys:
        if country.text == "JP":
            region.append(country.text)
            events = row.find_all("td", {'aria-label': "Event"})
            
            for event in events:
                name.append((event.text).replace("*", ""))
            event_times = row.find_all("td", {'aria-label': "Event Time"})
            
            for t in event_times:
                time.append(t.text)
            actual_ = row.find_all("td", {'aria-label': "Actual"})
            
            for x in actual_:
                actual.append(x.text)
            expecs = row.find_all("td", {'aria-label': "Market Expectation"})
            
            for expec in expecs:
                expectation.append(expec.text)

temp_list = []
for idx in enumerate(name):
    connec = sqlite3.connect('app/data/econ_events.db')
    cursor = connec.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS events
                       (name text, region text, time text, actual text,
                       expectation text)""")

    temp_list.append((idx[1], region[idx[0]], time[idx[0]], actual[idx[0]], expectation[idx[0]]))
    print("New Iter")
    
    cursor.executemany(f"INSERT INTO events VALUES (?,?,?,?,?)", temp_list)
    connec.commit()
    connec.close()