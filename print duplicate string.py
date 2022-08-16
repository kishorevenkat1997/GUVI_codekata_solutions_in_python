s1 = input()
s2=[]
for k in s1:
    if k not in s2:
        s2.append(k)
    elif k in s2:
        print(k , end="")