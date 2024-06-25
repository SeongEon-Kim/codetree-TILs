a, b =list(map(int, input().split()))

def special_num(n):
    if n %2!=0:
        list_n = list(n)
        if int(list_n[-1]) != 5:
            if n % 3 ==0 and n% 9 !=0:
                return 1
            
    return 0

sum = 0
for i in range(a, b +1):
    #sum += special_num(i)
    print(special_num(i))