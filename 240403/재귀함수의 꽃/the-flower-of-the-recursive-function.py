def recurison_flower(n):
    if n == -1:
        return
    print(_list[n], end=" ")
    recurison_flower(n-1)
    print(_list[n], end=" ")
    
a = int(input())
_list = [i+1 for i in range(a)]
recurison_flower(a-1)