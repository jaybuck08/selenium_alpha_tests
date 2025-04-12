

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
#  this prints the speccified os.environ variable "password" ....


# __________________________ # creating basic functions:

#  Let’s break it down **line by line** in the simplest way possible. Here's the same function that finds the product with the **lowest price** from a list of dictionaries — explained like you're brand new to Python. 😊


# ### 🧠 First, here's the function:

# ```python
# def get_min_price_product(products):
#     if not products:
#         return None
#     return min(products, key=lambda x: x['price'])
# ```


# #### `def get_min_price_product(products):`
# - This **defines a function** called `get_min_price_product`.
# - The function takes **one input**, a list called `products`.
# - Each item in the `products` list should be a **dictionary** with at least a `"price"` key.


# #### `if not products:`
# - This checks if the `products` list is **empty**.
# - In Python, `not products` means “if this list has nothing inside it…”


# #### `return None`
# - If the list is empty, we **stop the function** and return `None`.
# - That way we don’t try to search for a price in an empty list (which would cause an error).


# #### `return min(products, key=lambda x: x['price'])`
# - This line finds the item with the **lowest price**.
# - `min()` is a built-in Python function that returns the **smallest** item.
# - We're telling `min()` to compare the **'price'** inside each dictionary.


# #### `key=lambda x: x['price']`
# - This tells `min()` *how* to compare items.
# - `lambda x: x['price']` is just a quick way to say: “look at the `price` inside each item.”
# - So for each item (called `x`), it grabs `x['price']` to use for comparison.


# ### 🧪 Example for clarity:

# ```python
# products = [
#     {"name": "Shoes", "price": 45.99},
#     {"name": "Hat", "price": 15.49},
#     {"name": "Jacket", "price": 89.00}
# ]

# cheapest = get_min_price_product(products)
# print(cheapest)  # Output: {'name': 'Hat', 'price': 15.49}


