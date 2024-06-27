import sys

n = int(sys.stdin.readline().strip())

for i in range(n):
    num = int(sys.stdin.readline().strip())
    print(('++++ '*(num//5)+' '+'|'*(num%5)).strip())
