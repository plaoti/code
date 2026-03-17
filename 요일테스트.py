n = int(input("오늘이 일요일일 때, 며칠 후가 무슨 요일인지 궁금한가요. 정수입력"))
moak = n % 7
if(moak == 0):
    print("일요일")
if(moak == 1):
    print("월요일")
if(moak == 2):
    print("화요일")
if(moak == 3):
    print("수요일")
if(moak == 4):
    print("목요일")
if(moak == 5):
    print("금요일")
if(moak == 6):
    print("토요일")
