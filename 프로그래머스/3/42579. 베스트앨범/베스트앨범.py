from collections import defaultdict

def solution(genres, plays):
    music_map = defaultdict(int)
    music_num = defaultdict(int)
    for p1,p2 in zip(genres,plays):
        music_map[p1] += p2
    for i in range(len(plays)):
        music_num[i] += plays[i]
    
    # music_map을 값을 기준으로 정렬
    music_map = sorted(music_map.items(),key=lambda x:x[1],reverse=True)
      
    answer = []
    for g,k in music_map:
        idx = []
        for i,v in enumerate(genres):
            if g==v:
                idx.append(i)
        idx_sort = sorted(idx, key=lambda x:music_num[x],reverse=True)
        if len(idx)==1:
            answer.append(idx_sort[0])
        else:
            answer.append(idx_sort[0])
            answer.append(idx_sort[1])
    
    return answer