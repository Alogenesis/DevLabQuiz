'''
รับเลขมาแล้วเรียงกลับหลัง
In :
4 บรรทัดแรกบอกว่ารับกี่ครั้ง
5
2
1
3
Out :
3
1
2
5

'''
nloop = int(input('Loop Number > '))
lib = []
for i in range(nloop):
  x = int(input('Number > '))
  lib.append(x)

lib.reverse()
#print(lib)
for i in range(len(lib)):
  print(lib[i])