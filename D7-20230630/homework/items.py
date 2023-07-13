item1=int(input("Enter the amount of item1:"))
item2=int(input("Enter the amount of item2:"))
item3=int(input("Enter the amount of item3:"))
item4=int(input("Enter the amount of item4:"))
total=item1+item2+item3+item4
if total>500 and total<1000:
    print("silver tocken")
if total>=1000:
    print("Golden tocken")