# 문제 7-5(중/하)
filename = "system.log"

logs = [
    "2025-07-20 09:15:00 - WARNING - 메모리 사용량이 높습니다",
    "2025-07-20 10:30:00 - ERROR - 데이터베이스 연결 실패",
    "2025-07-20 11:45:00 - ERROR - 파일을 찾을 수 없음",
    "2025-07-20 12:00:00 - WARNING - 디스크 공간 부족"
]

with open(filename, "w", encoding="utf-8") as file:
    for log in logs:
        file.write(log + "\n")

error_logs = []
warning_logs = []

with open(filename, "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if "ERROR" in line:
            error_logs.append(line)
        elif "WARNING" in line:
            warning_logs.append(line)

print("ERROR 레벨 로그들: ")
for log in error_logs:
    print(log)
print("\nWARNING 레벨 로그들: ")
for log in warning_logs:
    print(log)