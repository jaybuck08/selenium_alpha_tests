from aeroairline_auto import aeroautomation
from arik_auto import arikFlightAutomation
from minimum_price import get_minimum_flight_price_detail

LOC = "ABV"
DES = "LOS"
DEPDATE = "24/03/2025"


result1 = aeroautomation(LOC,DES,DEPDATE)
print(result1)

result2 = arikFlightAutomation(LOC,DES,DEPDATE)
print(result2)


cheapest_flight = get_minimum_flight_price_detail([result1,result2])
print(cheapest_flight)

