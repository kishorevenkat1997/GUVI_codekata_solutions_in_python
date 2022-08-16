s1 = input()
upper = 0
lower = 0
for k in s1:
    if k.isupper():
        upper += 1
    elif k.islower():
        lower += 1
    else:
        pass
print(upper,lower)