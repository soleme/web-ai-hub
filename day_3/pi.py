radius = int(input('원의 반지름을 입력하시오 : '))
area = 3.14 * radius * radius
# area = 3.14 * radius ** 2 제곱연산자(**)
circum = 3.14 * radius * 2

# 소수점 2째자리
print('반지름 %.2f 의 면적은 = %.2f' %(radius,area))
print('반지름 %.2f 의 둘레는 = %.2f' %(radius,circum))
