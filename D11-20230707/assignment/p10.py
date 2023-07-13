name=input("Hey whats u r name? (sorry,i keep forgetting.)")
age=int(input(f"ok!{name},How old are you?"))
if age<16:
    print("You cant drive.")
elif age==16 or age==17:
  print(f"You can drive but you can't vote.{name}")
elif age==18 and age==24:
    print("You can vote but not rent a car.")
else:
    print("you can do pretty much anything")