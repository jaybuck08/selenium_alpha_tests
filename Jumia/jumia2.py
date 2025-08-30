from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import time

from selenium.webdriver.edge.service import Service

# specify location of web driver in pc (use double forward slash so python can recognise it)
service = Service("C:\\Users\\Mallon User\\Downloads\\QA\\All selenium\\selenium webdriver & grid\\edgedriver_win64\\msedgedriver.exe")


# set options to make browser not to close
options = Options()
options.add_experimental_option("detach", True)

driver = driver = webdriver.Edge(options=options, service=service)
url = "https://www.jumia.com.ng/"
driver.get(url)

# product search

item_search = driver.find_element(by=By.XPATH, value='//input[@placeholder="Search products, brands and categories"]')
item_search.send_keys("shoe")
item_search.send_keys(Keys.ENTER)

# shoe name and price

first_shoe_holder=WebDriverWait(driver,50).until(ec.presence_of_all_elements_located((By.XPATH, '//article[@class="prd _fb _spn c-prd col"]')))[11]

result=first_shoe_holder.find_elements(by=By.TAG_NAME, value="a")[1]

result.click()

shoe_name = WebDriverWait(driver,10).until(ec.presence_of_element_located((By.XPATH, '//h1[@class="-fs20 -pts -pbxs"]')))
shoe_price = driver.find_element(by=By.XPATH, value='//span[@class="-b -ubpt -tal -fs24 -prxs"]')

print(shoe_name.text)
print(shoe_price.text)