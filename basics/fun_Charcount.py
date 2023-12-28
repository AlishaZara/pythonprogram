def countchar(a,char):
    count=0
    for i in a:
        if char==i:
            count+=1
    return count
c=countchar('aaaabdef','a')
print(c)