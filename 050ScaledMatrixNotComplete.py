'''
จงเขียนโปรแกรมรับเมทริกซ์ขนาด m x n และให้ Scale ค่าภายในเมทริกซ์นั้นให้มีค่าอยู่ระหว่าง 0-1 โดยขนาดของเมทริกซ์จะต้องไม่เป็น 1x1

บรรทัดแรก m เป็นจำนวนหลัก
บรรทัดสอง n เป็นจำนวนแถว
บรรทัด m x n ต่อไป เป็นค่าประจำตำแหน่ง

In :
2
6
-4605.16
4768.87
-494.21
6548.12
9198.68
-5335.41
-7206.89
-9559.76
-731.66
2229.36
-8204.81
1053.96

Out :
0.2641 0.7638
0.4833 0.8587
1.0000 0.2252
0.1254 0.0000
0.4706 0.6285
0.0722 0.5658
'''
'''
import array as arr
x = arr.array([['-4605.16'],['4768.87'],['-494.21'],['6548.12'],['9198.68'],['-5335.41']],
              [['-7206.89'],['-9559.76'],['-731.66'],['2229.36'],['-8204.81'],['1053.96']])

m = reshape(x,(2,6))
print(x)
'''
'''
v - min
--------   x (maxscale - minscale)
max - min
'''

#รับค่า row บรรทัดแรก
row = int(input('Input Row >> '))
column = int(input('Input Column >> '))



v_lib = []
v_lib_sort = []
# data input
for i in range(row*column):
    v = float(input('Data >> '))
    v_lib.append(v)
    v_lib_sort.append(v)

#v_lib = [-4605.16,4768.87,-494.21,6548.12,9198.68,-5335.41
#         , -7206.89, -9559.76, -731.66, 2229.36, -8204.81, 1053.96]
#v_lib_sort = [-4605.16,4768.87,-494.21,6548.12,9198.68,-5335.41
#         , -7206.89, -9559.76, -731.66, 2229.36, -8204.81, 1053.96]
v_lib_sort.sort()
print(v_lib_sort)
print(v_lib_sort[0])
print(v_lib_sort[-1])

max = v_lib_sort[-1]  #max input
min = v_lib_sort[0]  #min input
v = -4605.16
a = (v - min) / (max - min)
print(round(a,4))
v_range01 = []

#ตัวแปรสำหรับทั้้ง 2 ฟังก์ชั่น
#row = 2
#column = 6
#คำนวณเทียบบรรยัตไตรยางค์ให้เหลือค่าแค่ 0-1 ทุกตัวแล้วส่งค่าเก็บไว้ใน v_range01
for i in range(0,(row*column)):
    v_result = (v_lib[i] - min) / (max - min)
    v_range01.append(round(v_result,4))
print(v_range01)

#ปริ้นเท่ากับจำนวนคอลัมน์ที่กำหนดไว้
#ถ้า input = 2
if row == 2:
    index = 0
    for i in range(0,column):
        if v_range01[index] == 1.0:
            print('1.0000',end=' ')
        elif v_range01[index] == 0.0:
            print('0.0000',end=' ')
        else:
            print(v_range01[index],end=' ')
        index += 1
        if v_range01[index] == 1.0:
            print('1.0000')
        elif v_range01[index] == 0.0:
            print('0.0000')
        else:
            print(v_range01[index])
        index += 1

#ถ้า input = 3
elif row == 3:
    index = 0
    for i in range(0,column):
        if v_range01[index] == 1.0:
            print('1.0000',end=' ')
        elif v_range01[index] == 0.0:
            print('0.0000',end=' ')
        else:
            print(v_range01[index],end=' ')
        index += 1

        if v_range01[index] == 1.0:
            print('1.0000',end=' ')
        elif v_range01[index] == 0.0:
            print('0.0000',end=' ')
        else:
            print(v_range01[index],end=' ')
        index += 1

        if v_range01[index] == 1.0:
            print('1.0000')
        elif v_range01[index] == 0.0:
            print('0.0000')
        else:
            print(v_range01[index])
        index += 1

