weight=int(input("Please enter your current earth weigth:"))
print('\t')
print("I have information from the following planet:")
print("\t 1. venus \t 2.Mars \t 3.Jupiter")
print("\t 4.saturn \t 5.Uranus \t 6.Neptune")
visit=int(input("Which planet are you visiting?"))
venus=0.78
mars=0.39
jupitor=2.65
saturn=1.17
uranus=1.05
neptune=1.23
if visit==1:
    print(f" Your weight would be {weight*venus} on the planet")
elif visit==2:
    print(f"Your weight would be  {weight*mars} on the planet")
elif visit==3:
    print(f" Your weight would be  {weight*jupitor} on the planet")
elif visit==4:
    print(f" Your weight would be  {weight*saturn} on the planet")
elif visit==5:
    print(f" Your weight would be  {weight*uranus} on the planet")
elif visit==6:
    print(f" Your weight would be  {weight*neptune} on the planet")

