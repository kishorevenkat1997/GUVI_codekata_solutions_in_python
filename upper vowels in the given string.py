s1 = input()
vowels = "aeiouAEIOU"
for k in s1:
    if k in vowels:
        print(k.upper(),end="")
    else:
        print(k,end="")