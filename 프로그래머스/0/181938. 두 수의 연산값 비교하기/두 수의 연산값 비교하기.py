def solution(a, b):
    answer = 0
    ab = int(str(a) + str(b))
    mp = 2*a*b
    if ab >= mp:
        answer = ab
    else:
        answer = mp
        
    return answer