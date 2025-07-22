unit = int(input("Enter your unit: "))


unit_2 = unit * 5
unit_3 = unit * 10
unit_4 = 10000



if(unit <=100 ):
    print("Your bill price will no chaarge: ")

elif(unit >= 100 and unit < 200):
    print("Your using unit bill: ", unit_2)

elif(unit >= 200 and unit <= 350):
   print("Your using unit bill: ", unit_3)

elif(unit >= 350):
    print("Your total unit bill is:", unit_4)
