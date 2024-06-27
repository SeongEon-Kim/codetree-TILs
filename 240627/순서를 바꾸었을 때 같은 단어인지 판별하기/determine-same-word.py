str1 = list(str(input()))
str2 = list(str(input()))

str1.sort()
str2.sort()

if str1 == str2:
    print('Yes')
else:
    print('No')