gender=input("What is u r gender (M or F):")
fname=input("firstname:")
lastn=input("last name:")
age=int(input("age:"))
if gender=="F" and age>=20:
  marriege=input(f"Are u married,{fname} yes or no?")
  if marriege=="yes":
    print(f" Then i shall call u Mrs  {lastn}")
  if marriege=="no":
   print(f"Then i shall call u MS {lastn}")


elif gender=="M"  and age>20:
  print(f" Then i shall call u Mr {fname}")
elif gender=="M" and age<20:
  print(f"Then i shall call u {fname}+{lastn}")


