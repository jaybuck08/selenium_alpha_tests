from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select
from minimum_price import get_minimum_flight_price_detail
from avaliable_flights import check_if_value_in_select


def aeroautomation(location, destination, depdate):


# set options to make browser not to close
    options = Options()
    options.add_experimental_option("detach", True)

    driver = webdriver.Edge(options=options)
    url = "https://flyaero.com/"
    driver.get(url)



# select state for outbound flight
    departure_state = driver.find_element(by=By.XPATH,value = '//select[@name="depPort"]')
    departure_selection = Select(departure_state)

     # this checks if the location inserted is in the list
    if not check_if_value_in_select(departure_selection.options, location):
        return "location unavilable"

    
    departure_selection.select_by_value(location)


# select state for inbound flight
    arrival_state = driver.find_element(by=By.XPATH,value = '//select[@name="arrPort"]')
    arrival_selection = Select(arrival_state)

    # this checks if the destination inserted is in the list
    if not check_if_value_in_select(arrival_selection.options, destination):
        return "destination unavailable"

    
    arrival_selection.select_by_value(destination)


# format date field to remove it from read only (javascript code)
    driver.execute_script("date = document.getElementsByClassName('input-date')[0]; date.removeAttribute('readonly')")


# select flight date
    date = driver.find_element( by=By.XPATH,value = "//input[@name='departureDate']")
    date.clear()
    date.send_keys(depdate)

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
            "price":float(unit_price)
            }
    
        price_list.append(flight_details)

    driver.quit()
    

    return {"flight": "arik", "details": get_minimum_flight_price_detail(price_list)}

# print(aeroautomation("ABV","LOS","22/04/2025"))














