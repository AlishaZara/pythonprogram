import re
with open(r"C:\Users\administrator.MCA\Desktop\Python\hello python.txt",'r') as file:
    data=file.read()
    out=re.split(' ',data)
    data1=re.split(' ',data)
    count=0
    words=[]
    for i in data1:
        out=re.match('^a',i)

        if out:
            words+=[i]
            count+=1
    print(count)
    print(words)