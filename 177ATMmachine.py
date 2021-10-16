'''
รูปเเบบ Input
input จะเป็นจำนวนเงินที่ต้องการจะกด

output จะเป็นจำนวนธนบัตรที่จะออกมาจากตู้ เช่น
1000 * 3
500 * 1
100 * 6

ธนบัตรในตู้มี 3 ชนิดคือ 1000 500 100
'''

x = int(input())

thousand = 0
fiveh = 0
oneh = 0

while x > 0 :
    if x >= 1000 :
        thousand += 1
        x -= 1000
    elif x >= 500 :
        fiveh += 1
        x -= 500
    elif x >= 100 :
        oneh += 1
        x -= 100
    else:
        pass

print('1000 *',thousand)
print('500 *',fiveh)
print('100 *',oneh)
