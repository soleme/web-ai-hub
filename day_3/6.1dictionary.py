# 회원 가입 프로그램 (딕셔너리)

members = {}

for i in range(2):
    id = input('아이디 입력 : ')
    pw = input('비밀번호 입력 : ')
    members[id] = pw

for key in members:
    print(key + " : " + members[key])    