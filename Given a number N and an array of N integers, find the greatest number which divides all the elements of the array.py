num = int(input())
arr1 = [int(x) for x in input().split()]
arr1.sort()
count = 0
for k in arr1:
    for j in arr1:
        if j % k == 0:
            pass
        else:
            count += 1
            break
    if count == 0:
        print(k)
        break
    else:
        pass