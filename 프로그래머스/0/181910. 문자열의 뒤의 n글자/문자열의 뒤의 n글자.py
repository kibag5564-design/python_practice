def solution(my_string, n):
    answer = ''
    for i in range(n+1):
        answer = my_string[-i:]
    return answer