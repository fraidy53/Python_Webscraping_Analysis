# 문제 8-1(중/하)
import math

def circle_area(radius):
    return math.pi * radius ** 2
def rectangle_area(width, height):
    return width * height
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a