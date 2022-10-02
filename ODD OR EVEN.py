numbers=list(map(int,input()))
even=[]
odd=[]
for k in numbers:
  if k%2==0:
    even.append(k)
  else:
    odd.append(k)
print(*even)
print(*odd)