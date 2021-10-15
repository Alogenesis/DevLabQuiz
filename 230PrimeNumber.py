'''
หาจำนวนเฉพาะของเลขระหว่างนี้ เช่น 1 - 10
concept จำนวนเฉพาะ จะหารได้แค่ตัวมันเอง
'''


start = int(input())
end = int(input()) +1

# data
found = 0
prime_lst = []

for i in range(start,end):
    #print(i)

    # check prime factor
    #g = 37      #ตัวที่จะเช็คว่าเป็น prime มั้ย เดี๋ยวเปลี่ยนเป็น i
    can_divide = 0
    if i == 1 :
        pass
    else:
        for n in range(2,i): # ไม่รวมตัวมันเอง ดังนั้น ผลลัพธ์ต้อง = 0
            if i % n == 0 :
                can_divide += 1

        if can_divide == 0 :
            #print(g, 'is prime number')
            found += 1
            prime_lst.append(i)
        else:
            #print('Not prime number')
            pass

#Answer
print('found:',found)
print(prime_lst)
