def add():
    a=int(input('enter a:-  '))
    b=int(input('enter b:-  '))
    print(a+b)

def cal(func):
    def inner():
        print('operation started')
        func()
        print('operation done')
    return inner
add=cal(add)
add()