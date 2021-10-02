'''
กำหนดให้ N (1<=N<=12) แทนเดือน เช่น 1 แทนมกราคม 2 แทนกุมภาพันธ์ ไปเรื่อย ๆ จนถึง 12 แทน ธันวาคม
ให้วันที่ i เป็นวันที่ดี (Lucky Day) ก็ต่อเมื่อ เลขของวันที่ i บวกกับเลขของเมื่อวาน แล้วหารด้วย N ลงตัว
จงหาว่าเดือนที่ N จะมีวันที่ดีกี่วัน
(กำหนดให้กุมภาพันธ์มี 28 วัน)
(ถ้าหากวันนั้นเป็นวันที่ 1 ให้เมื่อวานเป็นวันสุดท้ายของเดือนที่แล้ว เช่น วันที่ 1 เมษายน ทำให้เมื่อวานคือวันที่ 31 มีนาคม)
'''

n = int(input())
sum_lucky_day = 0
if n == 1 or n == 3 or n == 5 or n == 7 or n == 8 or n == 10 or n == 12:
    for i in range(1,32):
        if i == 1 and n ==1:
            luckyday = (i + (31)) % n
            # print(i)
            # print(luckyday)
            if luckyday == 0:
                sum_lucky_day += 1
        elif i == 1 and n == 3:
            luckyday = (i + (28)) % n
            # print(i)
            # print(luckyday)
            if luckyday == 0:
                sum_lucky_day += 1
        elif i == 1 and n == 5:
            luckyday = (i + (30)) % n
            # print(i)
            # print(luckyday)
            if luckyday == 0:
                sum_lucky_day += 1
        elif i == 1 and n == 7:
            luckyday = (i + (30)) % n
            # print(i)
            # print(luckyday)
            if luckyday == 0:
                sum_lucky_day += 1
        elif i == 1 and n == 8:
            luckyday = (i + (31)) % n
            # print(i)
            # print(luckyday)
            if luckyday == 0:
                sum_lucky_day += 1
        elif i == 1 and n == 10:
            luckyday = (i + (30)) % n
            # print(i)
            # print(luckyday)
            if luckyday == 0:
                sum_lucky_day += 1
        elif i == 1 and n == 12:
            luckyday = (i + (30)) % n
            # print(i)
            # print(luckyday)
            if luckyday == 0:
                sum_lucky_day += 1
        else:
            luckyday = (i + (i-1)) % n
            #print(i)
            #print(luckyday)
            if luckyday == 0:
                sum_lucky_day += 1
elif n == 2:
    for i in range(1,29):
        if i == 1:
            luckyday = (i + (31)) % n
            #print(i)
            #print(luckyday)
            if luckyday == 0:
                sum_lucky_day += 1
        else:
            luckyday = (i + (i-1)) % n
            #print(i)
            #print(luckyday)
            if luckyday == 0:
                sum_lucky_day += 1
else:
    for i in range(1,31):
        luckyday = (i + (i-1)) % n
        #print(i)
        #print(luckyday)
        if luckyday == 0:
            sum_lucky_day += 1

print(sum_lucky_day)

