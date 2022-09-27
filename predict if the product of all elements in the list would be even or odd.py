num = int(input())
arr1 = [int(x) for x in input().split()]
sum = 1
for k in arr1:
    sum *= k
if sum % 2 == 0:
    print('even')
else:
    print('odd')