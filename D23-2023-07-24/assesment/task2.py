months=[{'month_name':'January',
        'gold_rate':1200},
       {'month_name':'Feb',
        'gold_rate':1300},
        {'month_name':'March',
        "gold_rate":1500},
        {'month_name':'April',
        'gold_rate':1400}
       ]
top=0
small=months[0]['gold_rate']
name=None
names=months[2]['month_name']
for values in months:
    top_values=values['gold_rate']
    month=values['month_name']
    if top_values>=top:
         top=top_values
         name=month
    if small>=top_values:
         small=top_values
print(f"In {name} golden rate is {small}")
print(f"In {name} golden rate is {top}")
print(name)


    