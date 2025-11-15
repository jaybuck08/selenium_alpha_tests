
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
url = "https://themix.ng/collections/puma-men"
driver.get(url)

Total_collection = driver.find_element (by=By.XPATH, value = '//div[@class="collection__main"]')
Puma_shirts = Total_collection.find_elements (by=By.XPATH, value = './/product-card[@class="product-card"]')

for index in Puma_shirts:

    shirt = driver.find_elements (by=By.XPATH, value = '//div[@class="v-stack justify-items-center gap-2"]')

    shirt_name = index.find_element(by=By.XPATH, value = './/a[@class="product-title h6 "]').text
    sale_price = index.find_element(by=By.XPATH, value = './/span[@class="money"]').text

    clean_price = sale_price.replace(",", "").replace("₦", "").strip()

# this removes the decimal in the price
    price = float(clean_price)


# show only shirts that cost more than 100,000
    if price < 50000:
        # print("Shirt price:", price, shirt_name)
        print(f"Shirt price:{shirt_name}{price}")

   