num = int(input())
arr = [int(x) for x in input().split()]
duplicate = []
rem = []
ans = []
for k in arr:
    if k not in duplicate:
        duplicate.append(k)
    elif k in duplicate:
        rem.append(k)
for j in arr:
    if j in rem:
        pass
    if j not in rem:
        ans.append(j)
print(*ans)
