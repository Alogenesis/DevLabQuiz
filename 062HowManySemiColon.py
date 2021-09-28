'''
จงเขียนโปรแกรมรับค่า String มา1 ตัวเเล้วให้นำจำนวน semi conlon ว่ามีกี่ตัว
'''

sum = 0
x = 'a) apples; b) pears; c) bananas'

for i in x:
    if i ==';':
        sum = sum + 1

print(sum)