def fname(a):
    if a%2==0:
        return True
    else:
        return False
out=filter(fname,[2,3,4,5,6,7,])
print(list(out))