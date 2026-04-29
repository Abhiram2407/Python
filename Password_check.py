a=input("Enter the password")
up=0
low=0
dig=0
spl=0
if len(a)>7:
  for i in a:
    if i.isupper():
      up+=1
    elif i.islower():
      low+=1
    elif i.isdigit():
      dig+=1
    else:
      spl+=1
  if up>0 and low>0 and dig>0 and spl>0:
    print("Password is Strong")
  else : 
    print("Password is Weak")
else : 
  print("Password is weak due to less characters")
