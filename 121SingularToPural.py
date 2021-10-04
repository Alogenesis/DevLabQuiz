'''
การเปลี่ยนคำเอกพจน์ เป็นพหูพจน์ ในภาษาอังกฤษนั้น มีกฏอยู่
1.คำนามเอกพจน์ที่ลงท้ายด้วย s, x, z, sh, ch ให้เติม es
Ex. bus -> buses
2.คำนามเอกพจน์ที่ลงท้ายด้วย y และด้านหน้า y เป็นพยัญชนะ (ที่ไม่ใช่ a, e, i, o, u เพราะว่าเป็นตัวสระ) ให้ตัด y แล้วเติม ies
Ex. baby -> babies
3.หากไม่ตรงตามที่กล่าวมา เติม s ได้เลย
Ex.boat -> boats
'''

x = input()

last = x[-1]
second_last = x[-2:]
#print(x[-2])
#print(len(x))
xy = len(x) - 1
#print(xy)
#print(x[0:xy])



if last == 's' or last =='x' or last == 'z' or second_last == 'sh' or second_last == 'ch':
    print(x,' -> ',x,'es',sep='')
elif last == 'y':
    print(x,' -> ',x[0:xy],'ies',sep='')
else:
    print(x,' -> ',x,'s',sep='')