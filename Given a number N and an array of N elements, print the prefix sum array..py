num = int(input())
arr1 = [int(x) for x in input().split()]
count = 0
sum = 0
ans = []
for k in arr1:
    if arr1[count]:
        sum += k
        ans.append(sum)
        count += 1
print(*ans)
