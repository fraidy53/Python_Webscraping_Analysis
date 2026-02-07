# 문제 5-8(중/하)
point = (10, 20)
x, y = point
print(f"좌표: x={x}, y={y}") #언패킹

numbers = [1, 2, 3]
a, b, c = numbers
print(f"리스트 언패킹: a={a}, b={b}, c={c}") # 리스트 길이와 변수 개수가 반드시 같아야 함

def sum_numbers(*args): # 가변 위치 인수: 함수에 몇 개의 인수가 들어올지 모를 때 사용. 전달된 값들은 튜플로 묶임
    return sum(args)

print(f"가변 인수의 합: {sum_numbers(10, 20, 30)}") 

def print_info(**kwargs): #kwargs: 이름=값 형태로 전달된 인수들을 딕셔너리로 묶어줌
    info = ", ".join(f"{key}={value}" for key, value in kwargs.items())
    print(f"키워드 인수들: {info}")

print_info(name="김철수", age=25, city="서울")