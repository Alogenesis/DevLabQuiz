'''
รับตัวเลขจำนวนเต็มจนกว่าจะเจอเลข 0 จากนั้นหาว่ามีกี่จำนวณ และค่ามากที่สุดและน้อยที่สุดคืออะไร
In :
34
56
-23
34
567
12
98
3
0

Out :
Total : 8
Maximum : 567
Minimum : -23
'''

x = int(input())
numlib = []
while x != 0:
    numlib.append(x)
    x = int(input())

numlib.sort()
#print(numlib[0]) #น้อยสุด
#print(numlib[-1])  #มากสุด
if len(numlib) != 0:
    print('Total :', len(numlib))
    print('Maximum :', numlib[-1])
    print('Minimum :', numlib[0])
else:
    print('Total : 0')
    print('Maximum : 0')
    print('Minimum : 0')