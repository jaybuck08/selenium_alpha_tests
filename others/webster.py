# go to https://www.merriam-webster.com/
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
url = "https://www.merriam-webster.com/"
driver.get(url)

# search for word

webster_search = driver.find_element(by = By.XPATH, value = '//input[@id="home-search-term"]')
webster_search.send_keys("Politics")
webster_search.send_keys(Keys.ENTER)

# print content

content = driver.find_element(by=By.XPATH, value='//div[@class="entry-word-section-container"]')
print(content.text)