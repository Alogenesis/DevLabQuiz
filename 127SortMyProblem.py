'''
เมธีต้องการบวกเลขคณิตศาสตร์ แต่ตัวเลขที่ต้องการบวกเรียงมาไม่สวย เพราะตัวเลขไม่ได้เรียงจากน้อยไปมาก!
มันบวกยาก ไม่มีชั้นเชิง ฉะนั้นเราต้องเขียนโปรแกรมสำหรับการเรียงเลขให้กับเมธี ก่อนที่เมธีจะได้บวกเลขได้อย่างมีชั้นเชิง
In : 1+2+3+1+2+3+1+2+3+1+2+3
Out : 1+1+1+1+2+2+2+2+3+3+3+3
'''

user_input = '1+2+3+1+2+3+1+2+3+1+2+3'
xn = user_input.split('+')
x = []
for i in xn:
    x.append(int(i))
print(x)

x.sort(reverse=False)
print(x)

for j in range(len(x)-1):
    print(x[j],end='+')
print(x[-1])

