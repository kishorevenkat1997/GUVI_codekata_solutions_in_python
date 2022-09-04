n , k = map(str,input().split())
count = 0
for j in n:
    if j == k:
        count +=1
    else:
        pass
if count == 0:
    print('-1')
else:
    print(count)