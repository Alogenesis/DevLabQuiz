'''
คุณจะได้รับจำนวนเต็มบวก N พิมพ์สามเหลี่ยมเชิงตัวเลขที่มีความสูง N-1 ดังรูปด้านล่าง:
n = 4
1
22
333
...﻿

'''

x = int(input())
for i in range (0,x-1):
    print(str(i+1) * (i+1))