'''
หาจำนวนเวียนเกิดที่ n จากสูตร
An = Sqrt(1+ (An + 1)**2)
'''
import math

member_input = int(input())
n_lib = []
for i in range(0,member_input):
    n = int(input())
    n_lib.append(n)

#print(n_lib)

# Algorhytm
sqrt_lib = [1]

def find_an(n):
    An = math.sqrt(1 + (sqrt_lib[-1])**2)
    sqrt_lib.append(An)

# Loop for root n value
for i in n_lib:
    nloop = i
    # Algorhytm
    for i in range(1,nloop):
        find_an(i)
    #print(sqrt_lib)

    sum = 0
    for i in range(0,nloop-1):
        sum += (1 / (sqrt_lib[i] + sqrt_lib[i+1]))

    #print(sum)
    print('{:.2f}'.format(sum))