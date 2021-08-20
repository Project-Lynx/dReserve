import json
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from app.config import WEB_AGENT, WEB_BINARY_PATH
from app.data.CME_Futures import futures_map
from app.models.futures import Meta
from app.util import links


def collection():
    sql = '''CREATE TABLE IF NOT EXISTS testing(
    id int, last varchar(255), _change varchar(255),
    open varchar(255), close varchar(255), high varchar(255),
    low varchar(255), highLimit varchar(255), lowLimit varchar(255),
    volume varchar(255), code varchar(255), updated varchar(255),
    pChange varchar(255), expiration varchar(255), name varchar(255),
    url varchar(255)
    );'''
    Meta().execute(sql)

    options = webdriver.ChromeOptions()
    options.binary_location = WEB_BINARY_PATH
    options.add_argument('--headless')
    options.add_argument(f'user-agent={WEB_AGENT}')
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    start_time = time.time()
    PIDS = futures_map.values()

    """
    Ugly hack, tried using just a dict instead of multiple lists
    wasnt able to get the function of this method. Open to anyone
    cleaning this.
    """
    GE_cache = []
    ES_cache = []
    ZT_cache = []
    ZF_cache = []
    ZN_cache = []
    TN_cache = []
    ZB_cache = []
    UB_cache = []
    GC_cache = []
    SI_cache = []
    HG_cache = []
    CL_cache = []
    NG_cache = []
    BTC_cache = []
    sixE_cache = []
    ZQ_cache = []
    SR3_cache = []

    while True:
        time.sleep(60.0 - ((time.time() - start_time) % 60.0))

        for PID in PIDS:
            if len(GE_cache) > 2:
                GE_cache.pop(0)
            elif len(ES_cache) > 2:
                del ES_cache[0]
            elif len(ZT_cache) > 2:
                del ZT_cache[0]
            elif len(ZF_cache) > 2:
                del ZF_cache[0]
            elif len(ZN_cache) > 2:
                del ZN_cache[0]
            elif len(TN_cache) > 2:
                del TN_cache[0]
            elif len(ZB_cache) > 2:
                del ZB_cache[0]
            elif len(UB_cache) > 2:
                del UB_cache[0]
            elif len(GC_cache) > 2:
                del GC_cache[0]
            elif len(SI_cache) > 2:
                del SI_cache[0]
            elif len(HG_cache) > 2:
                del HG_cache[0]
            elif len(CL_cache) > 2:
                del CL_cache[0]
            elif len(NG_cache) > 2:
                del NG_cache[0]
            elif len(BTC_cache) > 2:
                del BTC_cache[0]
            elif len(sixE_cache) > 2:
                del sixE_cache[0]
            elif len(ZQ_cache) > 2:
                del ZQ_cache[0]
            elif len(SR3_cache) > 2:
                del SR3_cache[0]

            target_url = (links.CME_API_BASE + PID + links.CME_API_END)
            driver.get(target_url)
            content = str(driver.page_source)
            start = content.find("last")-2
            end = content.find("</pre>")-1
            data = json.loads(content[start:end])

            pid = int(data.get('productId'))
            last = data.get('last')
            _change = data.get('change')
            _open = data.get('open')
            _close = data.get('close')
            high = data.get('high')
            low = data.get('low')
            high_limit = data.get('highLimit')
            low_limit = data.get('lowLimit')
            volume = data.get('volume')
            code = data.get('code')
            last_update = data.get('updated')
            p_change = data.get('percentageChange')
            expiration = data.get('expirationDate')
            name = data.get('productName')
            url = data.get('uri')

            if PID == "1":
                GE_cache.append(last_update)
                if len(GE_cache) > 1:
                    if last_update == GE_cache[1]:
                        continue
            if PID == "133":
                ES_cache.append(last_update)
                if len(ES_cache) > 1:
                    if last_update == ES_cache[1]:
                        continue
            if PID == "303":
                ZT_cache.append(last_update)
                if len(ZT_cache) > 1:
                    if last_update == ZT_cache[1]:
                        continue
            if PID == "329":
                ZF_cache.append(last_update)
                if len(ZF_cache) > 1:
                    if last_update == ZF_cache[1]:
                        continue
            if PID == "316":
                ZN_cache.append(last_update)
                if len(ZN_cache) > 1:
                    if last_update == ZN_cache[1]:
                        continue
            if PID == "7978":
                TN_cache.append(last_update)
                if len(TN_cache) > 1:
                    if last_update == TN_cache[1]:
                        continue
            if PID == "307":
                ZB_cache.append(last_update)
                if len(ZB_cache) > 1:
                    if last_update == ZB_cache[1]:
                        continue
            if PID == "3141":
                UB_cache.append(last_update)
                if len(UB_cache) > 1:
                    if last_update == UB_cache[1]:
                        continue
            if PID == "437":
                GC_cache.append(last_update)
                if len(GC_cache) > 1:
                    if last_update == GC_cache[1]:
                        continue
            if PID == "458":
                SI_cache.append(last_update)
                if len(SI_cache) > 1:
                    if last_update == SI_cache[1]:
                        continue
            if PID == "438":
                HG_cache.append(last_update)
                if len(HG_cache) > 1:
                    if last_update == HG_cache[1]:
                        continue
            if PID == "425":
                CL_cache.append(last_update)
                if len(CL_cache) > 1:
                    if last_update == CL_cache[1]:
                        continue
            if PID == "444":
                NG_cache.append(last_update)
                if len(NG_cache) > 1:
                    if last_update == NG_cache[1]:
                        continue
            if PID == "8478":
                BTC_cache.append(last_update)
                if len(BTC_cache) > 1:
                    if last_update == BTC_cache[1]:
                        continue
            if PID == "58":
                sixE_cache.append(last_update)
                if len(sixE_cache) > 1:
                    if last_update == sixE_cache[1]:
                        continue
            if PID == "305":
                ZQ_cache.append(last_update)
                if len(ZQ_cache) > 1:
                    if last_update == ZQ_cache[1]:
                        continue
            if PID == "8462":
                SR3_cache.append(last_update)
                if len(SR3_cache) > 1:
                    if last_update == SR3_cache[1]:
                        continue

            temp_list = [(pid, last, _change, _open, _close, high, low,
                          high_limit, low_limit, volume, code, last_update,
                          p_change, expiration, name, url)]

            sql = '''INSERT INTO testing(
                        id, last, _change, open, close, high,
                        low, highLimit, lowLimit, volume, code,
                        updated, pChange, expiration, name, url)
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                     '''
            Meta().executemany(sql, temp_list)


collection()
