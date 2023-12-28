num1=int(input('enter the first number:-'))
num2=int(input('enter the second number:-'))
num3=int(input('enter the third number:-'))
if num1>num2 and num1>num3:
    if num2>num3:
        print(num2,':is second greater')
    else:
        print(num3,':is second greater')
elif num2>num3:
    if num1>num3:
        print(num1,':is second greater')
    else:
        print(num3,':is second greater')
else:
    if num1>num2:
        print(num1,':is second greater')
    else:
        print(num2,':is second greater')