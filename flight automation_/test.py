
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


age = 50
name = "tunde"
info = f"student with firstname {name} is {age}" 

print(info)