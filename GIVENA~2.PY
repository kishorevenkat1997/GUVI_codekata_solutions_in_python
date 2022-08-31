n = int(input())
arr1 = [int(x) for x in input().split()]
odd = []
even = []
if len(arr1) == n:
    for k in arr1:
        if k%2 == 0:
            even.append(k)
        else:
            odd.append(k)
    if len(even) == 0 or len(odd) == 0:
        print('-1')
    elif len(odd) < len(even):
        print(*odd)
    else:
        print(*even)
