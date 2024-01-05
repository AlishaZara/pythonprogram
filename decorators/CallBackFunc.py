def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def cal(func,a,b):
    return func(a,b)

print(cal(mul,4,5))
print(cal(add,6,5))
print(cal(sub,10,5))
    