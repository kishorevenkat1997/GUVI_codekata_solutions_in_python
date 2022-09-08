import string
upper = [x for x in string.ascii_uppercase]
sum = 0
s1 = input()
for k in s1:
    if k in upper:
        sum += 1
if sum > 1 :
    print('yes')
else:
    print('no')