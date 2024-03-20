# 연속된 수의 합

def solution(num, total):
    answer = []

    start_num = int((total-sum(range(0, num))) / num)
    answer = list(range(start_num, start_num + num))

    return answer
