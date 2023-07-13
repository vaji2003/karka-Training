def area_t ():
    num1=int(input("Enter the number: "))
    num2=int(input("Enter the number: "))
    num3=int(input("Enter the number: "))
    s=(num1+num2+num3)/2
    return (s*(s-num1)*(s-num2)*(s-num3))**2

con=input("Enter function:")

def fnd_area():
    num4=int(input("Enter the number:"))
    return num4*num4


def rectangle():
  length=int(input("Enter the number:"))
  breadth=int(input("Enter the number:"))
  return length*breadth


def fnd_circle():
    circle=int(input("Enter the number:"))
    return 3.14*circle*circle 




def trapezium():
    a=int(input("Enter the number:"))
    b=int(input("Enter the number:"))
    h=int(input("Enter the number:"))
    return int((a+b)/2)*h





if con=='1':
    print(area_t())
elif con=='2':
    print(fnd_area())
elif con=='3':
    print(rectangle())
elif con=='4':
    print(fnd_circle())
elif con=='5':
    print(trapezium())




