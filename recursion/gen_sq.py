def fun(a,b):
    for i in range(a,b+1):
        yield i**2
        yield i*2
out=fun(5,15)
print(list(out))