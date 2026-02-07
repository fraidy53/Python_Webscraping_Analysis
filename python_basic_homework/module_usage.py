# 문제 8-2 (중/하)
import datetime
import random

now = datetime.datetime(2025, 7, 20, 14, 30, 25)
print(f"현재 날짜와 시간: {now}")

formatted_date = now.strftime("%Y년 %m월 %d일 %A")

weekday_map = {
    "Monday": "월요일",
    "Tuesday": "화요일",
    "Wednesday": "수요일",
    "Thursday": "목요일",
    "Friday": "금요일",
    "Saturday": "토요일",
    "Sunday": "일요일"
}
for eng, kor in weekday_map.items():
    formatted_date = formatted_date.replace(eng, kor)

print(f"포맷된 날짜: {formatted_date}")
print(f"임의의 숫자: {random.randint(1, 10)}")
print(f"임의의 실수: {random.uniform(1, 5):.2f}")

fruits = ["사과", "바나나", "오렌지", "포도", "딸기"]
print(f"임의의 리스트 요소: {random.choice(fruits)}")

random.shuffle(fruits)
print(f"섞인 리스트: {fruits}")