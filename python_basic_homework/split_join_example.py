# 문제 5-1(중/하)
text = "Python is awesome programming language"

# split 사용
words = text.split(" ")
print(f"원본 문자열: {text}")
print(f"분리된 단어들: {words}")

# join 사용(하이픈 연결)
hyphen_text = "-".join(words)
print(f"하이픈으로 연결: {hyphen_text}")

# 대문자로 변환 후 공백으로 연결
upper_text = " ".join(word.upper() for word in words)
print(f"대문자로 변환 후 공백으로 연결: {upper_text}")