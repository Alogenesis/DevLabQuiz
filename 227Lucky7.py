'''
ตั้งแต่ 1 - n มีตัวเลขไหนบ้างที่ประกอบด้วยเลข 7 และ หารด้วย 7 ลงตัว
'''

x = int(input())
lst = []
for i in range(1,x+1):
    str_i = str(i)
    if i % 7 == 0 :
        lst.append(i)
    elif str_i[-1] == '7' :
        lst.append(i)
    else:
        pass

if len(lst) > 0 :
    print(*lst,sep=',')
else:
    print('no seven')