#First line contains two integer ‘n’ and ‘k’ ,n denotes the number of toys and k denotes total money he has.Next line contains n space separated integers denoting price of each toy
toys , money= map(int,input().split())
arr = [int(x) for x in input().split()]
arr.sort()
sum = 0
count = 0
if toys == len(arr):
    for k in arr:
        if k < money and sum <= money:
            sum += k
            if sum <= money:
               count += 1
        else:
            pass
print(count)
