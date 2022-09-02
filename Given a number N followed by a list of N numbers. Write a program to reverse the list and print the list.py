num = int(input())
arr1 = input()
for k in (arr1[::-1]):
    if k == ' ':
        print('->',end='')
    else:
        print(k,end='')