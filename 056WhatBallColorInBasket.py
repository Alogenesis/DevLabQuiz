'''
ในเวลาว่างของนายเซฟ เขามักจะชอบคิดโจทย์ปัญหามาให้เพื่อนๆของเขาแก้เสมอ วันนึงเขาเดินมาพร้อมกับถัง 3 ใบที่มีลูกบอลอยู่เต็มถัง
เขาถามเพื่อนของเขาว่าในถังใบที่หนึ่งและสองมีลูกบอลสีอะไรบ้างที่เหมือนกัน และสีที่เหมือนกันนั้นต้องไม่มีอยู่ในถังที่สามด้วย
เราที่สามารถเขียนโปรแกรมได้ จะเขียนโปรแกรมช่วยเพื่อนของนายเซฟได้อย่างไร
Out : สีของลูกบอลที่มีอยู่ในถังที่หนึ่งและสอง แต่ไม่มีอยู่ในถังที่สาม (กรณีที่ไม่มีลูกบอลสีใดเลยที่ตรงตามเงื่อนไข ให้ผลลัพธ์ออกเป็น none)

Input: b1=[red,green,blue] b2=[black,green,white] b3=[blue]
Out : green
'''

user_input = 'b1=[yellow,orange,red] b2=[brown,black,yellow] b3=[orange,red]'
sep_input = user_input.split(' ')
print(sep_input)
print(type(sep_input))
print(sep_input[0])
print(type(sep_input[0]))
print('------------------------')

#remove char
b1_1 = sep_input[0].replace('b1=[','')
b1_2 = b1_1.replace(']','')
b1 = b1_2.split(',')
print(b1)
print(type(b1))

b2_1 = sep_input[1].replace('b2=[','')
b2_2 = b2_1.replace(']','')
b2 = b2_2.split(',')
print(b2)
print(type(b2))

b3_1 = sep_input[2].replace('b2=[','')
b3_2 = b3_1.replace(']','')
b3 = b3_2.split(',')
print(b3)
print(type(b3))

print('------------------------')
print('------------------------')
#Loop for check color
# 1 check 2
match1_2 = []
for i in b1: #run b1 1 2 3 second
    for j in b2: #run b2: 1 2 3 first
        if i == j:
            print('b1',i ,'=', 'b2', j)
            match1_2.append(i)
        else:
            print('Not match')
print('------------------------')
print('Match 1+2 =', match1_2)
#check 1+2 unmatch 3
match = []
unmatch = 0
for m in match1_2:
    for l in b3: #run b3 first
        if l == m:
            unmatch = unmatch + 1
        else:
            match.append(m)

#remove duplicate of match
answer = []
for n in match:
    if n not in answer:
        answer.append(n)

#print answer
if unmatch > 0:
    print('none')
else:
    print(*answer)

print('Now match =',match)
'''
#check color and append to list
b1 = sep_input[0]
b2 = sep_input[1]
b3 = sep_input[2]

if 'red' in b1 :
    print('b1 have red')
elif 'green' in b1:
    print('b1 have green')
elif 'blue' in b1:
    print('b1 have blue')
elif 'black' in b1:
    print('b1 have black')
elif 'white' in b1:
    print('b1 have white')
elif 'brown' in b1:
    print('b1 have brown')
elif 'orange' in b1:
    print('b1 have orange')
elif 'pink' in b1:
    print('b1 have pink')
elif 'yellow' in b1:
    print('b1 have yellow')
else:
    print('No color')
'''
