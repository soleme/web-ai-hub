# 로또 번호 만들기
import random
lotto = []
while len(lotto) < 6: # 6개까지...
    for i in range(6):
        num = random.randint(1, 45)
        if num not in lotto: #중복체크
            lotto.append(num)
print(lotto)