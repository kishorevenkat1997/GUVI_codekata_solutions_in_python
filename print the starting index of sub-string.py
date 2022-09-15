s1 , s2 = map(str,input().split())
count = 0
for k,j in zip(s1,s2):
    if k in s2 and j in s1:
        pass
    else:
        count += 1
if count == 0:
    print('true')
else:
    print('false')