num = int(input())
arr1 = [int(x) for x in input().split()]
arr2 = []
rep = []
ans = []
for k in arr1:
    if k not in arr2:
        arr2.append(k)
    else:
        rep.append(k)
for j in arr1:
    if j in rep:
        pass
    else:
        ans.append(j)
if len(arr1) == num:
    ans.sort(reverse=True)
    print(*ans)
