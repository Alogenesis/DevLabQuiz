'''
บรรทัดแรกเป็นการนำเข้าค่า n,k,m,p โดยแสดงโดยคั่นด้วยช่องว่างตามลำดับ
บรรทัดที่สองเป็นการนำเข้าสตริงของชุดคำตอบของเฉลย
บรรทัดที่สามเป็นการนำเข้าสตริงของชุดคำตอบของผู้ทำข้อสอบ

In :
5 3 2 1
ABABB
AXXBA

Out : Your score:6
'''
#Input 1
n = '10 2 1 0' #จำนวนข้อทั้งหมด
score = n.split(' ')
total = int(score[0])
k = int(score[1]) #คะแนนข้อถูก
m = int(score[2]) #คะแนนที่ถูกหักเมื่อทำผิด
p = int(score[3]) #คะแนนที่ได้เมื่อไม่ได้ทำ X
#Execute
print(total)
print(k)
print(m)
print(p)
# Input 2
correct = 'ABBABABAAB'
lib_correct = []
for i in correct:
    lib_correct.append(i)
print(lib_correct)

# Input 3
user_answer = 'AXAXBBAXXA'
lib_user = []
for j in user_answer:
    lib_user.append(j)
print(lib_user)

#Cal Score

correct_score = 0
wrong_score = 0
ignore_score = 0
run_correct = 0
for l in user_answer:
    if l == 'X':
        ignore_score += 1
    elif l == lib_correct[run_correct]: # run = 0  correct
        correct_score += 1
    elif l != lib_correct[run_correct]: # run = 0  wrong
        wrong_score += 1
    else:
        pass
    run_correct += 1

print(correct_score)
print(wrong_score)
print(ignore_score)
sum_score = (correct_score*k) - (wrong_score*m) + (ignore_score*p)
print('Your score:',end='')
print(sum_score)