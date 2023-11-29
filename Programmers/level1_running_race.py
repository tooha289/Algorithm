def solution(players, callings):
    answer = []
    player_rank = {v: i for i, v in enumerate(players)}
    rank_player = {i: v for i, v in enumerate(players)}

    for call in callings:
        call_rank = player_rank[call]
        pre_rank = call_rank-1
        pre_player = rank_player[pre_rank]
        
        # 불려진 사람의 등수를 줄이기
        player_rank[call] = pre_rank
        rank_player[pre_rank] = call
        # 불려진 사람의 앞사람 등수를 늘이기
        player_rank[pre_player] = call_rank
        rank_player[call_rank] = pre_player

    answer = list([0]*len(players))
    for rank, player in rank_player.items():
        answer[rank] = player
    return answer

players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]
