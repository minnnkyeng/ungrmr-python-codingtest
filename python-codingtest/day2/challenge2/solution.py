# 없는 숫자 더하기

def solution(numbers):
    answer = -1

    arr = list(range(0, 10))
    answer = sum(set(arr) - set(numbers))

    return answer
