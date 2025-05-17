from aeroairline_auto import aeroautomation
from arik_auto import arikFlightAutomation
from minimum_price import get_minimum_flight_price_detail

LOC = "ABV"
DES = "LOS"
DEPDATE = "22/07/2025"


result1 = aeroautomation(LOC,DES,DEPDATE)
print(result1)

result2 = arikFlightAutomation(LOC,DES,DEPDATE)
print(result2)


# cheapest_flight = get_minimum_flight_price_detail([result1,result2])
# print(cheapest_flight)

def get_price(arg):
    price = arg.get("details")

    if not price:
        return 999999999999
    
    return price.get("price")

    # "min" is used to extract/recognises only numbers/ integer value.
    # "lambda" was used to compare results 1 & 2 and extracts only price. it is used to call a function without explicitly defining it.
cheapest = min(
    [result1,result2],
    key = lambda value : get_price(value)  
)

print(cheapest)