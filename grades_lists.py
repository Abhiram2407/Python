names=["Abhi","Ram","Varma","Raha","Chaitu"]
marks=[[30,20,50],[66,77,55],[63,78,90],[87,97,77],[47,30,47]]
for i in range(5):
  p=sum(marks[i])//3
  if p>80:
    g="S"
  elif p>=60:
    g="A"
  elif p>=40:
    g='B'
  else:
    g='F'
  print("{}. {} has scored {}% - {} Grade".format(i+1,names[i],p,g))
