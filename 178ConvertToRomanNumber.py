'''
เปลี่ยนตัวเลขเป็นเลขโรมัน
ตัวอักษรเลขโรมันจะมี I = 1 , V = 5 , X = 10 , L = 50 , C = 100 , D = 500 , M = 1000
'''

x = int(input())

class py_solution:
    def int_to_Roman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num


print(py_solution().int_to_Roman(x))
