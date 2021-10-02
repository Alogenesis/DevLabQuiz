'''
แปลง Yuan > Baht
1 Y > 4 B
'''

import re
x = input()
x_int = int(re.search(r'\d+', x).group())
print(x_int*4,'Baht')