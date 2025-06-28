
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
# names = input("firstname: ")

# #2 define vowels
# vowels = "aeiou"

# #3 create an empty list to store the vowels extracted
# vowel_list = []

# # # 4 Loop through each name and print
# for vowel_letters in names:
#     if vowel_letters in vowels:
#       vowel_list.append(vowel_letters)

# print(vowel_list)



# ____________________________# Assessment Task: Student Grade Processing System_________________________________________

# Write a Python program that simulates a basic student grade processing system with the following features:

#### *Requirements:*

# 1. *Define a function* process_students(data) that takes a list of student records. Each record is a dictionary containing:

#    * 'name': the student's name (string)
#    * 'scores': a list of integers representing test scores

#    Example input:

#    python
#    students = [
#        {"name": "Alice", "scores": [78, 85, 90]},
#        {"name": "Bob", "scores": [60, 65, 58]},
#        {"name": "Charlie", "scores": [95, 92, 88]},
#    ]
   

# 2. Inside the function, do the following *for each student*:

#    * Calculate the *average score*.
#    * Use conditionals to assign a *grade* based on the average:

#      * 90 and above: "A"
#      * 80–89: "B"
#      * 70–79: "C"
#      * 60–69: "D"
#      * Below 60: "F"
#    * Store and print a summary like:

#      plaintext
#      Alice - Average: 84.33 - Grade: B

# students = [
    
#         {"name": "Alice", "scores": [78, 85, 90]},
#         {"name": "Bob", "scores": [60, 65, 58]},
#         {"name": "Charlie", "scores": [95, 92, 88]},


#         ]

# def process_students(students):
   
#     summary = []
   
#     for candidate in students:

#         name = candidate["name"]
#         scores = candidate["scores"]
#         average =  sum(scores) / len(scores)

#         # print(average)

#         if average >= 90:
#             grade = "A"
#         elif average >= 80:
#             grade = "B"
#         elif average >= 70:
#             grade = "C" 
#         elif average >= 60:
#             grade = "D"
#         else:
#             grade = "F" 
        
#         summary_details = (f"{name} - Average: {average} - Grade: {grade}")
#         summary.append(summary_details)

#     return (summary)
        

# summary = process_students(students)
# print(summary)


#____________________________exercise________________________________________________  
      
# Extract a number from the terminal, convert to an integer and divide by 2

# password = input("code: ")
# output = int(password)
# result = output/2

# print(result)

#_______________arithmetic assignment (%= or -= or += or etc)____________________________
# age = 20
# age += 10
# print(age)

# the below divides and does not give a remainder beacuse of the double slash
# age = 21 // 2 
# print(age)

#___________escape characters (\n, end=, \t, + (used to join strings together), etc)____________________________
# print("Hello \n World") # prints world in a new line
# print ("world")


#_____________DATA Structures in Python___________________

# Built in:

# Mutable (values can be edited)
# 1. List [uses square brackets] --> (and is an ordered collection)    e.g.  names = ["John", "Mary"]

    # names.append (adds one value at a time) e.g. names.append = ["mary","john"]
    # names.extend (adds multiple values in a list or curved bracket) e.g. names.extend = [{"john","mary"}]
    # names.remove = ["John"] or names.pop(0)  --- used to remove by values or index respectively
    # names.clear (this clears the list) etc.
    # names.insert (this adds a value or number to a specific place on the list)
    

    # statistics = [23, 99, 900, 34, 55]
    # statistics.sort(reverse=True)
    # print(statistics)

    # statistics.reverse()
    # statistics.sort(reverse=True)

    # it is very important to note that DATA STRUCTURES do not create copies but strings CREATES COPIES when using a variable multiple times***

    #______________exercise__________________
    # create a list of random data and use the for loop to print out only string values.

    # mixed_bag = [12,"john", "apple", 35, "red", True, False, 9000]
    # new_bag = []

    # for values in mixed_bag:
    #     if type(values) == str:
    #         new_bag.append(values)
    # print(new_bag)

    #______________exercise__________________
    # write a python program that takes a list of numbers [30, 2, 31, 4, 0, 11, 16, 98].
    # check if number is an even number, if not, add 1 to it and print a new sorted list

    #     random_bag = [30, 2, 31, 4, 0, 11, 16, 98]
    # new_bag = []

    # for numbers in random_bag:
    #     if numbers % 2 == 0:
    #         new_bag.append(numbers)

    #     else:
    #         new_bag.append(numbers + 1)

    # new_bag.sort()
    # print("Answer", new_bag)

    
      
# 2. Dictionary {uses curly brackets} --> (and has key pair value)

    # user_info = {"name": "james", "age": 32, "dob":"1st March 1994"}

    # user_info ["dob"] = "email"  ..... #add new value to the dictionary

    # ____________________exercise________________________
    # write a python script that takes a list containing mixed data types (integers, strings, float, boolean) & peform the following:
    # return a dictionary with 3 keys: numbers (integers & floats) in ascending order
    # strings: all stings coverted to uppercase
    # sum_numbers: sum of all numeric values (integers & floats)

    # mixed_data = [1,11, 12.0, 3.5, "giancarlo", "martini", True, False]

    # numbers = [] #  or result["numbers"] = []  ---- this could be better when dealing with dictionaries
    # strings = []
    # boolean = []

# creating a dictionary
    # result = {"numbers": [], "strings": [], "boolean":[], "sum_numbers": 0 }

    # for items in mixed_data:
    #     if type (items) == int or type(items) == float:
    #         result["numbers"].append(items)
        
    #     elif type(items) == bool:
    #         result["boolean"].append(items)

    #     elif type (items) == str:
    #         result["strings"].append(items.upper())


    # result["sum_numbers"] = sum(result["numbers"])
    # print(result)


# 3. sets --> (unordered but cannot have repeated value)

    # names = {"john","james","mary"}
    # surnames = {"james", "jack "joan"}

    # # valu = names.copy() ---- this assigns names to valu as a copy. THis means that the original name can still be called later and remains unchanged.
    # # value = set() ---- this means an empty set

    # print(names.difference(surnames)) # means what is available in names that is not in surnames
    # intersection, symmetric_difference and union are also methods. 
    # pop removes a random value but remove takes away a specific value
    



# Immutable (cannot be edited)
# 4. Tuple --> (ordered collectiton)

    # names = ("john","james","mary")
    # othernames = ("mary","josiah")

    # Tuple has two methods; count and list

    # print(names.count("john"))
    # print(len(names))
    # print(names.index("john"))

    # print(names+othernames)   # merging two Tuples to create a new one


# other data structures (not built in):
# stacks, queues, trees, graphs, linked list.



