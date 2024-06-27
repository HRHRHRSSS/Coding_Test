import sys

working_time = 0
for i in range(5):
    # 한 줄을 읽고 양쪽 공백을 제거
    line = sys.stdin.readline().strip()
    # 공백을 기준으로 문자열을 분리
    start_str, end_str = line.split()
    
    start_hour, start_min = map(int, start_str.split(':'))
    end_hour, end_min = map(int, end_str.split(':'))

    hour_time = (end_hour - start_hour)*60
    min_time = (end_min - start_min)
    working_time += (hour_time + min_time)
    
print(working_time)
