num , a = map(int,input().split())
arr1 = [int(x) for x in input().split()]
if a in arr1:
    count = arr1.count(a)
    print('yes',count)
else:
    print('no')
