# 출석부 관리 시스템

students = ["정우람", "박으뜸", "배힘찬", "천영웅", "신석기", "배민규", "전민수", "박건우", "박찬호", "이승엽"]

# sorted는 보여지는것만 sort할뿐 students의 내용을 sort하지 않음
# sorted(students)
# print(sorted(students))
# print(students)

# 정렬
students.sort()
print(students)

# 삭제
students.remove('박찬호')
print(students)

# 앞에 3명만 보여주기
students[0:3] # students[:3] (0을 생략해도 된다.)
print(students[0:3])

# 이병규 전학
students.append('이병규')
print(students)

# 학생순서를 역순
students.reverse()
print(students)

# 정우람을 정잘남으로 개명
# students[students.index('정우람')] = '정잘남'
idx = students.index('정우람')
students[idx] = '정잘남'
print(students)
