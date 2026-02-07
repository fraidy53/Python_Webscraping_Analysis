# 문제 5-7(중/하)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared_numbers = list(map(lambda x: x** 2, numbers)) #map(함수, iterable): 모든 값 변형
filtered_numbers = list(filter(lambda x: x>5, numbers))
filtered_squared = list(map(lambda x: x ** 2, filtered_numbers))

print(f"원본 숫자: {numbers}")
print(f"모든 수의 제곱: {squared_numbers}")
print(f"5보다 큰 수들: {filtered_numbers}")
print(f"5보다 큰 수들의 제곱: {filtered_squared}")