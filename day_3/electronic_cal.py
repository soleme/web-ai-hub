# 전기 요금 계산기
amount = int(input('전기 사용량을 입력하세요. '))

if amount > 400:
    unitPrice = 280.6
    basicPrice = 7300
elif amount >200:
    unitPrice = 187.9
    basicPrice = 1600
else:
    unitPrice = 99.3
    basicPrice = 910

totalPrice = amount * unitPrice + basicPrice

print('사용량 : %.1f' %(amount) + 'kwh')
print('기본요금 : %.d' %(basicPrice) + '원')
print('단가 : %.1f' %(unitPrice) + '원')
print('전기 요금 : %.1f' %(totalPrice) + '원')