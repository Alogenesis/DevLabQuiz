inp = 10
mul = 1

for i in range(0,inp):
    print('*'*mul)
    mul += 1
mul -= 2
inp -= 1
for i in range(0,inp):
    print('/'*mul)
    mul -= 1
