num = int(input())
arr1 = [int(x) for x in input().split()]
for k in arr1:
    a=arr1.count(k)
    if a == 1:
        print(k)