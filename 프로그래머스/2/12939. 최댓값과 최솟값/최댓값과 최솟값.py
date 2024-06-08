def solution(s):
    # 처음엔 map을 쓰지않음
    # 그래서 배열 요소가 문자열이었다
    # 따라서 max, min을 쓸 때 인덱스의 최대최소를 찾는 문제가 발생
    arr = list(map(int, s.split(' ')))
    
    maxnum = max(arr)
    minnum = min(arr)
    
    # 처음엔 다시 문자열으로 만들어서 붙이려고 함
    # 근데 그냥 f"" 쓰면 되네 ! 
    return f"{minnum} {maxnum}"
    
