import sys

lst=[]
answer=[]

n = int(sys.stdin.readline())
for _ in range(n):
    p,q = map(int, sys.stdin.readline().split())
    lst.append([p,q])
    
for x,y in lst:
    count = 0
    for p,q in lst:
        if x<p and y<q:
            count+=1
    answer.append(count+1)

# join은 문자열 리스트에서만 사용가능
# 정수를 문자열로 변환해서 출력
print(' '.join(map(str,answer)))
        