a, key, b = list(map(str, input().split()))

if key == '+':
    print(a, key, b, "=",int(a)+int(b), end=' ')
elif key == '-':
    print(a, key, b, "=",int(a)-int(b), end=' ')
elif key == '/':
    print(a, key, b, "=",int(int(a)/int(b)),  end=' ')
elif key == '*':
    print(a, key, b, "=",int(a)*int(b), end=' ')
else:
    print("False")