num = int(input())
arr1 = [int(x) for x in input().split()]
ans = []
for k in arr1:
    if k < num:
        ans.append(k)
    else:
        pass
ans.sort(reverse=True)
if len(ans) == 0:
    print('-1')
else:
    print(*ans)