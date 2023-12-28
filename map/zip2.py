a=[1,2,3]
b=[2,3,4]
c=[3,4,5]
out=[]
for i,j,k in zip(a,b,c):
    out=out+[i]+[j]+[k]
print(out)