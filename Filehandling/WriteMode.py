file=open('mca.txt','w')
data='welcome to the mca department'
file.write(data)
file.close()

file=open('mca.txt','r')
date=file.read()
print(date)
file.close()