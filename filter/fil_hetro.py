def fname(a):
    if type(a) in [int,float,complex,bool]:
        return True
    else:
        return False
out=filter(fname,[2,(1,2,3),'abc',{'c':4},5,7])
print(list(out))