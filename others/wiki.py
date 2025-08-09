
# go to wikipedia.org
# search for a topic
# print the text


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.edge.service import Service


# specify location of web driver in pc 

service = Service("C:\\Users\\Mallon User\\Downloads\\QA\\All selenium\\selenium webdriver & grid\\edgedriver_win64\\msedgedriver.exe")

# set options to make browser not to close

options = Options()
options.add_experimental_option("detach", True)

# add options and service

driver = webdriver.Edge(options=options, service=service)
url = "https://www.wikipedia.org/"
driver.get(url)