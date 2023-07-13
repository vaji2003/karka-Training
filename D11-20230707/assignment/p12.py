quiz=input("Are u ready for a quiz?")
s=0
if quiz=="yes":
    print("ok! Here it comes.")
    a=int(input("What is the capital of Alaska? \n 1.Melboourne \n 2.Anchorage \n 3.Juneau \n"))
    if a==3:
        print("Thats right")
        s+=1
        print('\n')
    else:
        print("Thats wrong")

    b=int(input("Can u store the value of cat in a variable of type int? \n 1: Yes\n 2: No \n" )) 
    if b==1:
        print("sorry cat is a string ints can only store variables")
        s+=1
    else:
        print(" ")
    age=int(input("what is the result of 9+6/3? \n 1:5 \n 2:11 \n 3:15/3 \n"))
    if age==1:
         print("Thats right")
         s+=1
    print(f"Over you got {s} out of 3 correct \n Thanks for playing")
else:
    print("sorry u lost")




