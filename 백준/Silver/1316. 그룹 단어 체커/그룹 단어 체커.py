import sys

n = int(sys.stdin.readline().strip())
count = 0

for i in range(n):
    tempstr = str(sys.stdin.readline().strip())
    lst = list(set(tempstr))  # 중복 제거한 문자 리스트
    
    all_adjacent = True  # 모든 문자가 인접해야 함

    for p in lst:
        idxlst = [q for q, char in enumerate(tempstr) if char == p]

        # 인접한 인덱스의 차이가 1인 경우
        if len(idxlst) > 1 and not all(abs(idxlst[z] - idxlst[z + 1]) == 1 for z in range(len(idxlst) - 1)):
            all_adjacent = False  # 하나라도 인접하지 않으면 False로 변경
            break  # 더 이상 확인할 필요 없음

    if all_adjacent:  # 모든 문자가 인접한 경우
        count += 1

print(count)
