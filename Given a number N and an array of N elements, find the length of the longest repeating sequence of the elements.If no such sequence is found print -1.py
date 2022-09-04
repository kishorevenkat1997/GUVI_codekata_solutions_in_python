num = int(input())
arr1 = [int(x) for x in input().split()]
ans = []
for k in arr1:
    count = arr1.count(k)
    ans.append(count)
rep = []
for j in arr1:
    if j not in rep:
        rep.append(j)
if num == len(arr1):
    ans.sort()
    if len(arr1) == len(rep):
        print('-1')
    else:
        print(ans[-1])


