num = int(input())
arr = input().split()
arr1 = []
repeated = set()
for k in arr:
    if k not in arr1:
        arr1.append(k)
    elif k in arr1:
        repeated.add(k)
if num == len(arr):
    print(*repeated)
