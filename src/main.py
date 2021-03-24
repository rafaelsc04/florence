#! ../venv/bin/python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from login import login
from sig import signal
from upstream import upstream
from time import sleep
from downstream import downstream
import json

options = Options()
options.add_argument('--headless')

driver = webdriver.Chrome(options=options)

driver.get("http://192.168.100.1")

login(driver)
sig = signal(driver)
ups = upstream(driver)
down = downstream(driver)

final = {
    "tx": sig["tx"],
    "rx": sig["rx"],
    "upstream": ups,
    "downstream": down
}

jsonFinal = json.dumps(final)

print(jsonFinal)

driver.quit()
