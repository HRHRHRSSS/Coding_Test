import sys

n,k = map(int, sys.stdin.readline().strip().split())
lst = []
for i in range(n):
    lst.append(int(sys.stdin.readline().strip()))

# 동전 가치 리스트를 내림차순으로 정렬
lst.sort(reverse=True)

count = 0
for coin in lst:
    if k == 0:
        break
    if coin <= k:
        count += k // coin
        k = k % coin   
print(count)
        