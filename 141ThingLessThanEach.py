'''
คล้ายการตรวจสอบว่าเป็นสามเหลี่ยมไหม แต่มีสมาชิกlist n ตัว
เช่น
input: [2,3,4,5]
output: true
นั้นคือ
2<3+4+5
3<2+4+5
4<2+3+5
5<2+3+4
(ต้องเป็นจริงทุกกรณี)
'''

gg = '[222,224,223]' #input()
x1 = gg.replace('[','')
x2 = x1.replace(']','')
x3 = x2.split(',')
x = []
for i in x3:
    x.append(int(i))

print(x)


sum = 0
spec = 0
ans = 0
non = 0
for i in x:
    sum = sum + i
print('sum =',sum)

for static in x:
    spec = sum - static
    print('static=',static,'sum=',sum)
    print(spec,'spec')
    if static <= spec:
        ans += 1
    else:
        non += 1

if non > 0:
    print('false')
else:
    print('true')

