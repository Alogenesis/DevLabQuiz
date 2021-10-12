'''
นาย A ได้เดินทางไปทำงานที่สถานที่หนึ่งซึ่งสถานที่นั้นมีแต่เลขโรมัน
แต่นาย A ไม่สามารถอ่านเลขโรมันได้จึงได้ทำการจ้างเราซึ่งเป็นโปรแกรมเมอร์ให้เขียนโค้ดที่แปลงจากเลขโรมันเป็นเลขอารบิกเพื่อช่วยเขา
จงทำการเขียนโปรแกรม ที่รับinputเป็นเลขโรมันและแสดงoutpuเป็นเลขอารบิก
IV > 4
MD > 1500
LX > 60
'''


ans_sum = 0
num_input = input()
if num_input == 'CM':
    print(900)
    ans_sum += 900
elif num_input == 'CD':
    print(400)
    ans_sum += 1000
elif num_input == 'C':
    print(100)
    ans_sum += 100
elif num_input == 'M':
    print(1000)
    ans_sum += 1000
elif num_input == 'D':
    print(500)
    ans_sum += 500
elif num_input == 'XL':
    print(40)
    ans_sum += 40
elif num_input == 'XC':
    print(90)
    ans_sum += 90
elif num_input == 'L':
    print(50)
    ans_sum += 50
elif num_input == 'IX':
    print(9)
    ans_sum += 9
elif num_input == 'IV':
    print(4)
    ans_sum += 4
elif num_input == 'X':
    print(10)
    ans_sum += 10
elif num_input == 'V':
    print(5)
    ans_sum += 5
elif num_input == 'I':
    print(1)
    ans_sum += 1
else:
    ans_sum = 0
    for i in num_input:
        if i == 'M':
            ans_sum += 1000
        elif i == 'D':
            ans_sum += 500
        elif i == 'C':
            ans_sum += 100
        elif i == 'L':
            ans_sum += 50
        elif i == 'X':
            ans_sum += 10
        elif i == 'V':
            ans_sum += 5
        elif i == 'I':
            ans_sum += 1
    print(ans_sum)



I = 1
IV = 4
V = 5
IX = 9
X = 10
#XL = 40
#L = 50
#XC = 90
#C = 100
#CD = 400
#D = 500
#CM = 900
#M = 1000