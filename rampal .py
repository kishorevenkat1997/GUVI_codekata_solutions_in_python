n = str(input())
if int(n) > 0:
    if (int(n[-1]) + int(n[-2])) % 4 == 0:
        print("yes")
    else:
        print("no")
else:
    if (int(n[-1]) + int(n[1])) % 4 == 0:
        print("yes")
    else:
        print("no")
