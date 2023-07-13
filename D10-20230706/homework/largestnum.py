# numbers=[200,500,550,300,700,750,2000]
# empty=0
# for value in numbers:
#     if value>empty:
#         empty=value
# print("largest value:",empty)

list=[2,6,9,1,5]
empty=0

def largest(list,empty):
    for num in list:
        if num>empty:
            empty=num
    return empty

print(largest(list,empty))



    