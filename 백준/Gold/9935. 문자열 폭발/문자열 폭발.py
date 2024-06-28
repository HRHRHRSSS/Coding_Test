import sys

str = sys.stdin.readline().strip()
explore_str = sys.stdin.readline().strip()
explore_str_length = len(explore_str)

answer = []

for i in str:
	answer.append(i)
	# 만약 스택의 마지막 글자가 폭발문자열과 일치하면
	if ''.join(answer[-explore_str_length:]) == explore_str:
		# 일치하면, 폭발 문자열 길이만큼 스택에서 제거
			del answer[-explore_str_length:]
			
# 모든 문자를 처리한 후 스택에 남아있는 문자들을 합쳐서 결과를 만듦
result = ''.join(answer) if answer else "FRULA"
print(result)