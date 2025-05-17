from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select
# from minimum_price import get_minimum_flight_price_detail
# from avaliable_flights import check_if_value_in_select
import time


# def valuejet(location, destination, depdate):


# set options to make browser not to close
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=options)
url = "https://flyvaluejet.com/"
driver.get(url)


# select state for outbound flight
departure_state = driver.find_element(by=By.XPATH, value = '//select[@name="dep-airport"]')
departure_selection = Select(departure_state)
departure_selection.select_by_visible_text ("Abuja (ABV)")

# select state for inbound flight
arrival_state = driver.find_element(by=By.XPATH,value = '//select[@name="arr_ports"]')
arrival_selection = Select(arrival_state)
arrival_selection.select_by_visible_text ("Jos (JOS)")

# # format date field to remove it from read only (javascript code)
# driver.execute_script("date = document.getElementsByClassName('input-date')[0]; date.removeAttribute('readonly')")

# select flight date
date = driver.find_element( by=By.XPATH,value = "//input[@placeholder='Departure Date']")
date.clear()
date.send_keys("23 - jun")

# Number of passengers
# passengers = driver.find_element(by=By.XPATH, value = '//div[@class="block h-12 form-select w-full py-3 px-2 text-md border border-gray-300 bg-white rounded-md shadow-sm"]')
# passengers.clear()
# passengers.send_keys("1")


search_flights = driver.find_element(by=By.XPATH, value='//button[@data-testid="search-flights"]').click()

time.sleep(5)
all_flights = driver.find_element(by=By.XPATH, value='//div[@class="w-full focus:shadow-outline rounded-lg md:mx-auto"]')
price = all_flights.find_element(by=By.XPATH, value='.//div[@class"w-full focus:shadow-outline rounded-lg md:mx-auto"]').text

# print(price)


