import sys

# 첫 번째 입력값을 숫자로 변환해서 num_times에 대입
num_times = int(sys.stdin.readline())

# num_times 만큼 입력값을 받고 더한 후 출력하는 과정 반복
for i in range(num_times):
		# 받아들이는 리스트 값을 int로 변환 -> a,b에 각각 넣음
		a,b = map(int, sys.stdin.readline().split())
		print("Case #"+str(i+1)+":"+str(a+b))