'''
ในการส่งข้อความเพื่อไม่ให้ผู้อื่นสามารถอ่านได้โดยง่ายสามารถทำได้โดยทำการสลับคำในประโยคใหม่จากหลังไปหน้า และเราเป็นคนที่จะต้องเขียนโปรแกรมเพื่อถอดรหัสนี้ออกมาตามตัวอย่าง
In : life. social crumbling a and responsibilities, bills, with except again old years six be to good feel it does DAMN AND Bandicoot Crash played first I when 6 was I
Out : I was 6 when I first played Crash Bandicoot AND DAMN does it feel good to be six years old again except with bills, responsibilities, and a crumbling social life.
'''
string = input('Type a sentense. : ')
word = string.split()
words = list(reversed(word))
print(' '.join(words))