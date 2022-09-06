s1 = input()
vowels = ['a','e','i','o','u','A','E','I','O','U',' ']
for k in s1:
    if k in vowels:
        print(k,end='')
for j in s1:
    if j not in vowels:
        print(j,end='')