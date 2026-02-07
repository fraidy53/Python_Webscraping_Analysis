# 문제 4-2(중/하)

multiples = []

for i in range(1, 101):
    if i %3 == 0:
        multiples.append(i)

print(f"1부터 100까지 3의 배수: {multiples}")
print(f"3의 배수의 합: {sum(multiples)}")
print(f"3의 배수의 개수: {len(multiples)}개")
