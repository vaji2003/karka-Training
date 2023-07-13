print("Two questions! \nThink of a object I will try to guess it")
print('\t')
q1=input(" Question 1) It is animal , vegetable , or mineral? \n")

a="squirrel"
b="mouse"
c="carrot"
d="watermelon"
e="paperclip"
f="camero"

q2=input(" Question 2) It is bigger than the breadbox \n")

if q1=="animal":
 if q2=="yes":
  print(f"""My guess is that you are thinking of a {b}.
           \nI would ask you if I'am right, but I don't actually care """)
if q1=="vegetable":
  if q2=="yes":
     print(f"""My guess is that you are thinking of a {d}.\nI would ask you if I'am right, but I don't actually care """)
if q1=="mineral":
      if q2=="yes":
       print(f"""My guess is that you are thinking of a {f}.\nI would ask you if I'am right, but I don't actually care """)
if q1=="animal":
        if q2=="no":
         print(f"""My guess is that you are thinking of a {a}.\nI would ask you if I'am right, but I don't actually care """)
if q1=="vegetable":
          if q2=="no":
           print(f"""My guess is that you are thinking of a {c}.\nI would ask you if I'am right, but I don't actually care """)
if q1=="mineral":
            if q2=="no": 
             print(f"""My guess is that you are thinking of a {e}.\nI would ask you if I'am right, but I don't actually care """)