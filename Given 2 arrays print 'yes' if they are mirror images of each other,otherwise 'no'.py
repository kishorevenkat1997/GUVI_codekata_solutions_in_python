num = int(input())
arr1 = [int(x) for x in input().split()]
arr1_r = [int(z) for z in arr1[::-1] ]
arr2 = [int(y) for y in input().split()]
count = 0
for a,b in zip(arr1_r,arr2):
    if a == b:
        count += 1
if num == count:
    print('yes')
else:
    print('no')
