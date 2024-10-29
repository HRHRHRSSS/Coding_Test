import sys
n = str(sys.stdin.readline().strip())

lst = list(n)
lst = [int(i) for i in lst]
lst.sort(reverse=True)
lst = [str(i) for i in lst]

print(int(''.join(lst)))