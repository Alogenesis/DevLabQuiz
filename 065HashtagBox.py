'''
ให้สร้างกล่องสี่เหลี่ยมที่มีความสูงเป็น n
โดยที่ความสูงของกล่องต้องมากกว่า 2 ถ้าน้อยกว่าให้แสดงว่า "Box's height must be more than 2"
Input:8
Output:
########
#      #
#      #
#      #
#      #
#      #
#      #
########
'''

x = 8
if x <= 2 :
    print("Box's height must be more than 2")
else:
    a = x
    b = x
    print('#' * x)
    for i in range(0, b - 2):
        print('#' + (' ' * (b - 2)) + '#')
    print('#' * x)


