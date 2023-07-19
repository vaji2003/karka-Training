my_resume={
    'name':'Vajeeha',
    'E-mail':'vajeeha@gmail.com',
    'mobile_no':'95370326',
    'soft_skills':['communication','decision making'],
    'hard_skills':['coding','chess'],

 'Education_qualification':[
           {   'course':'sslc',
               'percentage':"80",
               'Institute_name':'G-H-S school'   },

           {   'course':'hsc',
               'percentage':"85",
               'Institute_name':'G-H-S school'   },

           {   'course':'Degree',
               'percentage':"80",
                'Institute_name':'Womens-christian-college'   }     ],

'project': [ {'Title':'Text input and validation',
           'about':'survey app',
           'language':'kotlin'   }],

'Experiance':[
            {   'company_name':'wibro',
                'duration':"1.4",
                'role':'HR',
                'place':'kerala'},

             {  'company_name':'google',
                'duration':"2.4",
                'role':'developer',
                'place':'chennai'     },

             {  'company_name':'flow',
                'duration':1.2,
                'role':'python_developer',
                'place':'nagercoil'   }   ],

'hobbies':['watch_movies','listening_song','sharing-reels'],

'personal_details':
                {'father_name':'Basheer',
                 'father_occupation':'shop',
                'languages_known':['Tamil','English'],
                'D-O-B':"25-2-2003",
                'Gender':'Female',
                'married_status':'unmarried','address':
              {'door_number':"6/46",
                 'street_name':'Bigstreet',
                 'place':'Thittuvilai',
                 'pincode':"629852",
                 'District':'TamilNadu',
                 'country':'India'}}} 


# # for key,values in my_resume.items():
# #    print(my_resume['Education_qualification'])

for i in my_resume['personal_details']:
    if i=='address':
        for j in my_resume['personal_details'][i]:
           print(f"{j}:{my_resume['personal_details']['address'][j]}")
# for j in my_resume['personal_details']:


# # for i in my_resume['personal_details']:
# #     print(f"{my_resume['personal_details'][i]}")

# # for i in my_resume['Experiance']:
# #     print([i]['role'])




# # print(my_resume['personal_details']['address'])
# # print(my_resume['personal_details']['address']['street_name'])



# name='vajeeha'
# dic_name={'name':name}
# print(dic_name)