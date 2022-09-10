n , m = map(int,input().split())
a = [int(x) for x in input().split()]
b = [int(y) for y in input().split()]
count = 0
for k in b:
    if k in a:
        pass
    else:
        count += 1
if count == 0:
    print('yes')
else:
    print('no')