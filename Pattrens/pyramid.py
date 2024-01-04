rows=int(input('no of rows:- '))

out='''
'''
for i in range(0,rows+1):
    out=out+(' '*(rows-i)+'* '*i)
    out=out+'\n'

for i in range(0,rows):
    out=out+(' '*(rows-i)+'*'*(i*2+1))
    out=out+'\n'
with open('pat1.txt', 'w') as file:
    file.write(out)