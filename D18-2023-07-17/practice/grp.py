stud_list=[{"name":"robin", "place":"Thirunelveli","hobbie":"playing","sslc":{"maths":99,"english":100,"Tamil":95,"science":90,"social":90}},
       {"name":"subin","place":"parvathipuram","hobbie":"playing","sslc":{"maths":80,"english":70,"Tamil":95,"science":90,"social":70}},
       {"name":"sreeram" ,"place":"Thaamaraikulam","hobbie":"movie","sslc":{"maths":60,"english":90,"Tamil":89,"science":100,"social":60}},
       {"name":"supriya" ,"place":"ganeshpuram","hobbie":"drawing","sslc":{"maths":99,"english":90,"Tamil":87,"science":60,"social":90}},
       {"name":"valliyammal", "place":"krishnakovil","hobbie":"playing","sslc":{"maths":90,"english":100,"Tamil":90,"science":50,"social":90}}]
for list in stud_list:
    marks=list["sslc"]   
    total=marks['maths']+marks['english']+marks['Tamil']+marks['science']+marks['social']
    percentage=((total/len(marks))*100)
  
    print(f"\n{list['name']},'ns total SSLC marks is ({total}) and percentage is ({percentage}) and maths mark is ({marks['maths']})")
    if percentage>90 or  percentage>75 and marks['maths']>=98:
        print(f"\n{list['name']} is eligible for maths biology")
    elif percentage>80 or  percentage>70 and marks['maths']>98 :
        print(f"\n{list['name']} is eligible for computer science")



