import re
st='ABCDE2345F ERTYU5790U'

data=re.findall('[A-Z]{5}\d{4}[A-Z]',st)
print(data)

#['ABCDE2345F', 'ERTYU5790U']