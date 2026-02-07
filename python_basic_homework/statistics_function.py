# 문제 6-4(중/하)
import math

def calculate_statistics(numbers):
    mean = sum(numbers) / len(numbers)
    max_value = max(numbers)
    min_value = min(numbers)

    variance = sum((x - mean) ** 2 for x in numbers) / (len(numbers) - 1)
    std_dev = math.sqrt(variance)

    return mean, max_value, min_value, std_dev
nums = [10, 20, 30, 40, 50]
mean, max_value, min_value, std_dev = calculate_statistics(nums)

print(f"숫자들: {nums}")
print(f"평균: {mean}")
print(f"최댓값: {max_value}")
print(f"최솟값: {min_value}")
print(f"표준편차: {std_dev:.2f}")