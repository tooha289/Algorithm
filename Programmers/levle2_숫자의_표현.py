import math
from collections import deque

def solution(n):
    if n<=1: return n
    answer = 1
    sum_queue = deque()
    for i in range(math.ceil(n/2), 0, -1):
        sum_queue.append(i)
        sum_num = sum(sum_queue)
        
        if sum_num<n:
            continue
        if sum_num==n:
            answer+=1
        sum_queue.popleft()            
        
    return answer