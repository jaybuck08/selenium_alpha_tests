
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
# with open ("write article or file name here.txt") as file:
#     result = file.read()


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
# NAME = "anabella"

# if NAME.startswith("a"):
#     NAME = NAME.upper()

# print(NAME)

# #2
# if NAME[0].islower():
#     print("first letter is lowercase")
# else:
#     print("first lteer is not lowercase")


# __________using print, sep, end ________________________________________________

# message = "Hello World"
# name = "John"
# print(message, "How are you doing", name, sep=",")

# "\n" ---new line character
# "end=*"   --- this ensures the end of the word ends with an "*". if nothing is added, it ends with a space.
# sep="," : this is used to seperate each entry of the output with a "," or whatever is put in there

# age = int(input("Enter your age: "))
# print(type(age))

# ____exercise_____________

# get an input of username and check if name is fully aplphabet
# else print name is invalid

# username = input("name: ")

# if username.isalpha(): 
#     print(username,"name is valid",sep="***")

# else:
#     print("name is invalid")


# ____exercise______________

#1 get an input of a combination of names with valid and invalid names
# namebasket = input("names: ")

# #2 split names to valid & invalid. This splits the names from the commas. if its a "." between the names, it will split from that
# names = namebasket.split(",")

# #3 create an empty list 
# valid_names=[]

# #4 check for valid names and put in new list
# for name in names:
#     if name.isalpha():
#         valid_names.append(name)
    
# #5 print the valid names
# print(".".join(valid_names))
# print("here are the alphabetical names:",valid_names)


#____exercise_________________

# write a program that loops through names and extracts the vowels
# put in a list and print out.

# 1 get an input of names
names = input("firstname: ")

#2 define vowels
vowels = "aeiou"

#3 create an empty list to store the vowels extracted
vowel_list = []

# # 4 Loop through each name and print
for vowel_letters in names:
    if vowel_letters in vowels:
      vowel_list.append(vowel_letters)

print(vowel_list)
