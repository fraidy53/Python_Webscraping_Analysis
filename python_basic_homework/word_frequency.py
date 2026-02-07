# 문제 7-3(중/하)
filename = "sample.txt"

text = """파이썬은 쉬운 프로그래밍 언어입니다
파이썬 프로그래밍을 배우기 쉽습니다
파이썬은 강력한 언어입니다
"""
with open(filename, "w", encoding="utf-8") as file:
    file.write(text)

word_count = {}

with open(filename, "r", encoding="utf-8") as file:
    for line in file:
        words = line.strip().replace("입니다", "").replace("을", "").replace("은", "").split()
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

print("단어 빈도 분석 결과: ")
for word, count in word_count.items():
    print(f"{word}: {count}번")