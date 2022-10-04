n = int(input())
l = input().split(" ")
l = [int(x) for x in l]
count = 0
for i in range(n):
    if (n*(i+1)) in l:
        count += 1
print(count)
