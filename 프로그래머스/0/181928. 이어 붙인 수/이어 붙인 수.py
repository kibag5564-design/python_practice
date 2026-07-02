def solution(num_list):
    o_n = ''
    e_n = ''

    for n in num_list:
        if n % 2 == 1:
            o_n += str(n)
        else:
            e_n += str(n)

    return int(o_n or '0') + int(e_n or '0')