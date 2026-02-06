#문제 1-2 (중/하)
pi = 3.14159

r = int(input("원의 반지름을 입력하세요: "))

area = pi * r * r
circumference = 2 * pi * r

print(f"반지름이 {r}인 원의 넓이: {area:.2f}")
print(f"반지름이 {r}인 원의 둘레: {circumference:.2f}")