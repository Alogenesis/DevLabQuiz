'''
นายเอ คิดโจทย์คณิตศาสตร์ขึ้นมาจำนวน 1,234 ข้อ โดยให้นายบี เป็นคนทำ
โดยนายบี จะทำโจทย์ตั้งแต่วันที่ n ถึงวันที่ m ในวันแรกที่เริ่มทำโจทย์นั้นนายบี จะทำโจทย์ทั้งหมด k ข้อ
และในแต่ละวันนายบี จะทำโจทย์มากขึ้นวันละ A ข้อ
In :
บรรทัดเดียว รับจำนวนเต็มบวก n, m, k และ A ตามลำดับ
Out :
บรรทัดเดียว มีสองกรณีคือ
1.สามารถทำโจทย์ได้ทั้งหมดให้แสดงคำว่า "YES"
2.ไม่สามารถทำโจทย์ทั้งหมดได้ทันเวลาให้แสดงจำนวนข้อที่เหลือ

'''
# 1 5 10 200
user_input = input()
sp = user_input.split(' ')
total = 1234
start = int(sp[0])
end = int(sp[1])
do = int(sp[2])
doplus = int(sp[3])

#print(start)
#print(end)
#print(do)
#print(doplus)

#start date
total = total - do

#current
for i in range(start,end):
    print(i)
    total = total - (doplus*i)

print(total)

# ทำทั้งหมดกี่ข้อ
m = end
n = start
k = do
A = doplus
Sn=((m-n+1)*(2*k+(m-n)*A))/2
answer = 1234 - Sn
print(Sn)

if answer >= 0:
    print(int(answer))
else:
    print('YES')
