password=input('enter a password:- ')
validate={'upper':False,'lower':False,'number':False,'number':False,'char':False,'space':'True'}
if len(password)>=8:
    for char in password:
        if 'A'<=char <='Z':
            validate['upper']=True
        elif 'a'<=char <='z':
            validate['lower']=True
        elif '0'<=char <='9':
            validate['number']=True
    if validate['upper'] and validate['lower'] and validate['number'] and validate['char'] and validate['space']:
        print('password is valid')
    else:
        print('password invalid')
else:
    print('password is valid')