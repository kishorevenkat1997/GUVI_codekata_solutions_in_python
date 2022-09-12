s1 = ['GUVI','GEEK']
s2 = input()
count = 0
for k in s1:
    if k in s2:
        count += 1
    else:
        pass
if count == 2:
    print('yes')
else:
    print('no')