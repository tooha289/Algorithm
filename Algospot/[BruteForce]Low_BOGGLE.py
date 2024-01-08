import sys
from collections import defaultdict
# 갈수 있는 방향
DIRECTIONS = [[-1,-1],
              [0,-1],
              [1,-1],
              [-1,0],
              [1,0],
              [-1,1],
              [0,1],
              [1,1]]

def find_word(word, position, characters, check):
    if len(word) <= 0:
        check[0] = True
        return

    char = word[0]
    positions = characters[char]
    if len(positions) <= 0:
        return
    # 초기 함수 실행(첫번째 문자)
    if position==None:
        for position in positions:
            find_word(word[1:], position, characters, check)
            if check[0]:
                return
        return
    # 이후 함수 실행(이후 문자)
    for col, row in DIRECTIONS:
        next_col = row + position[0]
        next_row = col + position[1]
        if next_col < 0 or next_row < 0:
            continue
        next_position = (next_col, next_row)
        if next_position not in positions:
            continue
        find_word(word[1:], next_position, characters, check)
        if check[0]:
            return
input = sys.stdin.readline

# C: number of test cases
C = int(input())
answers = []
for i in range(C):
    board = []
    characters = defaultdict(set)
    for i in range(5):
        line = input().strip()
        board.append(line)
        for j, char in enumerate(line):
            characters[char].add((i, j))
    # N: number of words we know
    N = int(input())
    for j in range(N):
        word = input().strip()
        check = [False]
        find_word(word, None, characters, check)
        answers.append([word, "YES" if check[0] else "NO"])
for word, result in answers:
    print(word, result)


# TEST CASE
    
# 4
# URLPM
# XPRET
# GIAET
# XTNZY
# XOQRS
# 10
# PRETTY
# GIRL
# REPEAT
# KARA
# PANDORA
# GIAZAPX
# REPEAT
# KARA
# PANDORA
# URLPMPMPMM
# NNNNS
# NEEEN
# NEYEN
# NEEEN
# NNNNN
# 4
# YESR
# SNNNNNNN
# EEEEEEEEE
# NEYN
# NNNNN
# NEEEN
# NEYEN
# NEEEN
# NSNNN
# 1
# YES
# AAAAA
# AAAAA
# AAAAA
# AAAAA
# AAAAB
# 4
# ABABABABAA
# AAAAAAAAAB
# ABABABABBA
# BAAAAAAABA