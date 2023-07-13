print("Ye oldy keychain shop")
def add_key():
    print("\n 1.Add key chain")  
def rem_key():
    print("\n 2.Remove keychin ")
def curr_key():
    print("\n 3. view order")  
def chekout():
    print("\n 4.checkout")
for i in range(8):
   print("\n\n1:Add keychain to order\n2:remove keychain from order\n3:view current order\n4:checkout")
   k=input("\nEnter the number:")
   if k=="1":
    add_key()
   elif k=="2":
    rem_key()
   elif k=="3":
    curr_key()
   elif k=='4':
    chekout()
    break










   