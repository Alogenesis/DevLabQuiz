'''
ให้แยกตัวอักษรที่เป็นสระของภาษาอังกฤษออกมาจากคำที่กำหนด
In :
My feelings are overwhelmed by you.3

Out :
eeiaeoeeeou
Myflngsrvrwhlmdbyy
'''

user_input = input()
vowels = []
word = []
for i in user_input:
    if i in 'aeiouAEIOU':
        vowels.append(i)
    elif i.isalpha():
        word.append(i)
    else:
        pass

print(*vowels,sep='')
print(*word,sep='')