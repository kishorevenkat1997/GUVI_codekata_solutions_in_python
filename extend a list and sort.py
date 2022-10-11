num = int(input())
arr1 = [int(x) for x in input().split()]
num = int(input())
arr2 = [int(y) for y in input().split()]
arr1.extend(arr2)
uniq = set(arr1)
ans = list(uniq)
ans.sort()
print(*ans)