
###### task: remove the dollar sign and the comma


# funds = ["$10,000", "$20,000", "$30,000"]

# print(funds)

# result = []

# for amount in funds:
#     cash = amount.replace(",","").replace("$","")

#     result.append(int(cash))

# print(result)


       
###### task: remove the dollar sign, space and the comma


# more_funds = ["$ 10,000.43", "$ 20,000.47", "$ 30,000.43"]
  
# print(more_funds)

# result = []

# for ego in more_funds:
#     new_money = ego.replace(",","").replace("$ ","")

#     result.append(float(new_money))

# print(result)


names = ["john", "james", "joan"]

result = []

for name in names:
    sentence_case = name.capitalize()
    result.append(sentence_case)

print(result)

###### or, it can be compressed below:

sentence_case = [name.capitalize() for name in names]
print(sentence_case)