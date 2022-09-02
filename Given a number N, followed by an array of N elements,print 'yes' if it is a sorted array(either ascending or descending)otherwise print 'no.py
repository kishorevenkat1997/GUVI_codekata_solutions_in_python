num = int(input())
arr1 = [int(x) for x in input().split()]
ascending = []
decending = []
for k in range(len(arr1)):
    if arr1[k] == arr1[-1]:
        ascending.append(arr1[k])
        decending.append(arr1[k])
    elif arr1[k] <= arr1[k+1]:
        ascending.append(arr1[k])
    elif arr1[k] >= arr1[k+1]:
        decending.append(arr1[k])
    else:
        pass
if len(ascending) == num or len(decending) == num:
    print('yes')
else:
    print('no')