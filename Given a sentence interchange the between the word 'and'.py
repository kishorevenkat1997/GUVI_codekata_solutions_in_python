l = input().split(" ")
m = []
for i in range(len(l)):
    if l[i] == "and":
        (l[i+1], l[i-1]) = (l[i-1], l[i+1])
for i in l:
    m.append(i)
print(*m)