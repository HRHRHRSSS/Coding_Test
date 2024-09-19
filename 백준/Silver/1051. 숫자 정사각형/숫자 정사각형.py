# 입력
N, M = map(int, input().split())
matrix = []

# 입력 받기
for _ in range(N):
    matrix.append(list(map(int, list(input().strip()))))  # 입력 처리 부분 수정

# 가장 큰 변의 길이를 구함
max_side = min(N, M)

# 큰 변의 크기부터 줄여가며 탐색
for side in range(max_side, 0, -1):
    for i in range(N - side + 1):
        for j in range(M - side + 1):
            # 꼭짓점 확인
            if matrix[i][j] == matrix[i+side-1][j] == matrix[i][j+side-1] == matrix[i+side-1][j+side-1]:
                print(side * side)  # 찾으면 즉시 출력하고 종료
                exit()