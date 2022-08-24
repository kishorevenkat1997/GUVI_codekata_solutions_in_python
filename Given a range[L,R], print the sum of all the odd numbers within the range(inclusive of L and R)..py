#Given a range[L,R], print the sum of all the odd numbers within the range(inclusive of L and R).
l , r = map(int,input().split())
sum = 0
for k in range(l,r+1):
    if k % 2 != 0:
        sum += k
    else:
        pass
print(sum)