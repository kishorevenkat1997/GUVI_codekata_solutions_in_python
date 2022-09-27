n,k = map(str,input().split())
arr1 = [str(x) for x in range(0,int(k)+1)]
arr2 = [y for y in n]
count = 0
for k in arr1:
    if k in arr2:
        pass
    else:
        count += 1
if count == 0:
    print('yes')
else:
    print('no')
