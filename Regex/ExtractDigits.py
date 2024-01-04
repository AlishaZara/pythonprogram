import re
st='The data is 04/01/2024'

data=re.findall('\d',st)
print(data)

#['0', '4', '0', '1', '2', '0', '2', '4']