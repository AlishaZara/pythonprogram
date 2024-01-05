def  cal(func):
    def inner():
        print('opertation started')
        func()
        print('opertion done')
    return inner

@cal #add=cal(add)
def add():
    a=int(input('enter a:- '))
    b=int(input('enter b:- '))
    print(a+b)
add()
