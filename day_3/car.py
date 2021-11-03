# 차량 2부제 프로그램
#input('차량 번호 4자리를 입력하세요 :')

from datetime import date, datetime

carNum = int(input('차량번호 : '))
dayNum = datetime.today().day
print('오늘 날짜 : %d일' %dayNum)
if dayNum % 2 == 0:
    print("오늘 입차 : 번호가 짝수인 차량")    
else:
    print("오늘 입차 : 번호가 홀수인 차량")

if dayNum % 2 == carNum % 2:
    print("귀하의 차량은 입차 가능합니다.")
else:
    print("귀하의 차량은 입차 불가합니다.")