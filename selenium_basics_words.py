

# use this below to switch the driver to other sections like; alert, i-frame etc. this means that if "driver." is used, it will be searching for elements within "alert, i-frame, etc" only. 
# in other words it will take "alert, i-frame, etc"" as the driver until is is reverted.

#driver.switch_to.frame(i_frame)

#________________________________________________________________________________________

# use this to go back to default driver

#driver.switch_to.default_content()


# the ".env" file is used to store variables that will only appear in your local storage. It is designed not to be stored in Github
# the ".gitignore" file is used to hide/ignore files or folders only

# use the below to load the ".env" file
# "from dotenv import load_dotenv"
# use "load_dotenv()" after "rom dotenv import load_dotenv" to run the .env file


# the below is used to import all varaiables to your file
# import os

# print(os.environ)
# this prints all environment variables

# print(os.environ["password"])
#  this prints the speccified os.environ variable "password" ...