s1 = input().split()
rev = []
for k in s1:
    rev.append(k[::-1])
print(*rev)