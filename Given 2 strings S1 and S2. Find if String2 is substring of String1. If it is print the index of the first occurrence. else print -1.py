s1 = input()
s2 = input()
ans = []
for k in s1:
    if k == s2[0]:
        ans.append(s1.index(k))
        break
    else:
        pass
for j in s2:
    if j not in s1:
        ans.clear()
    else:
        pass
if len(ans) == 0:
    print('-1')
else:
    print(*ans)

