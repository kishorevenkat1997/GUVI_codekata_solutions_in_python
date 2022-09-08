import string
letters = [x for x in string.ascii_letters]
s1 = input()
sum = 0
for k in s1:
    if k == ' ':
        pass
    elif k not in letters:
        sum += 1
if sum == 0:
    print('-1')
else:
    for j in s1:
        if j in letters:
            print(j,end='')