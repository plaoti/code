n = int(input("오늘이 일요일이면 n일 후는 무슨 요일일까요. n을 입력해 주세요. :"))
nam = n % 7
if(nam == 0): print("일요일")
if(nam == 1): print("월요일")
if(nam == 2): print("화요일")
if(nam == 3): print("수요일")
if(nam == 4): print("목요일")
if(nam == 5): print("금요일")
