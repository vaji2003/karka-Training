players=[{'name':'Virat','no_centuries':10,'half_centuries':'88','wickets_taken':'21','hat_trick':6,'top_batting_score':[250,150,300,120]},
          {'name':'dhoni','no_centuries':20,'half_centuries':'150','wickets_taken':'22','hat_trick':5,'top_batting_score':[270,180,230,154]},
          {'name':'sachin','no_centuries':12,'half_centuries':'350','wickets_taken':'60','hat_trick':12,'top_batting_score':[140,178,200,128]},
          {'name':'raina','no_centuries':30,'half_centuries':'50','wickets_taken':'80','hat_trick':20,'top_batting_score':[180.156,212,222]},
          {'name':'malinga','no_centuries':9,'half_centuries':'70','wickets_taken':'20','hat_trick':4,'top_batting_score':[120,280,213,143]}]
def player(players):
    hatrrick=[]
    count=0 
    for values in players:
        if(values['no_centuries'])>10:
          count+=1
        if(values['hat_trick'])>5:
           hatrrick.append(values['name'])
           
            #   print(values['name'])
    print(f"No of players = {count}.")
    print(hatrrick
         
player(players)
# def value(players):
#    total=0
#    for value in players:
#     a=int(value['top_batting_score'])
#     if a>total:
#         total=a
#    print(f"\nTop batting score is {total}")
# value(players)