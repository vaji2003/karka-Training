import p7
height=float(input("Your height in m: "))
weight=float(input("Your weight in kg: "))

bmi=p7.cal_BMI(height,weight)
print(f"your BMI is {bmi} ")
if bmi<18.5:
    print(" BMI category:Under weight")
if bmi>18.5 and bmi<24.9:
    print(" BMI category:normal weight")
if bmi>25.0 and bmi<29.9:
    print("BMI category:Over weight")
if bmi>=30.0:
    print("BMI category:obese")

