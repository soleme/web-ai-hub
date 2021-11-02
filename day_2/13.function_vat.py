# 함수는 서로 연관된 코드를 그룹핑해서, 이름을 붙인다.

def get_vat(가격):
    # 가격 = 1000
    부가가치세율 = 0.1
    return 가격*부가가치세율

# get_vat(10000)
# get_vat(20000)
# get_vat(100)

# get_vat(float(input('얼마요?')))

print(get_vat(10000))