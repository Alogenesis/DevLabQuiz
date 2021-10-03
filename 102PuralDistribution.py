'''
พหุนามดีกรีสาม เมื่อแยกตัวประกอบแล้ว จะอยู่ในรูปของ (ax+b)(cx+d)(ex+f)=0
เมื่อกระจายพหุนามแล้ว จะอยู่ในรูปของ Ax^3+Bx^2+Cx+D=0
จงเขียนโปรแกรมที่รับค่าของ a,b,c,d,e,f แล้วแสดงผลออกมาเป็นค่าของ A,B,C,D

input : มีบรรทัดเดียว รับค่าของจำนวนเต็ม a,b,c,d,e,f คั่นด้วยช่องว่าง 1 ช่อง แทนจำนวนใน (ax+b)(cx+d)(ex+f)=0
Out : มีบรรทัดเดียว แสดงผลเป็นจำนวนเต็ม A,B,C,D คั่นด้วยช่องว่าง 1 ช่อง
In : 1 -1 2 5 3 -2 (a,b,c,d,e,f)
Out : 6 5 -21 10 (A,B,C,D)
'''

user_input = input()
af,bf,cf,df,ef,ff = user_input.split(' ')
a = int(af)
b = int(bf)
c = int(cf)
d = int(df)
e = int(ef)
f = int(ff)

A = a*c*e
B = (a*c*f) + (a*d*e) + (b*c*e)
C = (a*d*f) + (b*c*f) + (b*d*e)
D = b*d*f
print(A,B,C,D)
'''
(ace)*X^3 + (acf + ade + bce)*X^2 + (adf + bcf + bde)*X + bdf
'''