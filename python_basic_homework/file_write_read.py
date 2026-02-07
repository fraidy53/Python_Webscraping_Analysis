# 문제 7-1(중/하)
filename = "sample.txt"
content = [
    "안녕하세요\n",
    "파이썬 파일 처리를 연습하고 있습니다\n",
    "오늘은 좋은 날씨입니다\n"
]

print("파일에 저장할 내용: ")
for line in content:
    print(line, end="")
with open(filename, "w", encoding="utf-8") as file:
    file.writelines(content)
print("\n파일에서 읽어온 내용:")
with open(filename, "r", encoding="utf-8") as file:
    read_content = file.readlines()
    for line in read_content:
        print(line, end="")