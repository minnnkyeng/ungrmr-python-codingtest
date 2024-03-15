# 제일 작은 수 제거하기

def solution(arr):
    answer = []

    arr.remove(min(arr))

    if len(arr) > 0:
        answer = arr
    else:
        answer.append(-1)

    return answer
