'''
บรรทัดแรก จำนวนรอบที่วิ่ง เป็นจำนวนเต็ม
บรรทัดสองเป็นเงินที่ได้จากการวิ่งแต่ละรอบ
เช่น
2(รอบ)
20(เงินในแต่ละรอบ)

แสดงอกกมาว่า รอบที่ .. ได้ เงินเท่าไหร่ และบรรทัดสุดท้ายบอกผลรวมเงินทั้งหมด
เช่น
1(รอบที่)-20(เงินในแต่ละรอบรอบ)
2-20
40(เงินรวม)

In :
4 (รอบที่วิ่ง)
20 (จำนวนเงินต่อรอบ)

Out :
1-20 (แต่ละรอบได้เท่ากัน)
2-20
3-20
4-20
80 (รวมเงิน)
'''

run_round = int(input())
money_gain = int(input())
sum_money = run_round * money_gain
for i in range(0,run_round):
    print(i+1,end='')
    print('-',end='')
    print(money_gain)
print(sum_money)