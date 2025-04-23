print("Select your ride")
print("1. Bike")
print("2. Car")
print("3. Public")

ride = int(input("Ener the number of your ride: "))

if (ride == 1):
    print("What type of bike:")
    print("1. Sports bike.")
    print("2. Scooter")
    print("3. Motorcycle")

    bike = int(input("Enter the type of bike: "))
    if (bike == 1):
     print("You chose sports bike.")
    elif (bike == 2):
     print("You chose scooter.")
    else:
      print("You chose motorcycle")

elif (ride == 2):
    print("What type of car:")
    print("1. SUV.")
    print("2. Sedan")
    print("3. Sports car")

    car = int(input("Enter the type of car: "))
    if (car == 1):
     print("You chose SUV.")
    elif (car == 2):
      print("You chose Sedan.")
    else:
      print("You chose Sports car.")

else:
    print("What type of public:")
    print("1. train.")
    print("2. ferry")
    print("3. bus")

    pr = int(input("Enter the type of public: "))
    if (pr == 1):
      print("You chose train.")
    elif (pr == 2):
       print("You chose ferry.")
    else:
      print("You chose bus.")  

