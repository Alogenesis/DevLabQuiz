'''
คิดโปรแกรมหนึ่งขึ้นมาโดยให้คุณช่วยเป็นคนเขียนโค้ด นั้นโดยโปรแกรมนั้นคือ Finding Number นั่นเอง งานของคุณคือ ให้รับค่า n แทนจำนวนช่อง ของชุดข้อมูล
และในบรรทัดสุดท้ายให้รับค่าที่ต้องการหาในชุดข้อมูล โดยมีเงื่อนไขคือ แต่ละจำนวนของชุดข้อมูลนั้นจะไม่ซ้ำกัน

บรรทัดแรก รับค่าจำนวนเต็มบวก n (0<n<=1000)
บรรทัดที่ 2 รับค่าจำนวนเต็มบวกเป็นจำนวน n ตัว
บรรทัดที่ 3 รับต่าจำนวนเต็มบวกที่ต้องการหา

In :
5
4 2 5 7 1
1
Out : Yes

In :
10
1 2 3 4 5 6 7 8 9 10
12
Out : No
'''

length = int(input('length >> '))

#รับค่าทั้งหมดในบรรทัดเดียว
lib_data = []
database = input('Database > ')
lib_data = database.split(' ')
print(lib_data)


#ตัวที่ต้องการหา
user_input = input('Find for >> ')
if user_input in lib_data:
    print('Yes')
else:
    print('No')

