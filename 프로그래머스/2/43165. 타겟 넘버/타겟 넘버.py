def solution(numbers, target):
    def dfs(idx, current_sum):
        # 모든 숫자를 사용한 경우(끝까지 탐색)
        if idx == len(numbers):
            if current_sum == target:
                return 1
            else:
                return 0
        else:
            add_case = dfs(idx+1, current_sum + numbers[idx])
            subtract_case = dfs(idx+1, current_sum - numbers[idx])
            
            return add_case + subtract_case
    # 첫 번째 인덱스와 합계 0에서 시작            
    return dfs(0,0)