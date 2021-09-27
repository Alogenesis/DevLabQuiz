'''
บอกว่าประโยคไหนยาววกว่า แต่ละประโยคยาวกี่ตัวอักษร เรียงจากมากไปน้อย
'''

a = input()
b = input()
ac = len(a)
print(ac)
bc = len(b)
print(bc)
answer = []
answer.append(ac)
answer.append(bc)
answer.sort(reverse=True)
print(answer)
print('---------')
for i in answer:
    print(i)