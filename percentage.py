m=eval(input('enter your marks:-'))
if m>=90 and m<=100:
    print('A+')
elif m>=80 and m<90:
    print('A')
elif m>=70 and m<80:
    print('B')
elif m>=60 and m<70:
    print('C')
elif m>=35 and m<60:
    print('pass')
elif m>=0 and m<=35:
    print('fail')
else:
    print('invalid marks')