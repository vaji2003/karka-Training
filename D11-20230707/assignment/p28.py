
curr_keychn=0
cost=10
sales_tax=8.25
ship_cost=5
add_per_key_cost=1
def add_key():
    global curr_keychn
    add=int(input(f"\nYou have {curr_keychn} keychains.How many to add:"))
    curr_keychn+=add
    print(f"You now have {curr_keychn} keychain.")  
def rem_key():
    global curr_keychn
    rem=int(input(f"\nyou have {curr_keychn} keychain .How many want to remove:"))
    if rem>curr_keychn:
       print(f"Error--> You have only {curr_keychn} keychain but u want to remove {rem} keychains")
    elif rem<=0:
       print("Enter valid number of keychain")
    elif rem<curr_keychn:
       curr_keychn-=rem
       print(f"You have now {curr_keychn} keychain")
def view_key():
    global curr_keychn
    print(f"you have {curr_keychn} keychain\nKey chain cost ${cost} per each.\nshipping charge is ${ship_cost}.\nAdd per keychain cost is ${add_per_key_cost}.\nTotal cost is {(cost*curr_keychn)+((add_per_key_cost*curr_keychn)+ship_cost)+(curr_keychn*cost*sales_tax/100)}") 
def chekout():
    name=input("\nEnter your name? ")
    print(f"you have {curr_keychn} keychain.\nkeychain cost ${cost} each.\nTotal cost is ${cost*curr_keychn}.\nThanks for u r order {name}.")  
while True:
    k=int(input("\nEnter your choice:"))
    if k==4:
      chekout()
      break
    elif k==3:
     view_key()
    elif k==2:
     rem_key()
    elif k==1:
     add_key()
    else:
       print("sorry,u r choice is wrong")
       break