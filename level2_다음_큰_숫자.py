def solution(n):
    answer = 0
    binary_n = bin(n)[2:]
    one_count_n = len(binary_n.replace("0", ""))
    one_count_answer = 0
    
    answer = n
    while one_count_answer != one_count_n:
        answer = answer+1
        binary_answer = bin(answer)[2:]
        one_count_answer = len(binary_answer.replace("0", ""))
    return answer