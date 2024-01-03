try:
    a=2+'2'
    print(a)
except TypeError:
    print('error handled')
finally:
    print('finally handled')

def sum(a,b):
    return a+b
print(sum(2,3))