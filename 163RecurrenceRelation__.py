'''
หาจำนวนเวียนเกิดที่ n จากสูตร
An = Sqrt(1+ (An + 1)**2)
'''
import math
'''
member_input = int(input())
n_lib = []
for i in range(0,member_input):
    n = int(input())
    n_lib.append(n)

print(n_lib)
'''
#find an
a_val = []

a0 = 0
a_val.append(a0)

a1 = math.sqrt(1+ (a0**2))
a_val.append(a1)

a2 = math.sqrt(1+ (a1**2))
a_val.append(a2)

a3 = math.sqrt(1+ (a2**2))
a_val.append(a3)

a4 = math.sqrt(1+ (a3**2))
a_val.append(a4)

a5 = math.sqrt(1+ (a4**2))
a_val.append(a5)

a6 = math.sqrt(1+ (a5**2))
a_val.append(a6)

print(a_val)

sum6 = (1 / (a1+a2)) + (1 / (a2+a3)) + (1 / (a3+a4)) + (1 / (a4+a5)) + (1/(a5+a6))
print(round(sum6,2))



# Sn = (n/2) * (a1 + an)
div_a1 = 1 / (a1+a2)
div_a6 = 1/(a5+a6)

s5 = (5/2) * (div_a1+div_a6)
print(s5)

