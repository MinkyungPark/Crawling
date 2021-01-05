# # for문 정리
# for 변수 in list(or tuple, str):
#     수행할 문장

test_list = ['one', 'two', 'three']
for i in test_list:
    print(i) # i에 test_list요소 하나씩 대입

print('------------------------------------------')
marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number = number +1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)

marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (number+1))

print('------------------------------------------')
a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)
# result
# 3
# 7
# 11

print('------------------------------------------')
marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number = number +1
    if mark < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다. " % number)

# while문에서 살펴본 continue문을 for문에서도 사용할 수 있다.
# 즉 for문 안의 문장을 수행하는 도중에 continue문을 만나면 for문의 처음으로 돌아가게 된다.

print('------------------------------------------')
# range 숫자 리스트를 자동으로 만들어주는 함수. a = range(1, 11) 끝 숫자는 포함X