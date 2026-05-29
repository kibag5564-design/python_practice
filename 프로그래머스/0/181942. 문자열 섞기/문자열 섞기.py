def solution(str1, str2):
    answer = ""
    
    # str1과 str2에서 같은 순서의 글자들을 꺼내 각각 a와 b에 담아라!
    for a, b in zip(str1, str2):
        answer += a + b
        
    return answer