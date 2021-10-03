'''
หาเลขฐานสองของคำที่รับมา
เลขฐาน 10 ที่ได้ มาจาก
Fire = 0, Water = 1, Wind = 2, Ground = 3, Light = 4, Dark = 5
แปลงเป็นเลข ฐาน 2 แล้วแสดงค่า 20 bit binary
'''

x = input()
if x == 'Fire':
    print('00000000000000000000')
elif x == 'Water':
    print('00000000000000000001')
elif x == 'Wind':
    print('00000000000000000010')
elif x == 'Ground':
    print('00000000000000000011')
elif x == 'Light':
    print('00000000000000000100')
elif x == 'Dark':
    print('00000000000000000101')
else:
    print('No have this mahou in your library.')