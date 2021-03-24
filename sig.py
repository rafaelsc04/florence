from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def signal(driver):
    tx_text = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[2]/div[3]/div[3]/div/div/table[1]/tbody/tr[1]/td[2]"))
    ).text

    rx_text = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/div[2]/div[3]/div[3]/div/div/table[1]/tbody/tr[2]/td[2]"))
    ).text

    tx = int(tx_text.split()[0])
    rx = int(rx_text.split()[0])

    return {"rx": rx, "tx": tx}
