first_input=int(input("Enter the number:"))
second_input=int(input("Enter the number:"))
third_input=int(input("Enter the number:"))
# sum=0
# if first_input>=sum:
#     sum=first_input 
# if second_input>=sum:
#    sum=second_input
# if third_input>=sum:
#    sum=third_input
# print("largest number is ",sum)


# for inputs in (first_input,second_input,third_input):
#     if inputs>=sum:
#         sum=inputs
# print(sum)
if first_input>second_input:
    if first_input>third_input:
        print(f"{first_input}")
    else:
        print(f"{third_input}")
elif second_input>third_input:
    print(f"{second_input}")
else:
    print(f"{third_input}")
list=[first_input,second_input,third_input]
