import sys

n = int(sys.stdin.readline().strip())
lst = list(map(int, sys.stdin.readline().strip().split()))

lst.sort()
answer = [0]*n

for i in range(n):
    answer[i] = answer[i-1]+lst[i]
print(sum(answer))