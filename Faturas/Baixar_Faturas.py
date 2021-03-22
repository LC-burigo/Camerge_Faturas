from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import time


def main(data):
    browser = access()
    find(browser, data)
    time.sleep(1)
    save()
    browser.quit()


def access():
    browser = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
    browser.get("https://agenciaweb.celesc.com.br/AgenciaWeb/autenticar/loginCliente.do")
    browser.maximize_window()
    return browser


def find(browser, data):
    search = browser.find_element_by_name("sqUnidadeConsumidora")
    search.send_keys("8246998")
    search = browser.find_element_by_name("numeroDocumentoCPF")
    search.send_keys("71012710904")
    search.send_keys(Keys.RETURN)

    WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.NAME, "senha")))
    search = browser.find_element_by_name("senha")
    search.send_keys("marilda809")
    search.send_keys(Keys.RETURN)
    WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.ID, "mn")))
    browser.find_element_by_partial_link_text("de Pagamento").click()
    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "histFat")))
        td = browser.find_element_by_link_text("{}".format(data)).click()
        return td
    except NoSuchElementException:
        print("No element found")


def save():
    pyautogui.hotkey('ctrl', 's')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(1)






