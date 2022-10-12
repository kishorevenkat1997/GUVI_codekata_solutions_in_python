num = int(input())
arr1 = [int(x) for x in input().split()]
arr1.sort()
min_arr1 = arr1[0]
max_arr1 = arr1[-1]
print(max_arr1-min_arr1)