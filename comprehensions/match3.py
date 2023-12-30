a=input('enter the color:  ')
match a:
    case 'red':
        print('stop')
    case 'yellow':
        print('ready to go')
    case 'green':
        print('Go')
    case _:
        print('Invalid')