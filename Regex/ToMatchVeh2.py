# import re
# st='AP02AB7890 AP40YU5643 '

# data=re.findall('AP[0-3]\d[A-Z]{2}\d{4}',st)
# print(data)

#['AP02AB7890']


import re
st='AP42AB7890 AP40YU5643 '

data=re.findall('AP[0-3][0-9][A-Z]{2}[0-9]{4}|AP40[A-Z]{2}[0-9]{4}',st)
print(data)
#['AP40YU5643']