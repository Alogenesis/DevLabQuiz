'''
โดร่าและผองเพื่อนของเธอได้ทำการสำรวจเกาะต่างๆ จากแผนที่ของเธอ ซ
ึ่งเธอต้องการให้คุณช่วยนับเกาะในแผนที่ว่ามีจำนวนเกาะทั้งหมดกี่เกาะในแผนที่
ซึ่งในแผนที่นั้น จะใช้ # แทนสัญลักษณ์ของพื้นดิน และ . แทนสัญลักษณ์ของน้ำ
ซึ่งถ้าพื้นดินอยู่ติดกัน(ทิศเหนือ ทิศใต้ ทิศตะวันออกและทิศตะวันตก)จะถือว่าเป็นเกาะเดียวกัน

รูปเเบบ Input
บรรทัดแรก รับค่าจำนวนเต็มบวก n และ m หมายถึง ขนาดของแถวและคอลลัมของแผนที่ตามลำดับ
อีก n บรรทัดต่อมา รับค่า # หรือ . หมายถึง สัญลักษณ์ของแผนที่ จำนวน m ตัว

รูปเเบบ Output
จำนวนเกาะทั้งหมด

4 4     Row + Column len()
###.    # land  . water
##..
#.##
.###
>> 2

5 5
...##
...#.
.##..
...#.
#.##.
>> 4

concept
บรรทัดเดียวกันมีกี่เกาะ
.### or ###. or ##.. or ..## or #... or ...# == 1
##.# or #.## ==2

ตำแหน่งบน เช็คล่าง ที่ตำแหน่งเดียวกัน มี # อยู่มั้ย ถ้ามี = เกาะเดียวกัน / ไม่มี = คนละเกาะ
บรรทัด 2 เช็ค 3 ไม่มี # ในตำแหน่งเดียวกัน เกาะ +1
บรรทัด 3 เช็ค 4 ไม่มี # ในตำแหน่งเดียวกัน เกาะ +1
บรรทัด 4 เช็ค 5 มี #
บรรทัด 5 เช็ค 4 มี # 1 และไม่มี # 1
'''

class NumIsland:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])
        sum = 0

        for i in range(m):
            for j in range(n):

                if grid[i][j] == ".":
                    continue
                else:

                    # sum up only once per chance of meeting "1"
                    sum += 1
                    stack = list()
                    stack.append([i, j])

                    # visit each "1" in the adjacent area using a stack
                    while len(stack) != 0:

                        [p, q] = stack.pop()

                        if p >= 1 and grid[p - 1][q] == "#":
                            stack.append([p - 1, q])

                        if p < m - 1 and grid[p + 1][q] == "#":
                            stack.append([p + 1, q])

                        if q >= 1 and grid[p][q - 1] == "#":
                            stack.append([p, q - 1])

                        if q < n - 1 and grid[p][q + 1] == "#":
                            stack.append([p, q + 1])

                        # mark as visited
                        grid[p][q] = "."

        return sum


a = input()
b,c = a.split(' ')
val = int(b)
loop = int(c)

grid = []
for i in range(0,loop):
    get = input()
    lst = []
    for j in get:
        lst.append(j)
    grid.append(lst)

print(grid)







NumIsland.numIslands(self, grid)