name=input("Hello.  What is u r name? ")
age=int(input(f"Hi,! How old are you? "))
# print(f"Did you know that in five years you will be {age+5}years old? And five years ago you were {age-5}! Imagine that!")
def after(age):
    age+=5
    return age
def  before(age):
    age-=5
    return age
a=after(age)
b=before(age)
print(f"""Did you know that in five years you will be {
    a} years old and five years ago you were {b} ! Imagine that !""")
