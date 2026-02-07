# 문제 5-3(중/하)
fruits = ['사과', '바나나', '오렌지', '포도', '딸기']

print("과일 목록: ")
for index, fruit in enumerate(fruits): # enumerate(): 인덱스 + 값 동시 반환
    print(f"{index} : {fruit}")