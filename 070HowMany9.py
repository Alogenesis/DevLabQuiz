'''
รับinput 2 ตัว เป็นเลขจำนวนเต็ม ให้หาว่าระหว่างเลขนั้นมีเลข 9 อยู่กี่ตัว
เช่น 0-10 มี 9 อยู่ 1 ตัว คือ 9
80 - 100 มี 9 อยู่ 12 ตัว คือ 89 90 91 92 93 94 95 96 97 98 99(นับเป็น 2)
'''

x = int(input())
y = int(input())

nine = 0
for i in range(x,y+1):
    #print(i)
    if '999' in str(i):
        #print(i, '999 in here')
        nine = nine + 3
    elif '99' in str(i):
        #print(i, '99 in here')
        nine = nine + 2
    elif '9' in str(i):
        #print(i, '9 in here')
        nine = nine + 1

print(nine)