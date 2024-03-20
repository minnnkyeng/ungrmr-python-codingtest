# 369게임

def solution(order):
    result = 0
    orders = list(str(order))

    for i in [3, 6, 9]:
        result += orders.count(str(i))

    return result
