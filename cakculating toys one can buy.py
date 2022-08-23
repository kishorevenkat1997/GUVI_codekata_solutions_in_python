toys , money= map(int,input().split())
arr = [int(x) for x in input().split()]
sum = 0
count = 0
if toys == len(arr):
    for k in arr:
        if k < money and sum <= money:
            sum += k
            if sum >= money:
               count += 1
        else:
            pass
print(count)
