import sys
areas = [
    [(0,1), (1,0)],
    [(0,1), (1,1)],
    [(1,0), (1,-1)],
    [(1,0), (1,1)]
]

def cover_board(board):
    width = len(board[0])-2
    height = len(board)-2
    y, x = 0, 0

    for r in range(1, height+1):
        for c in range(1, width+1):
            if board[r][c]==0:
                y, x = r, c
                break
        if y!=0: 
            break
    # 모든칸이 1로 채워져 있을 경우
    if y==0:
        return 1
    ret = 0
    for area in areas:
        is_cover = True
        for dy, dx in area:
            if board[y+dy][x+dx]==1:
                is_cover = False
                break
        if is_cover == False:
            continue

        # 현재 area 채우기
        board[y][x] = 1
        for dy, dx in area:
            board[y+dy][x+dx] = 1

        # 재귀 호출
        ret += cover_board(board)

        # 현재 area 지우기
        board[y][x] = 0
        for dy, dx in area:
            board[y+dy][x+dx] = 0
    return ret

input = sys.stdin.readline
# number of test cases
C = int(input())
for i in range(C):
    # board height, width
    H, W = map(int, input().strip().split())
    board = []
    num_white = 0
    # board 주위로 1로 padding
    board.append([1]*(W+2))

    for row in range(H):
        line = input().strip()
        blocks = []
        blocks.append(1)
        for char in line:
            if char == "#":
                blocks.append(1)
            elif char == ".":
                blocks.append(0)
                num_white += 1
        blocks.append(1)
        board.append(blocks)
    board.append([1]*(W+2))
    answer = 0
    if num_white % 3 != 0:
        print(answer)
    else:
        answer = cover_board(board)
        print(answer)
