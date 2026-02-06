# 문제 3-2(중/하)

fruits = ['사과', '바나나', '오렌지', '포도', '딸기']

target = input("찾을 과일을 입력하세요: ")

print(f"과일 목록: {fruits}")

if target in fruits:
    print(f"'{target}'가 목록에 있습니다!")
else:
    print(f"'{target}'가 목록에 없습니다.")