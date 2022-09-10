len_of_arr1 = int(input())
arr1 = [int(x) for x in input().split()]
mul = 1
for k in arr1:
    mul *= k
ans = []
for j in range(1,mul+1):
    if len(ans) == 0:
        for i in arr1:
            if j % i != 0:
                ans.clear()
                break
            else:
                ans.append(j)
print(ans[0])
