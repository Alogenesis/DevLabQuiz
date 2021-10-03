'''
มีชายคนหนึ่งเขาไม่เคยเห็นเลนส์มาก่อน แต่เขาจำวิชาฟิสิกส์ตอน ม.2 ได้ว่า ถ้าหากนำวัตถุห่างจากเลนส์และวางวัตถุไว้หน้าเลนส์ เป็นระยะ S
ภาพที่เกิดขึ้นเป็นระยะ Y หากจากตัวเลนส์ ความยาวโฟกัสของเลนส์จะหาได้จาก 1/f = 1/S + 1/Y
ซึ่ง f > 0 จะเป็นเลนส์นูน
f < 0 จะเป็นเลนส์เว้า

input : s y = 15 30
output :
10.00 cm
เลนส์นูน
'''
import re
numbers = re.compile('-?\d+')


user_input = input()
lib_list = list(map(int, numbers.findall(user_input)))
print(lib_list)
s = lib_list[0]
y = lib_list[1]

#f_1 = (1/15) + (1/30)
#print(f_1)
f = 1/(1/s + 1/y)
print('{:.2f} cm'.format(f))
if f > 0:
    print('เลนส์นูน')
elif f < 0:
    print('เลนส์เว้า')
else:
    pass