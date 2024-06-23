y = int(input())

def is_specialyear(n):
    if n % 4 == 0 :
        if n % 100 == 0 and n % 400 != 0:
            return False
        return True
    return False

if is_specialyear(y):
    print('true')
else:
    print('false')