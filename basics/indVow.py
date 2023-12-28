def index_vowel(a):
    out=[]
    for i in range(0,len(a)):
        if a[i] in 'aeiouAeiou':
            out=out+[i]
        i=i+1
    return out
b=index_vowel('aassddee')
print(b)