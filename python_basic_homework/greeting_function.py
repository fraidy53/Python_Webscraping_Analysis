# 문제 6-3(중/하)
def greet(name, greeting="안녕하세요", message=""):
    if message:
        print(f"{greeting}, {name}님! {message}")
    else:
        print(f"{greeting}, {name}님!")
greet("김철수")
greet("John", greeting="Hello")
greet("이영희", message="좋은 하루 되세요!")