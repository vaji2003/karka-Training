consumer_data = {"consumer_name": "vajeeha","eb_reading": [1100, 1200, 1350, 1650, 2050]} 
import json
def calculate_electricity_bill(consumer_data):
    list=[ ]
    reading=consumer_data['eb_reading']
    for i in range(1,len(reading)):
        dict_view={
                    "month":0,
                    "unit":0,
                    "amount":0
                    }
        rs=0
        difference=reading[i]-reading[i-1]
        if difference<100:
            print("no amount")
        elif difference>=100 and difference<200:
            rs=difference*2   
        elif difference>=200 and difference<500:
            rs=difference*5  
        elif difference>500 and difference<1000:
            rs=difference*10 
        elif difference>1000:
           rs=difference*14   
        dict_view["month"]= i
        dict_view["unit"]=difference
        dict_view["amount"]=rs
        list.append(dict_view)
    return list
calling=calculate_electricity_bill(consumer_data)
str_list=str(calling)
choice=input("Enter u r choice:")
change=choice.upper()
if change=="DICT":
    print(calling)
elif change=="JSON":
    jsons=json.dumps(str_list)
    print(jsons)
# myfile=open("/home/vagiha/vaji/vajeehaebill.txt","w")
# myfile.write(str_list)
# myfile.close()