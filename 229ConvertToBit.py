'''
แปลงเลขฐานที่กำหนดไปเป็นเลขฐาน 10
เลขฐาน 2 5 10 16
'''

base_get = int(input())
txt = input()

if base_get == 2 :
    print(int(txt, 2))

elif base_get == 5 :
    print(int(txt, 5))

elif base_get == 16 :
    print(int(txt, 16))
else:
    print(txt)