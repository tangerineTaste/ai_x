import datetime
now = datetime.datetime.now().timestamp() # 현재의 유닉스 시간(70.01.01부터 현재까지 초)
print(now)
now_datetime = datetime.datetime.fromtimestamp(now)
print(now_datetime)
print(now_datetime.strftime('%Y-%m-%d %H:%M:%S'))
