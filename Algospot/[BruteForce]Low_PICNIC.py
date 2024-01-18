from collections import defaultdict
import sys

def find_pairs(prev, num, friends, is_pair):
    if len(is_pair)==num:
        return 1
    result = 0
    for friend in sorted(list(friends)):
        if prev >= friend:
            continue
        if friend in is_pair:
            continue
        is_pair.add(friend)
        for pair in friends[friend]:
            if pair in is_pair:
                continue
            is_pair.add(pair)
            result += find_pairs(friend, num, friends, is_pair)
            is_pair.discard(pair)
        is_pair.discard(friend)
    return result

input = sys.stdin.readline

# number of test cases
C = int(input())

for i in range(C):
    # number of students, number of friend pairs
    n, m = map(int, input().strip().split())

    # 친구 dict
    # N번 친구는 자기보다 높은 번호의 친구만 저장한다.
    friends = defaultdict(list)
    # 짝이 결정되었는지 set
    is_pair = set()

    input_friends = map(int, input().strip().split())
    for j, friend in enumerate(input_friends):
        if j%2==0:
            previous = friend
            continue
        if previous > friend:
            previous, friend = friend, previous
        friends[previous].append(friend)
    result = find_pairs(-1, n, friends, is_pair)
    print(result)
    

