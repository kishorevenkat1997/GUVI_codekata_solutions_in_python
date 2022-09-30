num = int(input())
arr = [int(x) for x in input().split()]
arr.sort(reverse=True)
for k in arr:
    print(k,end='')