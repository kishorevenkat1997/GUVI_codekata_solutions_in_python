l , r = map(int,input().split())
prime = []
count = 0
sum = 0
for k in range(l,r):
    for j in str(k):
        count += int(j)
    if count == 2 or count == 3 or count==5 or count==7:
        prime.append(k)
        sum +=1
        count = 0
    elif count == 1 or count % 2 == 0 or count % 3 == 0 or count % 5 == 0 or count % 7 == 0:
        count = 0
        pass
    else:
        prime.append(k)
        sum += 1
        count = 0
print(sum)