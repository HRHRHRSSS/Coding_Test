import sys

k,n = map(int,sys.stdin.readline().split())
arr = []
for _ in range(k):
    i = int(sys.stdin.readline())
    arr.append(i)
    
arr.sort()

left=1
right = max(arr)

while left<=right:
    mid = (left+right)//2
    cnt=0
    for i in arr:
        cnt+=i//mid
    if cnt < n:
        right = mid-1
    else:
        left = mid+1
print(right)