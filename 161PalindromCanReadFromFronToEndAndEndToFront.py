'''
ให้เขียนโปรแกรมในการตรวจสอบ Palindrome เช่น 'asoi' ไม่เป็น Palindrome เพราะว่า
หลังจาก reverse แล้วได้ iosa ไม่ตรงกับ asoi ที่ยังไม่ revrse เป็นต้น
In : รับค่าจาก argument ใน function checkPalindrome(str)
abba
Out : return ข้อความ str is a Palindrome หรือ str is not palindrome
abba is a palindrome.
'''

x = input()
y = x[::-1]
#print(y)

if x == y:
    print(x,'is a palindrome.')
else:
    print(x,'is not a palindrome.')