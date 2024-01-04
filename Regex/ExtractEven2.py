import re
st='The 9 data 5 is 04/01/2024'

data=re.findall('[24680]{2}',st)
print(data)

#['04', '20', '24']