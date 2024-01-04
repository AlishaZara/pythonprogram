# to extract only even numbers..... 

import re
st='The 9 data 5 is 04/01/2024'

data=re.findall('[24680]',st)
print(data)

#['0', '4', '0', '2', '0', '2', '4']