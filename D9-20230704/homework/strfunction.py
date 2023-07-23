# word="hello,my name is vajeeha."
# convert 1 character in to uppercase(H)
# print(word.capitalize())

# convert lowercase
# print(word.casefold())

# space after charcter
# print(word.center(100))

# txt="He buyed a Apple,in a Apple shop,"
# no.of.times the specified value(apple) appears
# print(txt.count("Apple"))

# encoded version of string                             
# print(txt.encode())

# it returns true if the string ends with specified value(,)
# print(txt.endswith(","))

# txt="W\tE\tL\tC\tO\tM\tE\tV\tA\tJ\tE\tE\tH\tA"
# set tabsize to white spaces                            
# print(txt.expandtabs(6))

# find the index no of the specified value
# print(txt.find("shop"))

# shop="This Black dress is ${Ruppes:.1f}only"
# # #  format the specified value insert condition in blaceholder     
# print(shop.format(Ruppes=200))

#  txt={'a': "I am",'y':"fever"}
# return dictionary key value                           
# print("{a} Suffering from {y}".format_map(txt))


# txt="Hello this is Riya"
# it return the index position of the specified value
# print(txt.index("dubai"))

# it returns true if, all the charcters r alphanumeric  otherwise retrns false
# txt="vajeeha20"
# print(txt.isalnum())

# txt="VAJI"
# it returns true if, all the charcters r alphabet  otherwise retrns false
# print(txt.isalpha())

# isascii means charcters containing numbers,alphabet,special charcters
# print(txt.isascii())


# all the values in a string r decimals (true or false)
# print(txt.isdigit())

#check if all the values in a string r digit(True or false)
# print(txt.isdigit())

# a string contain A_Z,0_9,
# and underscore (true or false)
# print(txt.isidentifier())


# txt="hello,vajeeha"
# check the givern string contain only lowecase (abcd) (true or false)
# print(txt.islower()) 

# check the given string contain only numbers (15362574) (true or false)
# print(txt.isnumeric())

# returns true if the all the charcter r printable           
# print(txt.isprintable()) 

# returns true if the all the charcter r whitespces
# txt=" "
# print(txt.isspace())

# return true if the string contain uppercase letter
# txt="HELLO"
# print(txt.isupper())


# return true if the charcter strat with (A) uppercase letter
# str="My,name is vajeeha"
# print(str.istitle())


# str=("Aji","vaji","suji")
# it joins all items
# print("@".join(str))

# txt="Three"
# a=txt.ljust(22)
# returns 22 white spaces after the charcter
# print(a,"is my favourite movie")


# convert string into lowercase
# print(txt.lower())

# txt="     Hello"
# remove spaces of the left of the string
# a=txt.lstrip()
# print(f"{a} is a word" )


# txt="Hi Riya"
# set=txt.maketrans("R","M")                  
# print(txt.translate(set))

# str="OH Its very cold"
# it returns a charcter with 3 elements
# print(str.partition("very"))

# replace a specified charcter with another charcter
# print(str.replace("cold","hot"))


# searches a specifed value and  returns last position where it was found
# print(str.rfind("cold"))

# searches a specifed value and  returns last position where it was found
# print(str.rindex("very"))

# str="Nun"
# x=str.rjust(10)
# returns 10 white spaces before the word nun
# print(x,"is a horror movie")

# txt="She want to buy a jwellery,in a jwellery shop"         
# returns tuple whre str is partitioned into 3 parts                                                                    #  (doubt)
# print(txt.rpartition("jwellery"))


# txt="cow,cat,dog"
# it splits a str in to a list
# x=txt.rsplit(",")
# print(x)

