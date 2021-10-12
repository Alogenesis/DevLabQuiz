'''
ให้รับค่ามา 2 บรรทัด
บรรทัดแรกคือ วันใน 1 สัปดาห์(วันไหนก็ได้)
บรรทัดที่สองคือ จำนวนเต็ม n ที่มากกว่าหรือเท่ากับ 0
โปรแกรมจะคำนวณว่า จากวันในบรรทัดแรกไปอีก n วันจะเป็นวันอะไร

monday
6
>> sunday

'''

nowsday = input().lower()
next_to = int(input())

days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
print(days)

index = days.index(nowsday)
print(index)
ans_day = nowsday
while next_to > 0 :
    next_to -= 1
    index += 1
    if index == 7 : #reset index 7 to 0
        index = 0
    ans_day = days[index]


print(ans_day)