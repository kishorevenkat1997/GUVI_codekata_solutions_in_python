num = int(input())
arr1 = [int(x) for x in input().split()]
arr2 = [int(y) for y in arr1]
arr1.sort()
indx =[]
for k in arr2:
    indx.append(arr1.index(k)+1)
print(*indx)