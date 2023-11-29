import numpy as np

def solution(A,B):
    answer = 0
    a = np.sort(np.array(A))[::-1]
    b = np.sort(np.array(B))

    answer = int(sum(a*b))
    return answer

def solution(A,B):
    answer = 0
    a = sorted(A)[::-1]
    b = sorted(B)
    ab = zip(a, b)
    
    mulitplied_ab = [a*b for a, b in ab]
    answer = sum(mulitplied_ab)
    return answer