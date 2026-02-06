# 문제 3-8(중/하)

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 3]

print(f"원본 리스트: {numbers}")

unique_numbers = sorted(set(numbers)) # set: 중복 제거, sort: 정렬

print(f"중복 제거 후: {unique_numbers}")