def fib(n):
    a,b,count = 0,1,0
    list = []
    while count < n:
        list.append(a)
        a, b = b, a+b
        count += 1
    return list

print(fib(10))
        