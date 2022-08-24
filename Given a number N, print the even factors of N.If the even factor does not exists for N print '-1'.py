#Given a number N, print the even factors of N.If the even factor does not exists for N print '-1'.
factor = int(input())
even_factors = []
for k in range(1 , factor + 1):
    if factor % k == 0 and k % 2 == 0:
        even_factors.append(k)
if len(even_factors) == 0:
    print('-1')
else:
    print(*even_factors)
