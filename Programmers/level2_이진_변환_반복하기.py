def to_binary(num):
    binaries = []
    while num!=0:
        binaries.append(num%2)
        num = num//2
    return "".join(map(str,binaries[::-1]))

def solution(s):
    answer = [0, 0]
    
    while s!='1':
        pre_len = len(s)
        next = s.replace('0', '')
        next_len = len(next)

        diff_len = pre_len - next_len
        s = to_binary(next_len)

        answer[0] += 1
        answer[1] += diff_len

    return answer