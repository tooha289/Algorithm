def solution(triangle):
    answer = 0
    ans_tri = triangle.copy()

    for depth in range(len(ans_tri)):
        if depth == 0:
            continue
        for i, node in enumerate(ans_tri[depth]):
            parent = ans_tri[depth - 1]
            if i == 0:
                ans_tri[depth][i] = parent[0] + node
            elif i == len(ans_tri[depth]) - 1:
                ans_tri[depth][i] = parent[-1] + node
            else:
                ans_tri[depth][i] = max(parent[i - 1] + node, parent[i] + node)
    # print(max(ans_tri[depth]))
    answer = max(ans_tri[depth])
    return answer
