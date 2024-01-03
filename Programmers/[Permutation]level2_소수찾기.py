from collections import Counter, defaultdict
from math import sqrt, floor

def solution(numbers):
    num_count = Counter(numbers)
    num_count = defaultdict(int, num_count)
    answer = 0
    combinations = set()
    make_permutation("", num_count, combinations)
    combinations = set(map(int, combinations))
    for combi in combinations:
        if check_prime_number(combi):
            answer += 1
    return answer

def make_permutation(previous_combi, numbers, combinations):
    keys = list(numbers.keys())
    if len(keys) <= 0:
        return
    # 각 key별로 모든 조합을 다 생성 한 뒤에 다음 key로 넘어감
    for key in numbers.copy().keys():
        current_combi = previous_combi + key
        combinations.add(current_combi)
        numbers[key] -= 1
        if numbers[key]<= 0:
            numbers.pop(key)
        make_permutation(current_combi, numbers, combinations)
        numbers[key] += 1

def check_prime_number(number):
    if number <= 1:
        return False
    for i in range(2, floor(sqrt(number)+1)):
        if number%i == 0:
            return False
    return True
solution("123")