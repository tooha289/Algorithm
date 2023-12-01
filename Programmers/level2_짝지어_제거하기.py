from collections import Counter, deque

# 완전탐색 풀이
def solution(s):
    while True:
        len_prev = len(s)
        for i in range(len(s)-1):
            if s[i]==s[i+1] and i+2 < len(s):
                s = s[:i] + s[i+2:]
                break
            elif s[i]==s[i+1] :
                s = s[:i]
                break
        len_after = len(s)
        if len_prev == len_after:
            return 0
        if len_after == 0:
            return 1
    return 0

# 스택을 이용한 풀이
def solution(s):
    answer = -1
    
    # 짝지어 제거할 수 없으면 0을 리턴
    counts = Counter(s)
    for count in counts.values():
        if count%2 != 0:
            return 0
    
    stack = deque(s[0])
    
    # 앞에서부터 스택의 top과 비교하며 진행
    for i in range(1, len(s)):
        current = s[i]
        
        if len(stack)==0:
            stack.append(current)
            continue
            
        top = stack.pop()
        
        if top==current:
            continue
        else:
            stack.append(top)
            stack.append(current)
            
    # 짝지어 제거할 수 없으면 0을 리턴
    if len(stack)%2 !=0:
        return 0
    
    # 스택에 남아있는 문자열 처리
    while len(stack)>1:
        first = stack.pop()
        second = stack.pop()
        if first!=second:
            return 0
    
    # 스택에 문자열이 남아있으면 0을 리턴
    if len(stack)>0:
        return 0
    
    return 1