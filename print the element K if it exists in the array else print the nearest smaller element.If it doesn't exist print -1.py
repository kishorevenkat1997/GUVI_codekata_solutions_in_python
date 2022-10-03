n , k = map(int,input().split())
arr = [int(x) for x in input().split()]
count = 0
if k in arr:
    print(k)
else:
    arr.sort(reverse=True)
    for j in arr:
        if j < k:
            print(j)
            break
        else:
            count += 1
if count == len(arr):
    print('-1')
