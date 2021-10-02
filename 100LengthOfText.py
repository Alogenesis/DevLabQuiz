'''
เรียงข้อความจากความยาวน้อยไปความยาวมาก
'''

num_text = int(input())
txt_lib = []
for n in range(0,num_text):
    txt1 = input()
    txt_lib.append(txt1)

txt_lib.sort(key=len)
for i in txt_lib:
    print(i)