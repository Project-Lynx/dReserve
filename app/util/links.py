CME_API_BASE = "https://www.cmegroup.com/CmeWS/mvc/Quotes/ContractsByNumber?productIds="
CME_API_END = "&contractsNumber=1&venue=G&type=VOLUME"

HIST_TOMO_BASE = "https://markets.newyorkfed.org/read?productCode=70&startDt=2013-09-28&endDt=2021-09-27"
HIST_TOMO_END = "&eventCodes=730&operationTypes="
HIST_RRP = HIST_TOMO_BASE + HIST_TOMO_END + "Reverse%20Repo&format=xml"
HIST_RP = HIST_TOMO_BASE + HIST_TOMO_END + "Repo&format=xml"
