'''
รับค่าเป็นตัวอักษร จากนั้นทำการแปลงเป็น ตัวเลข
เช่น a = 97 ,b= 98
แล้วนำตัวเลขที่แปลงจากแต่ละตัวมาทำการยกกำลังด้วย จำนวนอักษรทั้งหมด เช่น abc
แปลง a=97,b=98,c=99 แล้วมายกกำลังด้วยจำนวนตัวอักษรทั้งหมด คือ 3 (abc = 3 จำนวน)
97**3 =912673
98**3=941192
99**3=970299
นำตัวเลขทั้งหมดมาบวกรวมกัน ได้ 2824164
จากนั้นนำเลขทุกตัวมาบวกกันเรื่อยๆ จนเหลือ แค่ตัวเดียว
ยกตัวอย่าง
2+8+2+4+1+6+4= 27 => 2+7 =9
'''

str_input = input()
asc_lib = []
for i in str_input:
    asc_lib.append(ord(i))

print(asc_lib)

pow_number = len(str_input)
print(pow_number)

ascpow_lib = []
for i in asc_lib:
    ascpow_lib.append(i**pow_number)

print(ascpow_lib)
# Sum all to 1 string
sum_ascpow = 0
for i in ascpow_lib:
    sum_ascpow += i
print(sum_ascpow)

# Mini - Set before loop
sum_val = sum_ascpow

while sum_val >= 10:
    # Convert to string add to lib
    num_str = str(sum_val)
    print(num_str)
    print(type(num_str))
    num_str_lib = []
    for i in num_str:
        num_str_lib.append(i)
    print(num_str_lib)


    # Sum string lib to 1 int line
    sum_val = 0
    for i in num_str_lib:
        sum_val += int(i)
    print(sum_val)

print(sum_val)

