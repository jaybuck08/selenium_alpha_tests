
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
url = "https://themix.ng/collections/men-sale-apparel"
driver.get(url)


shirt_collection = driver.find_element (by=By.XPATH, value ='//div[@class="collection__main"]')

shirts = shirt_collection.find_elements (by=By.XPATH, value = './/product-card[@class="product-card"]')

for index in shirts:

    # shirt = driver.find_elements (by=By.XPATH, value = '//div[@class="v-stack justify-items-center gap-2"]')

    sale_price = index.find_element(by=By.XPATH, value = './/span[@class="money"]')
    print(sale_price.text)

    shirt_title = index.find_element(by=By.XPATH, value = './/a[@class="product-title h6 "]')
    print(shirt_title.text)
    




    

  

    
  

