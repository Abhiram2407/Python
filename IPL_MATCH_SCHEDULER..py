import random
a= int(input("Enter the number of Teams:"))
teams=[]
print("Enter the team names:")
for i in range(a):
  t=input("Enter the team name:")
  teams.append(t)
m=int(input("Enter the number of times team meet"))
matches=[]
for i in range(0,a-1):
  for j in range(i+1,a):
    for k in range(m):
      matches.append([teams[i],teams[j]])
pos=1
random.shuffle(matches)
for i in  matches:
  print("MAtch {}:  {} v/s {}".format(pos,i[0],i[1]))
  pos+=1
