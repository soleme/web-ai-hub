# members = [
#     ['egoing','Seoul','Web'],
#     ['leezhe','Jeju','Design']
# ]
# print(members[0][1])

# for member in members:
#     # print(member)
#     print(member[0], member[1], member[2])

# 리스트는 순서가 있는 데이터를 담는다.
# 그리고, 색인을 통해서 식별한다.

# 딕셔너리는 순서가 없는 데이터를 담는다.
# 그리고, 이름을 통해서 식별한다.

members = [
            {'name':'egoing', 'city':'Seoul', 'job':'Web'},
            {'name':'leezche', 'city':'Jeju', 'job':'Design'}
         ]
# print(member['name'])
# print(member['city'])

for member in members:
    print(member['name'], member['city'], member['job'])