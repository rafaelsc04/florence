from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


def login(driver):
    username = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "username"))
    )
    username.send_keys(os.environ.get("FLORENCE_USER"))

    password = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "password"))
    )
    password.send_keys(os.environ.get("FLORENCE_PASSWORD"))

    loginButton = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "login-button"))
    )
    loginButton.click()
