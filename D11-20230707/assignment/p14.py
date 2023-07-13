print("!!WELCOME TO KARKA TINY ADVENTURE!!")
a=input("""\nYou are in a creepy house! would u like to go "upstrains" or into the "Kitchen"?\n""")

if a=="upstrains":
    d=input("""You hava a parashuit ,and You like to fall from the upstrains?" 1:yes or 2:no \n""")
    if d=="yes":
     print("Finall u escape\n")
    elif d=="no":
       print("U lose")
if a=="kitchen":
   b=input("""\nThere is a long countertop with dirty dishes everywhere. off to one side 
there is as you'd expect, a refrigerator. You may open the "refrigerator" or look in a "cabinet".\n""")
   if b=="refrigerator":       
    e=input("""\nInside the refrigerator u can see food and stuff. It looks pretty nasty.
Would u like to eat some of the food? ("yes or "no")\n""")     
    if e=="no":
      print("\n You die of starvation......eventually.")
    elif e=="yes":
     print("Finally u win the adventure")




