'''
รับค่าเป็นตัวเลข ถ้าหาร 3 ลงตัวให้คืนค่า Fizz ถ้าหาร 2 ลงตัวให้คืนค่า Buzz ถ้าลงตัวทั้ง 2 และ 3 ให้คืนค่า FizzBuzz
'''

x = int(input())
if x % 2 == 0 and x % 3 == 0:
    print('FizzBuzz')
elif x % 2 == 0:
    print('Buzz')
elif x % 3 == 0:
    print('Fizz')
else:
    pass