import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

from config import *


service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://dhlottery.co.kr/user.do?method=login&returnUrl=")
time.sleep(1)

driver.find_element(By.NAME, "userId").send_keys(user)
time.sleep(1)

driver.find_element(By.NAME, "password").send_keys(password)
time.sleep(1)

driver.find_element(By.XPATH, '//*[@id="article"]/div[2]/div/form/div/div[1]/fieldset/div[1]/a').click()
time.sleep(1)

driver.get("https://el.dhlottery.co.kr/game/TotalGame.jsp?LottoId=LO40")
time.sleep(1)

driver.switch_to.frame("ifrm_tab")
driver.find_element(By.XPATH, '//*[@id="num2"]').click()
time.sleep(1)

select = Select(driver.find_element(By.XPATH, '//*[@id="amoundApply"]'))
select.select_by_value("5")

driver.find_element(By.XPATH, '//*[@id="btnSelectNum"]').click()
time.sleep(1)

driver.find_element(By.XPATH, '//*[@id="btnBuy"]').click()
time.sleep(1)

driver.find_element(
    By.XPATH, '//*[@id="popupLayerConfirm"]/div/div[2]/input[1]'
).click()
time.sleep(5)

