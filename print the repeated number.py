num = int(input())
arr1 = [int(x) for x in input().split()]
arr2 = []
rep = []
ans = set()
for k in arr1:
    if k not in arr2:
        arr2.append(k)
    elif k in arr2:
        rep.append(k)
if len(rep) == 0:
    print('unique')
else:
     for j in rep:
         ans.add(j)
     print(*ans)