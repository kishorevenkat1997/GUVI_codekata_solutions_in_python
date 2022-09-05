num = int(input())
arr1 = input().split()
count = []
sum = 0
for k in range(num):
    for j in arr1:
       sum += int(j)
    count.append(sum)
    sum = 0
    arr1.pop(0)
print(*count)
