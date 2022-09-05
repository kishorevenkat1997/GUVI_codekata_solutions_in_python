s1 = input().split()
len = len(s1) +1
x = input()
count = 1
for k in s1:
    if k not in x:
        count += 1
    else:
         break
if count == len:
    print('-1')
else:
    print(count)