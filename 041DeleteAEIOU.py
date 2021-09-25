'''
ให้เขียนโปรแกรมที่ทำการลบตัวอักษรสระในภาษาอังกฤษออกจากประโยคทุกตัวอักษร
Welcome to BornToDev
Wlcm t BrnTDv
'''

x = input('>> ')
vowel = 'aeiou'
vowel_c = 'AEIOU'
out = []

for i in x:
    if i == vowel[0] or i == vowel_c[0]:
        #print('i = a')
    elif i == vowel[1] or i == vowel_c[1]:
        #print('i = e')
    elif i == vowel[2] or i == vowel_c[2]:
        #print('i = i')
    elif i == vowel[3] or i == vowel_c[3]:
        #print('i = o')
    elif i == vowel[4] or i == vowel_c[4]:
        #print('i = u')
    else:
        #print('Not AEIOU')
        out.append(i)

print(out)
for i in out:
    print(i, end='')