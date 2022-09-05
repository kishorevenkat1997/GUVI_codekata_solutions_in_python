s1 = input()
arr1 = []
rep = []
for k in s1:
    if k not in arr1:
        arr1.append(k)
    elif k in arr1:
        rep.append(k)
for j in s1:
    if j in rep:
        print(j.upper(),end='')
    else:
        print(j,end='')