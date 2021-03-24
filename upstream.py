from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def upstream(driver):
    upstream_table = driver.find_element_by_id("sta_signal_us")

    upstream = []
    i = 0

    for row in upstream_table.find_elements_by_css_selector("tr"):
        d = {}
        for cell in row.find_elements_by_tag_name("td"):
            if i == 0:
                d["id_canal"] = int(cell.text)
                i += 1
                continue
            if i == 1:
                d["status_bloqueio"] = cell.text
                i += 1
                continue
            if i == 2:
                d["frequencia"] = float(cell.text.split()[0])
                i += 1
                continue
            if i == 3:
                d["modulacao"] = cell.text
                i += 1
                continue
            if i == 4:
                d["nivel_potencia"] = float(cell.text.split()[0])
                i += 1
                continue
            if i == 5:
                d["taxa_simbolos"] = int(cell.text)
                i = 0
                break
        upstream.append(d)

    upstream.remove({})

    return upstream
