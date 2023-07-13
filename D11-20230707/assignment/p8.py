name=input("Hey! Whats u r name? ")
print('\t')
age=int(input(f"ok! How old are you? "))
print('\t')
if age<16:
        print(f"You cant drive")
if age<18:
        print(f"You can't vote ,{name}.")
if age<25:
        print(f"You cant rent a car ,{name}.")
if age>=25:
        print("You can do anything thats legal")

