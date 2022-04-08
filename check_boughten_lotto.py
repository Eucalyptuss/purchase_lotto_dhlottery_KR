import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
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

driver.find_element(
    By.XPATH, '//*[@id="article"]/div[2]/div/form/div/div[1]/fieldset/div[1]/a'
).click()
time.sleep(1)

driver.get("https://dhlottery.co.kr/userSsl.do?method=myPage")

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

soup_table = soup.select_one("table.tbl_data")

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

tables = pd.read_html(str(soup_table))
table = tables[0]
print(table)

table.to_excel("lotto_result.xlsx")
