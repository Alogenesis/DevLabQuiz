'''
โดยการคำนวณเกรดนั้นจะมีการให้คะแนนตามเกรดแต่ละช่วงเป็น 80- 100 ได้เกรด A , 70 - 79 ได้เกรด B , 60 - 69 ได้เกรด C , 50 - 59 ได้เกรด D และ ต่ำกว่า 50 จะได้เกรด F โดยผู้ใช้จะต้องกรอกเป็นตัวเลขจำนวนเต็มเท่านั้น
'''

score = int(input('Enter your score'))
if score < 50:
  print('F')
elif score < 60:
  print('D')
elif score < 70:
  print('C')
elif score < 80:
  print('B')
elif score < 101:
  print('A')