# 문제 6-2(중/하)
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n-1)

def factorical_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

nums = [5, 7]

for num in nums:
    print(f"{num}! (재귀) = {factorial_recursive(num)}")
    print(f"{num}! (반복) = {factorical_iterative(num)}")

