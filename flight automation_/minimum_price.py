


# def get_minimum_flight_price_details(details : list[dict]):
#     minimum_price = min([detail["Price"] for detail in details])
#     for detail in details:
#         if minimum_price == detail["price"]:
#             return detail
        






def get_minimum_flight_price_detail(details : list[dict]):
    prices = []

    for detail in details:
        prices.append(detail["price"])

    minimum_price = min(prices)
    
    for detail in details:
        if minimum_price == detail["price"]:
            return detail