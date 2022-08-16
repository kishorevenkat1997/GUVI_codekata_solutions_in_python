year = int(input())
if (year % 400 == 0) and (year % 100 == 0):
    print("leap year".format(year))
elif (year % 4 ==0) and (year % 100 != 0):
    print("leap year".format(year))
else:
    print("not a leap year".format(year))