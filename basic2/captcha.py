import random
cap=''
while len(cap)<6:
    cap=cap+chr(random.randint(65,90))
    cap=cap+chr(random.randint(97,122))
    cap=cap+str(random.randint(0,9))
print(cap)