medical_cause = input("Enter if you have a medical cause in Y or N : ")
attend = int(input("Enter your attendence: "))

if medical_cause == 'Y':
    print("You are allowed.")

elif attend >= 75:
    print("You are allowed.")

else:
    print("You are not allowed.")