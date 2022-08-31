n , m = map(int,input().split())
arr1 = [int(x) for x in input().split()]
count = 0
index = []
for k in arr1:
    if k == m:
        print(arr1.index(k) + 1)
    else:
        count += 1
if count == n:
    print('-1')

