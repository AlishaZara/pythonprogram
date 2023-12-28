num=input('enter a binary number')
out=''
i=0
while i<len(num):
    if num[i]=='0':
        out=out+'1'
    else:
        out=out+'0'
    i+=1
print(out)