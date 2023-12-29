# failed

from collections import defaultdict
def solution(a, b, g, s, w, t):
    time_weights = defaultdict(lambda: [0, 0])
    for i in range(len(t)):
        gold = g[i]
        silver = s[i]
        weight = w[i]
        time = t[i]

        gold -= weight
        index = 1
        remains = 0
        while gold > 0:
            weight_gold = time_weights[time*index][0]
            if weight_gold >= a:
                break
            if a - weight_gold >= weight:
                weight_gold += weight*index
                index+=2
            else:
                remains = weight - (a - weight_gold)
        
        weight_silver = time_weights[time*index][1]
        silver -= remains
        if remains>0 and silver>0:
            weight_silver += remains

        while silver > 0:
            break

    answer = -1
    return answer

solution(10, 10, [100], [100], [7], [10])