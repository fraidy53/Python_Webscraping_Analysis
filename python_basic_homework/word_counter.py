# 문제 2-4(중/하)
sentence = input("문장을 입력하세요: ")

# 앞뒤 공백 제거 + 중간 여러 공백을 하나로
clean_sentence = " ".join(sentence.split())
word_count = len(clean_sentence.split())

print("공백 제거: ",clean_sentence)
print(f"단어 개수: {word_count}")