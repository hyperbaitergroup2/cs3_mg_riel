def calculate_space_weight(earth_weight, destination):
    if destination == ("Mars"):
        spaceweight = earth_weight * 0.38 
        return print(spaceweight)
    elif destination == ("Jupiter"):
        spaceweight = earth_weight * 2.34
        return print(spaceweight)
    elif destination == ("Moon"):
        spaceweight = earth_weight * 0.16
        return print(spaceweight)
    else:
        return print("Not Applicable")
        
print(calculate_space_weight(110,"Moon"))
def main():
    destination = input("What moon/planet are you from? ")
    earth_weight = int(input("What is your weight on earth? "))
    calculate_space_weight(earth_weight, destination)
    
    
main()