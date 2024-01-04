import re
st='psalisha03@gmail.com'

data=re.findall('[a-zA-Z]+[a-zA-z0-9]*\@gmail*\.com',st)
print(data)