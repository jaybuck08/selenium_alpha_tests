# https://ringmagazine.com/en/fighters
# locate to each fighter and print details


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
url = "https://ringmagazine.com/en/fighters"
driver.get(url)


fighters_container = driver.find_element(by=By.XPATH, value='//div[@class="mt-ringtvGapMobile grid grid-cols-12 gap-ringtvGapMobile md:gap-ringtvGapIpad xl:gap-ringtvGapIpad"]')
fighters = fighters_container.find_elements(by=By.XPATH, value='.//div[@class="col-span-12 flex flex-col justify-start gap-ringtvGapMobile overflow-hidden rounded-[2rem] bg-[#FFFBF1] p-4 sm:col-span-6 lg:col-span-4 xl:col-span-3 3xl:col-span-2"]')


for fighter in fighters:
     
    details = fighter.click()

    WebDriverWait(driver,10).until(ec.presence_of_all_elements_located((By.XPATH, '//button[@class="w-full rounded-[1.125rem] py-4 font-bold uppercase ar:font-arabicFont bg-ringtv-red text-white "]')))
    
    driver.back()
    time.sleep(5)
    
    # (By.TAG_NAME, "a" ).get_attribute("href")
    # print(details)

  

        
      
        