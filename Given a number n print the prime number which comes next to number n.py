num = int(input())
arr = [x for x in range(2,101)]
prime = []
for k in range(num,100):
    if k == 2 or k == 3 or k == 5 or k == 7:
        prime.append(k)
    elif k % 2 == 0 or k % 3 == 0 or k % 5 == 0 or k % 7 == 0:
        pass
    else:
        prime.append(k)
if num in prime:
    print(prime[1])
else:
    print(prime[0])