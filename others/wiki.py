
# go to wikipedia.org
# search for a topic
# print the text


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import time

from selenium.webdriver.edge.service import Service


# specify location of web driver in pc (use double forward slash so python can recognise it)

service = Service("C:\\Users\\Mallon User\\Downloads\\QA\\All selenium\\selenium webdriver & grid\\edgedriver_win64\\msedgedriver.exe")

# set options to make browser not to close

options = Options()
options.add_experimental_option("detach", True)

# add options and service

driver = webdriver.Edge(options=options, service=service)
url = "https://www.wikipedia.org/"
driver.get(url)

# search for product

wiki_search = driver.find_element(by=By.XPATH, value='//input[@id="searchInput"]')
wiki_search.send_keys("Australia")
wiki_search.send_keys(Keys.ENTER)

# print content

content = WebDriverWait(driver,10).until(ec.presence_of_element_located((By.XPATH, '//main[@id="content"]'))) 

# or

# time.sleep(10)

# text_holder = driver.find_element(by=By.XPATH, value='//div[@class="mw-content-container"]')
# content = text_holder.find_element(by=By.XPATH, value='.//main[@id="content"]')

print(content.text)

