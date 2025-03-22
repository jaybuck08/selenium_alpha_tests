def check_if_value_in_select(items, value):
    new_options = []

    for option in items:
        new_options.append(option.get_attribute("value"))
    
    return value in new_options
