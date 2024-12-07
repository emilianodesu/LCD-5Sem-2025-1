"""GET Request to download a file from a URL and save it to a local file"""
import gzip
import shutil
import json
import requests

URL = "https://smn.conagua.gob.mx/tools/GUI/webservices/index.php?method=1"
FILEPATH = "C:\\Users\\cemh0\\Documents\\LCD\\LCD-5Sem-2025-1\\BDE\\2EP\\"
FILENAME = FILEPATH + "DailyForecast_MX.gz"
OUTPUT = FILEPATH + "DailyForecast_MX.json"

with open(FILENAME, "wb") as f:
    r = requests.get(URL, timeout=1000)
    f.write(r.content)

with gzip.open(FILENAME, 'rb') as f_in:
    with open(OUTPUT, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)


### Aqui se agregan nuevos estados al archivo JSON
with open(OUTPUT, "r", encoding='utf-8') as f:
    content = f.read()

content_without_bracket = content.lstrip('[')

nuevo_estado = {
    "cc": "75.5",
    "desciel": "Parcialmente nublado",
    "dh": "6",
    "dirvienc": "Sureste",
    "dirvieng": "135.0",
    "dloc": "20241130T00",
    "ides": "33",
    "idmun": "54",
    "lat": "17.3884",
    "lon": "-97.229",
    "ndia": "2",
    "nes": "New Hampshire",
    "nmun": "Magdalena Zahuatlán",
    "prec": "0.0",
    "probprec": "10",
    "raf": "12.5",
    "tmax": "23.0",
    "tmin": "8.2",
    "velvien": "5.6"
}

nuevo_estado_2 = {
    "cc": "75.5",
    "desciel": "Parcialmente nublado",
    "dh": "6",
    "dirvienc": "Sureste",
    "dirvieng": "135.0",
    "dloc": "20241130T00",
    "ides": "34",
    "idmun": "54",
    "lat": "17.3884",
    "lon": "-97.229",
    "ndia": "2",
    "nes": "Wyoming",
    "nmun": "Magdalena Zahuatlán",
    "prec": "0.0",
    "probprec": "10",
    "raf": "12.5",
    "tmax": "23.0",
    "tmin": "8.2",
    "velvien": "5.6"
}

new_record_json = json.dumps(nuevo_estado, ensure_ascii=False)
new_record_json_2 = json.dumps(nuevo_estado_2, ensure_ascii=False)

with open(OUTPUT, "w", encoding='utf-8') as file:
    file.write("[")
    file.write(new_record_json)
    file.write(",")
    file.write(new_record_json_2)
    file.write(",")
    file.write(content_without_bracket)
