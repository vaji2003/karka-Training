# detail='Education_details':{'study':'BSC',
#                        'Institute':'cape',
#                        'sem_marks':{
#                                     "sem_name":1,
#                                      'subject':['computer','maths','datascience'],
#                                      'sem_grade':'A'
#                                      },

#                                      {
#                                          "sem_name":2,
#                                          'subject':['cphysics','chemistry','science'],
#                                          'sem_grade':'B'
#                                      }}
# set={"vajeeha",20,"25-02-2003","supriya"}
# print(set)c
# print(set)
# # print(set)

# file=open("/home/vagiha/vaji/karka.txt","r")
# for line in file:
#  print(line)
# data=file.read()
# print(data)


file=open("/home/vagiha/vaji/karka.txt","a")
file.write("I am vajeeha\n")
file.write("Hello this is vajeeha")
file.close()

file=open("/home/vagiha/vaji/karka.txt","r")

# data=file.read()
# print(data)
for line in file:
 print(line.split())