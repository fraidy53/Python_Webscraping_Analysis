# 문제 3-4(중/하)

import math

point1 = (0,0)
point2 = (3,4)

x1, y1 = point1
x2, y2 = point2

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print("두 점사이의 거리: ", distance)