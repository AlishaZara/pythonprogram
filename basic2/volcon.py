a='hello'
vow_count=0
con_count=0
for var in a:
    if 'A'<= var<='Z' or 'a'<=var <='z':
        if var in'aeiouAEIOU':
            vow_count+=1
        else:
            con_count+=1
print(vow_count,con_count)