n , k = map(int,input().split())
arr1 = [int(x) for x in input().split()]
arr1.sort(reverse=True)
print(arr1[k-1])