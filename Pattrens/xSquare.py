rows=int(input('no of rows:- '))
col=int(input('no of columns:- '))

for i in range(rows):
    for j in range(col):
        if i==0 or i==rows-1:
            print('+',end='')
        else:
            if j==0 or j==col-1:
                print('+',end='')
            else:
                print(' ' ,end='')
    print()
    
#no of rows:- 5
# no of columns:- 5
# +++++
# +   +
# +   +
# +   +
# +++++