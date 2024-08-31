def solution(numbers):
    # 문자열으로 비교를 해야 한다
    # 이어붙였을 때 더 큰 수를 만들 수 있는 순서 찾기 위해
    answer = ' '
    numbers = [str(i) for i in numbers]
    numbers.sort(key=lambda x: x*3, reverse=True)
    answer = str(int(''.join(numbers)))
    return answer