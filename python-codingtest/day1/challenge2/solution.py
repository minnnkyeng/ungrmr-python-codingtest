# 369게임

def solution(order):
    result = 0
    checks = [3, 6, 9]
    orders = list(map(int, str(order)))

    for check in checks:
        for order in orders:
            if order == check:
                result += 1
                orders.pop(orders.index(order))
            continue
    return result
