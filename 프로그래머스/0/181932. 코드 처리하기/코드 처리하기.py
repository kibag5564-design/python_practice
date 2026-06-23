def solution(code):
    ret = []
    mode = 0
    
    for idx in range(len(code)):
        if code[idx] == "1":
            # 0이면 1로, 1이면 0으로 전환 (1 - mode 토글 연산 활용)
            mode = 1 - mode
        else:
            # mode가 0일 때는 짝수(idx % 2 == 0)만, mode가 1일 때는 홀수(idx % 2 == 1)만 추가
            if idx % 2 == mode:
                ret.append(code[idx])
                
    # 리스트를 문자열로 합쳐준 후 빈 문자열 체크
    answer = "".join(ret)
    return answer if answer else "EMPTY"