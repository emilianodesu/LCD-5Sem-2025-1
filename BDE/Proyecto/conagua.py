"""GET Request to download a file from a URL and save it to a local file"""
import gzip
import shutil
import requests

URL = "https://smn.conagua.gob.mx/tools/GUI/webservices/index.php?method=1"
FILEPATH = "C:\\Users\\cemh0\\Documents\\LCD\\LCD-5Sem-2025-1\\BDE\\Proyecto\\"
FILENAME = FILEPATH + "DailyForecast_MX.gz"
OUTPUT = FILEPATH + "DailyForecast_MX.json"

with open(FILENAME, "wb") as f:
    r = requests.get(URL, timeout=1000)
    f.write(r.content)

with gzip.open(FILENAME, 'rb') as f_in:
    with open(OUTPUT, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
