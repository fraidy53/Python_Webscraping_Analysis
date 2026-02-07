# 문제 4-5(중/하)

num = int(input("숫자를 입력하세요: "))

if num <= 1:
    print(f"{num}은 소수가 아닙니다.")
else:
    is_prime = True
    for i in range(2, num):
        if num %i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num}은 소수입니다.")
    else:
        print(f"{num}은 소수가 아닙니다.")