# Assignment M03 SDEV 220 CAR STUFF
# Author: Carey Armstrong
# Version: 2.0
# Date: 2024-11-04
# Initialize Vehicle class
class Vehicle:
    def __init__(self, typeveh):
        self.typeveh = typeveh

# Initialize Automobile class
class Automobile(Vehicle):
    def __init__(self, typeveh, year, make, model, roof_type: int, door_number: int):
        super().__init__(typeveh)
        self.year = year
        self.make = make
        self.model = model
        self.roof_type = roof_type
        self.door_number = door_number


# Function to get the vehicle type & validate that it is a car and exit if not
def get_vehcle_dta():
    listcarvalid = ["car", "CAR", "cAr", "CAr", "caR"]
    typeveh = input("Enter the type of vehicle: ")
    if typeveh not in listcarvalid:
        print("Thanks for using our program!!")
        quit(0)
    else:
        return typeveh

# Function to get the data on the particular car, with some error
# checking to make sure that at least the entries are numbers
def get_car_dta():
    global roof
    global doors
    typeveh = get_vehcle_dta()
    try:
        year = int(input("Enter the car year manufactured: "))
    except:
        print("Not a valid year")
        year = int(input("Enter the car year manufactured: "))
    make = input("Enter the car make: ")
    model = input("Enter the car model: ")
    try:
        roof_type = int(input("Enter the type of roof - 1 for sunroof, 2 for regular: "))
    except:
        print("Not a valid entry for roof type")
        roof_type = int(input("Enter the type of roof - 1 for sunroof, 2 for regular: "))
    if roof_type == 1:
        roof = "Sun Roof"
    elif roof_type == 2:
        roof = "Regular roof"
    try:
        door_number = int(input("Enter the number of doors - 2 for coupe, 4 for sedan: "))
    except:
        print("Not a valid entry for number of doors")
        door_number = int(input("Enter the number of doors - 2 for coupe, 4 for sedan: "))
    if door_number == 2:
        doors = "Coupe"
    elif door_number == 4:
        doors = "Sedan"
    return typeveh, year, make, model, roof, doors


# Function to put the other functions together/main function
if __name__ == "__main__":
    carout = Automobile(*get_car_dta())
    print(
        f"Vehicle type: {carout.typeveh}\n Car year: {carout.year}\n Car Model: {carout.model}\n Roof Type: {carout.roof_type}\n Doors: {carout.door_number}")
