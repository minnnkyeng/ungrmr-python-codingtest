# 7의 개수

def solution(array):
    result = 0
    str_array = []

    for num in array:
        str_array += str(num)

    for num in str_array:
        if int(num) == 7:
            result += 1

    return result
