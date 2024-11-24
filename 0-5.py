import os

AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Rivian R1T', 'Ram 1500']

if not os.path.isfile("AllowedVehiclesList.txt"):
    with open("AllowedVehiclesList.txt", "x") as db:
        db.close()

def updateList():   
    with open("AllowedVehiclesList.txt", "w") as db:
        db.write(str(AllowedVehiclesList))
        db.close()
    
def startProgram():
    print("\n********************************")
    print("AutoCountry Vehicle Finder v0.5")
    print("********************************")
    print("Please Enter the following number below from the following menu:")
    print("\n1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. DELETE Authorized Vehicle")
    print("5. Exit")

while True:
    startProgram()
    updateList()
    response = input("")
    if (response == "1"):
        print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
        for cars in AllowedVehiclesList:
            print(cars)      
    if (response == "2"):
        make = input('\nPlease Enter the full Vehicle name: ')
        if make in AllowedVehiclesList:
            print(f'{make} is an authorized vehicle')
        else:
            print(f'{make} is not an authorized vehicle, if you received this in error please check the spelling and try again')
    if (response == "3"):
        newVehicle = input("\nPlease Enter the full Vehicle name you would like to add: ")
        AllowedVehiclesList.append(newVehicle)
        print(f'\nYou have added "{newVehicle}" as an authorized vehicle')
    if (response == "4"):
        removeVehicle = input("\nPlease Enter the full Vehicle name you would like to REMOVE: ")
        areYouSure = input(f'Are you sure you want to remove "{removeVehicle}" from the Authorized Vehicles List?\n')
        if (areYouSure == "yes"):
            AllowedVehiclesList.remove(removeVehicle)
            print(f'You have REMOVED "{removeVehicle}" as an authorized vehicle')
        else:
            continue     
    if (response == "5"):
        print("\nThank you for using the AutoCountry Vehicle Finder, good-bye!")
        break