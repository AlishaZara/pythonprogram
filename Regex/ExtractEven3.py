#\d represent first digit of a number
#[24680]represent second digit of a number

import re
st='The 92 data 54 is 04/01/2024'

data=re.findall('\d[24680]',st)
print(data)

#['92', '54', '04', '20', '24']