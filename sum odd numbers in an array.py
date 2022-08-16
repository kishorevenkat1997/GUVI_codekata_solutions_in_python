num = int(input())
arr = [int(x) for x in input().split()]
sum = 0
for k in arr:
    if num == len(arr):
      if k%2 != 0 :
          sum += k
      else:
          pass
print(sum)
