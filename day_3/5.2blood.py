boolds = []

for i in range(10):
    print('\n헌혈해 주셔서 감사합니다. 헌혈하신 혈액형을 선택하세요')
    boolds.append(input('A, B, AB, O : '))

print('-' * 30)
print('혈액형 :', '개수')
print('-' * 30)
print('A형 :', boolds.count('A'))
print('B형 :', boolds.count('B'))
print('AB형 :', boolds.count('AB'))
print('O형 :', boolds.count('O'))
print('-' * 30)