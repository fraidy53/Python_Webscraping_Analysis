# 문제 5-10(중/하)
score = 85
result = "합격" if score >= 80 else "불합격"
print(f"점수: {score}, 결과: {result}")

age = 17
status = "성인" if age >= 19 else "미성년자"
print(f"나이: {age}, 상태: {status}")

numbers = [10, 42, 7, 23]
max_value = numbers[0] if numbers[0] > numbers[1] else numbers[1]
max_value = max_value if max_value > numbers[2] else numbers[2]
max_value = max_value if max_value > numbers[3] else numbers[3]
print(f"숫자들의 최대값: {max_value}")

nums = [5, -3, 12, 0, 8, -1, 23]
positive_nums = [n for n in nums if n> 0]
print(f"양수들: {positive_nums}")