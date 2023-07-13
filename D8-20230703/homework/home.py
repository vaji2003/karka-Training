a=int(input("Enter the number:"))
b=input("Enter the operator")
c=int(input("Enter the number:"))
def sub(num1,operation,num2):
    if operation=="*":
      return num1*num2
    if operation=="-":
      return num1-num2
    if operation=="+":
      return num1/num2
    if operation=="**":
     return num1**num2
    if operation=="%":
      return num1%num2
    if operation=="/":
      return num1/num2
total=sub(a,b,c)
print("Total:",total)
