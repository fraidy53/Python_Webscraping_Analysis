# 문제 7-2(중/하)
import csv

filename = "grades.csv"

students = [
    ('김철수', 85),
    ('이영희', 92),
    ('박민수', 78),
    ('최수진', 95)
]

with open(filename, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["이름", "점수"])
    writer.writerows(students)
print("학생 성적이 grades.csv에 저장되었습니다.\n")

total = 0
count = 0

print("성적 분석 결과")

with open(filename, "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)

    for name, score in reader:
        score = int(score)
        print(f"{name}: {score}점")
        total += score
        count += 1
average = total / count
print(f"전체 평균: {average:.1f}점")
