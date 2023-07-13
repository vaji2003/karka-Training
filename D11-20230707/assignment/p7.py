# height=float(input("Your height in m: "))
# weight=float(input("Your weight in kg: "))
# # print(f"BMI {weight/(height*height)}")
def cal_BMI (height,weight):
    return weight/(height**2)
# print(f"BMI {cal_BMI (height,weight)}")
