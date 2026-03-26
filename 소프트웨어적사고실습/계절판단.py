import datetime
now = datetime.datetime.now()

if 3 <= now.month <=5: print(f"이번 달은 {now.month}월로, 봄입니다.")
elif 6 <= now.month <=8: print(f"이번 달은 {now.month}월로, 여름입니다.")
elif 9 <= now.month <=11: print(f"이번 달은 {now.month}월로, 가을입니다.")
else: print(f"이번 달은 {now.month}월로, 겨울입니다.")