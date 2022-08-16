import string as s
letter = [str(c) for c in s.ascii_letters]
s1 = input()
sum = 0
for f in s1:
    if f == " ":
        continue
    elif f not in letter:
        sum += 1
    else:
        pass
if sum == 0:
    print("-1")
else:
    print(sum)
