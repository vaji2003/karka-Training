
number=int(input("Enter the number:"))
def find_year(number):
     if number==1:
         return "january" 
     elif number==3:
          return"march"
     elif number==4:
         return("april")
     elif number==5:
      return("may")
     elif number==6:
        return("june")
     elif number==7:
        return("july")
     elif number==8:
        return ("august")
     elif number==9:
         return ("september")
     elif number==10:
         return("october")
     elif number==11:
        return ("november")
     elif number==12:
         return ("december")
     else:
         return("error")

print(find_year(number))