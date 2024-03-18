# 문자열 나누기

def solution(s):
    answer = 0

    x = a = ''
    x_num = etc_num = 0

    a_list = []

    for i in range(0, len(s)):

        a += s[i]

        if x == '':
            x = s[i]
            x_num = 1
            continue

        if x == s[i]:
            x_num += 1
        else:
            etc_num += 1

        if x_num == etc_num:
            a_list.append(a)
            x = a = ''
            etc_num = 0

        if i == len(s)-1:
            a_list.append(a)

    answer = len(a_list)

    return answer


print(solution('banana'))
print(solution('abracadabra'))
print(solution('aaabbaccccabba'))