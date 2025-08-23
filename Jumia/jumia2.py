from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
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

