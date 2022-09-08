num = int(input())
arr1 = []
ans = []
for k in range(2,num+100):
    if k == 2 or k == 3 or k == 5 or k==7 or k == 11:
        arr1.append(k)
    elif k % 2 == 0 or k%3 == 0 or k%5 == 0 or k%7==0 or k%11==0:
        pass
    else:
        arr1.append(k)
for j in arr1:
    if j > num:
        if len(ans) < 3:
            ans.append(j)
print(*ans)
