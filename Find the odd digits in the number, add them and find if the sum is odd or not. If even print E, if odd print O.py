#Find the odd digits in the number, add them and find if the sum is odd or not. If even print E, if odd print O
num = input()
sum = 0
for k in num:
    if int(k) == 1 or int(k) % 2 != 0:
        sum += int(k)
    else:
        pass
if sum % 2 == 0:
    print('E')
else:
    print('O')