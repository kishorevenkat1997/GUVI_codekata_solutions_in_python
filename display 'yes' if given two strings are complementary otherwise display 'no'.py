import string
alpha = [x for x in string.ascii_uppercase]
s1 = list(input())
s2 = list(input())
s1.extend(s2)
sum = 0
for k in alpha:
    if k in s1:
        pass
    else:
        sum += 1
if sum > 0 or len(alpha) != len(s1):
    print('no')
else:
    print('yes')