def solution(a, b, flag):
    answer = 0
    if flag == True:
        answer = a + b
    elif flag == False:
        answer = a - b
    return answer