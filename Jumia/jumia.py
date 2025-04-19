from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# set options to make browser not to close

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=options)
url = "https://www.jumia.com.ng/"
driver.get(url)


# search for product

search_bar = driver.find_element(by=By.XPATH, value = '//input[@id="fi-q"]')
search_bar.send_keys("earphone")
search_bar.send_keys(Keys.ENTER)

# close pop up

driver.implicitly_wait(5)

try:
    
    button_holder = driver.find_element(by=By.XPATH, value = '//div[@class="fc-dialog-container"]')
    consent_button = button_holder.find_element(by=By.XPATH, value = './/button[@class="fc-button fc-cta-do-not-consent fc-secondary-button"]').click()

# "pass" is used for everthing and "contiune" is used only for loops
except:
    pass 

# getting container that holds all ear phones

# all_earphones = driver.find_element(by=By.XPATH, value= '//div[@class="-phs -pvxs row _no-g _4cl-3cm-shs"]')
earphone_containers = driver.find_elements(By.XPATH, value= './/article[contains(@class,"prd")]')


print (len(earphone_containers))


final_prices = []

for earphone in earphone_containers:

    # names_and_prices = earphone.find_element(By.XPATH, './/div[@class="info"]').text
    names  = earphone.find_element(By.XPATH,'.//h3[@class="name"]').text
    price_raw = earphone.find_element(By.XPATH, './/div[contains(@class,"prc")]').text
    
    # removing the naira sign, space and comma then converting to float
    price_cleaned = float(price_raw.replace(",","").replace("₦ ",""))

    # putting the price and name in a dctionary beacuse price is a float and name is a string
    price_data = {"name":names, "price":price_cleaned}

    # appending the dictionary into a list
    final_prices.append(price_data)


def price_extract (product_package):
    return product_package["price"]

# statement below : if the length of final prices is less than 1, then print () ..

# note: "if not" converts true statements to false and vice versa

if len (final_prices) < 1 : 
    # print(final_prices)
    print("search did not generate any result")

else:
# find minimum price

   
    minimum = min(
        final_prices,
        key = lambda product_package : price_extract(product_package)
    )

    print(minimum)



    
# def price_extract (product_package):
# This defines a function called price_extract.
# The function takes one input, a list called product_package.
# Each item in the product_package list should be a dictionary with at least a "price" key.

