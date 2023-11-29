def solution(s):
    numbers = [int(x) for x in s.split(" ")]
    answer = f"{min(numbers)} {max(numbers)}"
    return answer
