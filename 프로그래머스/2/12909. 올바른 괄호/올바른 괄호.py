
def solution(s):
    stack = []
    
    for i in s:
        if i == '(':
            stack.append(i)
            
        elif i == ')':
            if not stack: # 스택이 비어있는 경우
                return False
            stack.pop()
    
    # len(stack) == 0 이 성립하면 true 출력
    # 처음엔 if 문을 하나 더 썼는데 이 방법으로 코드를 더 줄일 수 있네!
    return len(stack) == 0