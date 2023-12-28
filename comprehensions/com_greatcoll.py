b=([1,2,3,4],(1,2),{4,6,7},{2:1,4:2,1:3},'efgh')
out=[i for i in b if len(i)>2]
print(out)