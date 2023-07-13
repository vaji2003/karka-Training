# list=[2,7,1,4,3]
# sum=0
# for i in list:
#     sum=sum+i
# print(sum)
# avg=sum/len(list)

list=[2,4,6,8,3,5,7]
sum=0
for i in list:
    print("before",sum)
    sum=sum+i
    print("After",sum)
enum_list=enumerate(list)
print(type(enum_list))
for i,list in enum_list:
    print("Entering iteration process :"+str(i))
    print("Before sum",sum)
    sum=sum+list
    print("After sum",sum)
    print("Exiting iteration process for item the:"+str(i))
    print("\n")



