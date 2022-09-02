num = int(input())
arr1 = [int(x) for x in input().split()]
arr2 = []
rep = []
for k in arr1:
    if k not in arr2:
        arr2.append(k)
    else:
        rep.append(k)
if len(arr2) < 2:
    print('-1')
else:
    if len(arr1) == num:
        arr2.sort()
        print(arr2[1])
