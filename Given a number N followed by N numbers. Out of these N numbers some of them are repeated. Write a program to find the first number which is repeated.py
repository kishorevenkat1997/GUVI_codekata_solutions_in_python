num = int(input())
arr1 = [int(x) for x in input().split()]
arr2 = []
rep = []
for k in arr1:
    if k not in arr2:
        arr2.append(k)
    else:
        rep.append(k)
        break
if len(rep) == 0:
    print('unique')
else:
    print(*rep)