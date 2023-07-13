print("Ye oldy keychain shop")
curr_keychn=0
cost=10
def add_key():
    global curr_keychn
    add=int(input(f"\nYou have {curr_keychn} keychains.How many to add:"))
    curr_keychn+=add
    print(f"You now have {curr_keychn} keychain.")  
def rem_key():
    global curr_keychn
    rem=int(input(f"\nyou have {curr_keychn} keychain .How many want to remove:"))
    curr_keychn-=rem
    print(f"You now have {curr_keychn}")  
def curr_key():
    global curr_keychn
    print(f"you have {curr_keychn} keychain\nKey chain cost ${cost} each.\nTotal cost is {cost*curr_keychn}") 
def chekout():
    global curr_keychn
    global cost
    print("\nCHECKOUT")
    name=input("\nEnter your name? ")
    print(f"you have {curr_keychn} keychain.\nkeychain cost ${cost} each.\nTotal cost is ${cost+curr_keychn}.\nThanks for u r order {name}.")  
for i in range(5):
    print("\n\n1:Add keychain to order\n2:remove keychain from order\n3:view current order\n4:checkout")
    k=int(input("\nEnter your choice:"))
    if k==1:
     add_key()
    elif k==2:
     rem_key()
    elif k==3:
     curr_key()
    elif k==4:
     chekout()
     break
    elif k>=5:
       break
