import re
st='1 6 567 The data 54 is 04/01/2024'

data=re.findall('\d+',st)
print(data)

#['1', '6', '567', '54', '04', '01', '2024']