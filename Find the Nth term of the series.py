a=[]
b=int(input())
for i in range(1,b+2):
  a.append(i**2)
if b<0:
  print("Error")
elif b==0:
  print(0)
else:
  c=a[b-1]
  print(c)