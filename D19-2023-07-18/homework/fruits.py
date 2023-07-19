items_list=[     {'name': 'Apple', 'category': 'Fruits'},
                 {'name': 'Carrot', 'category': 'vegetables'},
                 {'name': 'Banana', 'category': 'Fruits'},
                 {'name': 'Broccoli', 'category': 'vegetables'}  ]
category={
          "fruits":[],
          "vegetable":[]
          }
for items in items_list:
    if items['category']=='Fruits':
     category['fruits'].append(items['name'])
    if items['category']=='vegetables':
       category['vegetable'].append(items['name'])
print(category)
   
