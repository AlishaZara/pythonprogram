import re
st='AP02AB7890 AP40YU5643 '

data=re.findall('[A-Z]{2}\d{2}[A-Z]{2}\d{4}',st)
print(data)

#['AP02AB7890', 'AP40YU5643']