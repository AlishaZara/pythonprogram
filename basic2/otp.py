import random
otp=''
while (True):
    otp=otp+str(random.randint(0,9))
    if len(otp)==4:
        break
print('your otp is:-',otp)
    