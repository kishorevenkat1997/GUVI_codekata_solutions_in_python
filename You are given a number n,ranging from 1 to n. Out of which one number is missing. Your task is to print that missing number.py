num = int(input())
arr = [int(x) for x in input().split()]
n = [int(y) for y in range(1,num+1)]
ans = []
for k in n:
    if k in arr:
        pass
    else:
        ans.append(k)
print(*ans)