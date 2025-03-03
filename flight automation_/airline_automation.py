from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select

# set options to make browser not to close
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Edge(options=options)
url = "https://flyaero.com/"
driver.get(url)


# select state for outbound flight
departure_state = driver.find_element(by=By.XPATH,value = '//select[@name="depPort"]')

departure_selection = Select(departure_state)
departure_selection.select_by_visible_text("Abuja (ABV)")


# select state for inbound flight
arrival_state = driver.find_element(by=By.XPATH,value = '//select[@name="arrPort"]')

arrival_selection = Select(arrival_state)
arrival_selection.select_by_visible_text("Lagos (LOS)")


# format date field to remove it from read only (javascript code)
driver.execute_script("date = document.getElementsByClassName('input-date')[0]; date.removeAttribute('readonly')")


# select flight date
date = driver.find_element( by=By.XPATH,value = "//input[@name='departureDate']")
date.clear()
date.send_keys("28/02/2025")

driver.find_element(by=By.XPATH, value='//button[@type="submit"]').click()


price_container=driver.find_elements(by=By.XPATH, value = '//div[@class="flight-details false"]')

price_list=[]

for container in price_container:
    price =container.find_element(by=By.XPATH, value = './/div[@class="mobile-price col-xs-4 col-md-12 col-sm-12 col-lg-12 false"]').text

    unit_price=price.strip("NGM").replace(",","").replace("\n","")
    # price_list.append(float(unit_price))

    departure_time = container.find_element(by=By.XPATH, value = './/span[@class="departure-time"]')
    arrival_time = container.find_element(by=By.XPATH, value = './/span[@class="arrival-time"]' )
   
    flight_details = {
        "Arrival": arrival_time.text, 
        "Departure": departure_time.text, 
        "Price":float(unit_price)
        }
   
    price_list.append(flight_details)

# print(price_list)


def get_minimum_flight_price_details(details : list[dict]):
    minimum_price = min([detail["Price"] for detail in details])
    for detail in details:
        if minimum_price == detail["Price"]:
            return detail
        
print(get_minimum_flight_price_details(price_list))











