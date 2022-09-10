n = int(input())
l = [int(x) for x in input().split()]
max = max(l)
min = min(l)
max_i = l.index(max) +1
min_i = l.index(min) +1
print(min_i,max_i)
