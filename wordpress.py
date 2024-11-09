from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from dotenv import load_dotenv

# used to import all varaiables to your file
import os

load_dotenv()


# set options to make browser not to close
options = Options()
options.add_experimental_option("detach", True)

url = os.environ["url"]

# add "option=options" below
driver = webdriver.Edge(options=options)
driver.maximize_window()

driver.get(url)

# access_code = driver.find_element(By.CLASS_NAME, value="form-control")
# access_code.send_keys(607)
# access_code.send_keys(Keys.ENTER)

wordpress_username = driver.find_element(By.XPATH, "//input[@type='text']")
wordpress_username.send_keys(os.environ["user"])
wordpress_password = driver.find_element(By.ID, value="user_pass")
wordpress_password.send_keys(os.environ["password"])

wordpress_password.send_keys(Keys.ENTER)

driver.find_element(By.XPATH, f"//a[@href='{url}post-new.php']").click()

add_title_cover = driver.find_element(By.CLASS_NAME, value="block-editor-iframe__container")

i_frame = add_title_cover.find_element(By.XPATH, ".//iframe[@name='editor-canvas']")

# use this below to switch the driver to other sections like; alert, i-frame etc. this means that if "driver." is used, it will be searching for elements within "alert, i-frame, etc" only. 
# in other words it will take "alert, i-frame, etc"" as the driver until is is reverted..

driver.switch_to.frame(i_frame)

body = driver.find_element(By.XPATH, ".//div[@class='editor-visual-editor__post-title-wrapper edit-post-visual-editor__post-title-wrapper']")

add_title = WebDriverWait(body,20).until(ec.presence_of_element_located((By.TAG_NAME, "h1")))                                                                                  
add_title.send_keys("We Are The Champions")

content = driver.find_element(By.TAG_NAME, "p")
content.send_keys("one for the road")


# use this to go back to default driver
driver.switch_to.default_content()


publish = driver.find_element(By.XPATH, "//button[@class='components-button editor-post-publish-panel__toggle editor-post-publish-button__button is-primary is-compact']")
publish.click()

publish_2 = driver.find_element(By.XPATH, "//button[@class='components-button editor-post-publish-button editor-post-publish-button__button is-primary is-compact']")
publish_2.click()


view_post = WebDriverWait(driver,40).until(ec.presence_of_element_located((By.XPATH, "//a[@class='components-button is-primary']")))
view_post.click()



