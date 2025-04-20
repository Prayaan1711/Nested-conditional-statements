units = int(input("Enter the units consumed: "))

if units<50:
    lb = (units*2.60)+25
    print(lb)

elif units < 100:
    lb = (units*3.25)+35
    print(lb)

elif units < 200:
    lb = (units*5.26)+45
    print(lb)

else:
    lb = (units*8.45)+75
    print(lb)