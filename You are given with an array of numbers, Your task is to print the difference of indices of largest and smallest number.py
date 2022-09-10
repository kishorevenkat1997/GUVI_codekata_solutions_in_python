num = int(input())
arr1 = [int(x) for x in input().split()]
min = arr1.index(min(arr1))
max = arr1.index(max(arr1))
sum = max - min
print(sum)