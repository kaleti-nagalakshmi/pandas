number_1 = int(input("Enter first Number:"))
number_2 = int(input("Enter second Number:"))

print("1.addition")
print("2.subtraction")
print("3.multiply")
print("4.division")
print("5.square")

choose_number = int(input("enter your choose (1-5):"))

if choose_number==1:
    print(f"addition:{number_1+number_2}")
elif choose_number==2 :
    print(f"subtraction:{number_1-number_2}")
elif choose_number==3 :
    print(f"multiply:{number_1*number_2}")
elif choose_number==4 :
    print(f"division:{number_1/number_2}")
elif choose_number==5 :
    print(f"square:{number_1**number_2}")
else :
    print("invalid number")

