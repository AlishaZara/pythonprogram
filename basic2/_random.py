import random
num=random.randint(1,10)
while True:
    a=int(input('enter a number:-'))
    if a==num:
        print('congrats you successfully guessed the number')
        break
    elif a<num:
        print('enter greater number')
    elif a>num:
        print('enter lesser number')