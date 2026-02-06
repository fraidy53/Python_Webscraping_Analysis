# 문제 3-9(중/하)
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

print(f"리스트1: {list1}")
print(f"리스트2: {list2}")

merged_list = sorted(set(list1) | set(list2)) # |:두 리스트 합치고 중복 제거 후 정렬
common_elements = sorted(set(list1) & set(list2)) # &: 두 리스트에 둘 다 있는 값만(교집합)하고 중복 제거 후 정렬

print(f"병합된 리스트: {merged_list}")
print(f"공통 요소: {common_elements}")
