
curr_keychn=0
cost=10
sales_tax=8.25/100
ship_cost=5
add_per_key_cost=1
def add_key():
    add=int(input(f"\nYou have {curr_keychn} keychains.How many to add:"))
    curr_keychn+=add
    print(f"You now have {curr_keychn} keychain.")  
def rem_key():
    global cur_keychn
    rem=int(input(f"\nyou have {curr_keychn} keychain .How many want to remove:"))
    if rem>curr_keychn:
       print(f"Error--> You have only {curr_keychn} keychain but u want to remove {rem} keychains")
    elif rem<=0:
       print("Enter valid number of keychain")
    else:
       return curr_keychn-rem
    #    print()   
def view_key():

    print(f"you have {curr_keychn} keychain\nKey chain cost ${cost} per each.\nshipping charge is {salex_tax}{cost*curr_keychn} after tax is {cost*curr_keychn*sales_tax}") 
    # print(f"{curr_keychn} keychains in the order\nThe prize per keychain is {per_cost}\nship charge of a order is ${sales_tax}")

def chekout():
   
    name=input("\nEnter your name? ")
    print(f"you have {curr_keychn} keychain.\nkeychain cost ${cost} each.\nTotal cost is ${cost*curr_keychn}.\nThanks for u r order {name}.")  
while True:
    k=int(input("\nEnter your choice:"))
    if k==1:
     add_key()
    elif k==2:
     rem_key()
    elif k==3:
     view_key()
    elif k==4:
     chekout()
     break
    elif k>=5:
       break
