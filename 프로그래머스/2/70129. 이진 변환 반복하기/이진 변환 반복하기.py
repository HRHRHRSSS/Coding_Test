def solution(s):
    cnt2 = 0
    cnt0 = 0
    while s != '1':
        cnt2 +=1
        # 0삭제
        removed0 = s.count('0')
        cnt0 += removed0
        s = s.replace('0','')
        # 길이 -> 2진수 변환
        c = len(s)
        s = bin(c)[2:]
    return [cnt2, cnt0]