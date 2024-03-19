# 문자열 나누기

def solution(s):
    result = x_num = etc_num = 0
    x = ''

    for i in range(0, len(s)):
        if x == '':
            x = s[i]

        if x == s[i]:
            x_num += 1
        else:
            etc_num += 1

        if (x_num == etc_num) | (i == len(s)-1):
            result += 1
            x = ''

    return result
