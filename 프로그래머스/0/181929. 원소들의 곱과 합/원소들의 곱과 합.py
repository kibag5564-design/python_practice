def solution(num_list):
    total_sum = 0
    total_mul = 1
    answer = 0
    
    for num in num_list:
        total_mul *= num
        total_sum += num
        
        if total_mul < total_sum ** 2:
            answer = 1
        else:
            answer = 0
        
    return answer