# 올바른 괄호

def solution(s):
    answer = True
    while s.find('()') != -1:
        s_index = s.find('()')
        if s_index == 0:
            s = s[s_index+2:]
        else:
            s = s[0:s_index] + s[s_index+2:]
        print(s)

    if len(s) == 0:
        answer = True
    else:
        answer = False

    return answer
