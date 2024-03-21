# 완주하지 못한 선수

def solution(participant, completion):
    for i in range(0, len(completion)):
        c_index = participant.index(completion[i])
        participant.pop(c_index)

    answer = ''.join(participant)

    return answer
