'''
ให้หาว่าจากที่ list ของเลขที่กำหนดให้ ตัวไหนบ้างที่หารด้วย 7 ลงตัวและหารด้วย 11 ไม่ลงตัว
in : 1,2,3,4,5,6,7,8,9,10
out : 1,7
'''

x = '1,2,3,4,5,6,7,8,9,10'
a = x.split(',')
print(a)
n = []
for i in a:
    print(i)
    b = int(i)
    n.append(b)

print(n)
answer = []
for j in n:
    if j == 1:
        answer.append(1)
    elif j % 7 == 0 and j % 11 != 0 :
        answer.append(j)
    #elif j % 7 == 0 :
    #    answer.append(7)
    #elif j % 11 == 0:
    #    answer.append(11)
    else:
        pass


#print(*answer)

#remove duplicate of match
output_answer = []
for n in answer:
    if n not in output_answer:
        output_answer.append(n)
#print(output_answer)
print(*output_answer,sep=',')