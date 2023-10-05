# def solution(s):
#     stack = []
#     for n in range(len(s)):
#         count = 0
#         is_right = True

#         for bracket in s:
#             if bracket in ("(", "[", "{"):
#                 stack.append(bracket)
#                 if len(stack) == 1:
#                     count += 1
#             elif len(stack) == 0:
#                 is_right = False
#                 break
#             elif bracket == ")":
#                 top = stack.pop()
#                 if top != "(":
#                     is_right = False
#                     break
#             elif bracket == "]":
#                 top = stack.pop()
#                 if top != "[":
#                     is_right = False
#                     break
#             elif bracket == "}":
#                 top = stack.pop()
#                 if top != "{":
#                     is_right = False
#         if len(stack) > 0:
#             is_right = False
#         if is_right:
#             return count

#         first = s[0]
#         s = s.replace(first, "")
#         s += first
#     return 0


# print(solution("}]()[{"))

def solution(s):
    stack = []
    for n in range(len(s)):
        count = 0
        is_right = True

        for bracket in s:
            if bracket in ("(", "[", "{"):
                stack.append(bracket)
                if len(stack) == 1:
                    count += 1
            elif len(stack) == 0:
                is_right = False
                break
            elif bracket == ")":
                top = stack.pop()
                if top != "(":
                    is_right = False
                    break
            elif bracket == "]":
                top = stack.pop()
                if top != "[":
                    is_right = False
                    break
            elif bracket == "}":
                top = stack.pop()
                if top != "{":
                    is_right = False
        if len(stack) > 0:
            is_right = False
        if is_right:
            pass

        first = s[0]
        s = s.replace(first, "", 1)
        s += first
        print(s)
    return 0

solution("[[]{}](){}")