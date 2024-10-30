import sys

n = int(input())

endPoint = 0
answer = 0
arr = []

for _ in range(n):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    arr.append([a,b])
    
arr.sort(key=lambda x:(x[1],x[0]))

for newStart, newEnd in arr:
    if endPoint <= newStart:
        answer += 1
        endPoint = newEnd

print(answer)