def getSum(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum


n = int(input())
d = getSum(n)
print(d)
if d % 3 == 0:
    print("yes")
else:
    print("no") 