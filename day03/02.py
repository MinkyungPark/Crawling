# json 파이썬 딕셔너리

json = {'name':'Minkyung', 'age':'27', 'where':'광진구', 'phone_number':'010-1234-1234',}

print(json)
print(json.keys()) # key값만 출력
print(json['name'])
print(json['age'])
print(json['where'])
print(json['phone_number'])

tmp = {'friends':[{'name':'sian', 'age':'28'},{'name':'nami','age':'31'},]}
json.update(tmp)

friends = json['friends']
print(friends)
for friend in friends:
    print(friend)
    print(friend['name'])
    print(friend['age'])

# json viewr  http://jsonviewer.stack.hu/
