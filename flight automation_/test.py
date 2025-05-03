
# arik = {'flight': 'arik', 'details': {'Arrival': '16:25', 'Departure': '15:10', 'price': 89381.0}}

#     # use 1
# price = arik["details"]['price']
# print(price)

    # or use 2 below. gives same result

# def get_price(arg):
#     # Extract price from dictionary
#     price = arg.get("details").get("price")
#     return price

# print(get_price(arik))


# age = 50
# name = "tunde"
# info = f"student with firstname {name} is {age}" 

# print(info)

#__________

#  use the below script if you need to read another file into your current file
with open ("write article or file name here.txt") as file:
    result = file.read()


# _________________________Variables_____________________________________

# constant variables do not change. Python doesnt necessarily have constant variables (you can put constant variables in all caps) but javascript does

# _____# varaibles in python:

# strings = "john" (must be in quotes)  # interger = 28    # float = 3.5 (floats must have desimal points)   # boolean = False    # complex = 2j

# _name = single underscore means a protected variable   __name = double underscore means  a private variable - both work normally but when used in classes fxn as protected & private
#  local variables are defined within a function or class (withib a block). Global variables can be anywhere in the script, within & outside functions & classes.


# _________________________Srings________________________________________

# full_name = " John Doe"

# print(full_name[1:3])               # slicing
# print(full_name[1])                 # indexing
# print(full_name[-1])                # negetive indexing (starts from the opposite direction of indexing)
# print(full_name[1::3])              # this starts from the second alphabet and skips 3 before listing the next alphabet
# print(full_name.center(50,"*"))     # "." gives you options to choose from like capitalise(), center(), isnumeric(), startswith(), count(), find(), 
#                                      strip() - this removes whitespaces or characters specified etc.

football_name = "michael angelo"

# print(len(football_name))
# print(football_name[::3])
# print(football_name[4])
# print(football_name[4:5])
# print(football_name[8:])
# print(football_name[-6::1])
# print(football_name[5::-2])

#1
NAME = "anabella"

if NAME.startswith("a"):
    NAME = NAME.upper()

print(NAME)

#2
if NAME[0].islower():
    print("first letter is lowercase")
else:
    print("first lteer is not lowercase")
