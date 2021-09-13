import urllib.request

from app.models.yields import Meta as yields_model
from app.util.links import JGB_LINK

model = yields_model()
data = urllib.request.urlopen(JGB_LINK)
count = 0

for line in data.readlines():
    count += 1
    if count > 2:
        start = str(line).find("'") + 1
        end = str(line).find("\\")
        line = str(line)[start:end]

        list_ = list(line.split(","))

        # Converting YYYY/m/d -> YYYY-MM-DD
        _date = (list_[0])
        y_start = 0
        y_end = _date.find("/")
        year = _date[y_start:y_end]
        m_start = _date.find("/") + 1
        m_end = _date[m_start:].find("/")+(m_start)
        month = _date[m_start:m_end]
        if len(month) == 1:
            month = f"0{month}"
        d_start = _date[m_start:].find("/")+(m_start+1)
        day = _date[d_start:]
        if len(day) == 1:
            day = f"0{day}"
        _date = f"{year}-{month}-{day}"

        temp_list = [(_date, list_[1], list_[2],
                     list_[3], list_[4], list_[5],
                     list_[6], list_[7], list_[8],
                     list_[9], list_[10], list_[11],
                     list_[12], list_[13], list_[14],
                     list_[15])]

        model.executemany(
            "INSERT INTO JGB_table VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            temp_list,
        )
