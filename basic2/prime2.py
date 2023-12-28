num=int(input('enter a number:-'))
i=2
temp=False
while i<num:
    if num%i==0:
       temp=True
    i=i+1
if not temp:
    print(num,'is prime')
else:
    print(num,'is not prime')