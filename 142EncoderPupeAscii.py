'''
ได้รับข้อความที่เข้ารหัสมาแล้วชื่อ Pupe Code
ซึ่งรูปแบบการเข้ารหัสเป็นดังนี้
text -> binary(ASCII) -> pupe code
ตัวอย่างการเข้ารหัส
A = pupepupupupupupe //(A = 01000001 = pupepupupupupupe)
Ab = pupepupupupupupepupepepupupupepu //(Ab =0100000101100010 = pupepupupupupupepupepepupupupepu)
a	097	01100001	A	065	01000001
b	098	01100010	B	066	01000010
c	099	01100011	C	067	01000011
d	100	01100100	D	068	01000100
e	101	01100101	E	069	01000101
f	102	01100110	F	070	01000110
g	103	01100111	G	071	01000111
h	104	01101000	H	072	01001000
i	105	01101001	I	073	01001001
j	106	01101010	J	074	01001010
k	107	01101011	K	075	01001011
l	108	01101100	L	076	01001100
m	109	01101101	M	077	01001101
n	110	01101110	N	078	01001110
o	111	01101111	O	079	01001111
p	112	01110000	P	080	01010000
q	113	01110001	Q	081	01010001
r	114	01110010	R	082	01010010
s	115	01110011	S	083	01010011
t	116	01110100	T	084	01010100
u	117	01110101	U	085	01010101
v	118	01110110	V	086	01010110
w	119	01110111	W	087	01010111
x	120	01111000	X	088	01011000
y	121	01111001	Y	089	01011001
z	122	01111010	Z	090	01011010
space 00000000
'''

user_code = 'pupepupupupupupepupupepupupupupupupepepupupupepupupupepupupupupupupepupupupupepe' #input()
print(user_code[0:2])
lib_decode = []

#translate pupe code to binary
while len(user_code) > 0:
    x = user_code[0:2]
    if x == 'pu':
        print('go pu')
        lib_decode.append(0)
    elif x == 'pe':
        print('go pe')
        lib_decode.append(1)
    else:
        pass
    user_code = user_code[2:]
    print('now user code =',user_code)

print('lib_decode =',lib_decode)


# Extract 8 digit to 1 string
bin_lib = [] # for put all member in
while len(lib_decode) > 0:
    binary =  lib_decode[0:8] # assign 8 bit to var
    print('binary in process =',binary)

    binary_str = ''.join(str(item) for item in binary)
    print(binary_str,'binary_str')
    bin_lib.append(binary_str)
    print('bin_lib=',bin_lib)

    # cut lib decode 8 digit
    print('lib_decode nct =', lib_decode)
    lib_decode = lib_decode[8:]
    print('lib_decode cut =', lib_decode)



#Loop decode bit to string
for loop_decode in bin_lib:
    #test bit to string
    ascii_string = "" #for assign
    an_integer = int(loop_decode, 2)  #convert to base 2 decimal int
    ascii_character = chr(an_integer) # convert to ascii char
    ascii_string += ascii_character #append char to ascii_string
    print(ascii_string,end='')