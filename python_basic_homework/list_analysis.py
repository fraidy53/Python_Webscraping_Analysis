# 문제 3-6(중/하)

numbers = [15, 3, 27, 8, 19, 12, 31]

print(f"숫자 목록: {numbers}")

max_value = max(numbers)
min_value = min(numbers)

unique_numbers = list(set(numbers))
unique_numbers.sort(reverse=True)
second_max = unique_numbers[1]

print(f"최댓값: {max_value}")
print(f"최솟값: {min_value}")
print(f"두 번째로 큰 값: {second_max}")