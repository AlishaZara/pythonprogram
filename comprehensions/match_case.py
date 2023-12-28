seats=int(input('enter the seats...'))
option=int(input('enter option here...'))
match option:
    case 1:
        print("diamond class")
        amount=seats*200
    case 2:
        print("golden class")
        amount=seats*150
    case 3:
        print("silver class")
        amount=seats*100
    case _:
        print('invalid option')
        amount=None
print(amount)
    