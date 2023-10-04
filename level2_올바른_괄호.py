def solution(s):
    answer = True
    brackets = []

    for bracket in s:
        if bracket == "(":
            brackets.append(bracket)
        # 왼쪽 소괄호가 아니고 괄호 스택이 비어있으면 올바르지 않은 괄호
        elif len(brackets) < 1:
            return False
        # 왼쪽 소괄호가 아니고 괄호 스택이 비어있지 않은 경우
        brackets.pop()
    if len(brackets) == 0:
        return True
    return False


solution("()()")
