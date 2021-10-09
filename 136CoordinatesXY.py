'''
ต้องการสร้างตารางรูป (#) โดยมีการระบุพิกัดไว้
โดยจุดที่ระบุพิกัดจะแทนที่ด้วย (*) ซึ่งพิกัดคู่อันดับ (0,0)
จะอยู่ที่มุมล่างซ้ายของตาราง เมื่อไปทางขวา x จะเพิ่ม และเมื่อไปด้านบน y จะเพิ่ม
Output เป็นตารางที่จุด Mark จะอยู่ และหากคู่อันดับ (x,y) เกินขนาดของตารางก็จะมี Output ว่า That position is not loaded.
(2,3)
7

#######
#######
#######
##*####
#######
#######
#######
'''


po2 = input()
po1 = po2.replace('(','')
position = po1.replace(')','')
#print(position)
xr,yr = position.split(',')
x = int(xr)
y = int(yr)
#print(x)
#print(y)
row = int(input())


sharp = '#'
change = '#'
cl = list(change)
#cl[x] = '*'
x_pos = ''.join(cl)

#print(sharp)
#print(x_pos)

#create list = row member
blist = []
answer_lib = []
normal = 0
for i in range(0,row):
    blist.append(sharp)

index_counter = 0
for i in blist:
    if x >= row or y >= row:
        print('That position is not loaded.')
        break
    elif index_counter == y:
        change = '#'*row
        cl = list(change)
        cl[x] = '*'
        x_pos = ''.join(cl)
        #print(y_pos)
        answer_lib.append(x_pos)
        index_counter += 1
    else:
        #print('#'*row)
        normal = '#'*row
        index_counter +=1
        answer_lib.append(normal)

answer_lib.reverse()
print(answer_lib)

for i in answer_lib:
    print(i)

