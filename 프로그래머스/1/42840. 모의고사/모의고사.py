def solution(answers):
    answer = [0 for i in range(3)]
    
    # 답안 패턴 정의
    man1 = [1,2,3,4,5]
    man2 = [2,1,2,3,2,4,2,5]
    man3 = [3,3,1,1,2,2,4,4,5,5]
    
    # 답안 비교 및 맞힌 문제 수 계산
    for i in range(len(answers)):
        ans = answers[i]
        if(man1[i%len(man1)] == ans):
            answer[0] += 1
        if(man2[i%len(man2)] == ans):
            answer[1] += 1
        if(man3[i%len(man3)] == ans):
            answer[2] += 1 
    
    result = []
    for i in range(len(answer)):
        if(answer[i] == max(answer)):
            # result에는 수포자의 번호를 저장
            # 수포자의 번호는 1부터 시작하니까 i+1
            result.append(i+1)
    
    return sorted(result)