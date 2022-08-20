def getHCF(x, y):
    minimum = min(x, y)
    if (x % minimum == 0 and y % minimum == 0):
        return minimum
    for i in range(minimum // 2, 1, -1):
        if (x % i == 0 and y % i == 0):
            return i
    return 1
x, y = map(int,input().split())
print(getHCF(x, y))