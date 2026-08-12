def calculate_total(topping_count):
    while True:
        topping_count = input("Add topping or are you done?")
        if topping_count == ("pepperoni") or ("mushroom") or ("extra cheese"):
            return
        elif topping_count == ("Done"):
            break
        else:
            result print("not applicable")