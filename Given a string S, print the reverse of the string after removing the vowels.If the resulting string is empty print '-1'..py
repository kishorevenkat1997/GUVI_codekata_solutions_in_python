# space elama reverse la print pandrathu so have a look at it
vowels = ['a','e','i','o','u','A','E','I','O','U']
s = str(input())[::-1]
b = 0
for k in s:
  if k not in vowels:
    b += b + 1
for i in range(len(s)):
  if b == 0:
      print(-1)
      break
  elif s[i] not in vowels:
        print(s[i], end = "")

