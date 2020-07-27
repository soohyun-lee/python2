import random
n = random.randrange(1,101)
print('랜덤숫자:', n)
count = 0
while 1:
    x = int(input('숫자를 입력하세요'))
    if x > n:
        print('입력한 숫자는 랜덤 숫자보다 큽니다')
    if x < n:
        print('입력한 숫자는 랜덤 숫자보다 작습니다')
    if x == n:
        break
count += 1
print('정답. 입력한 횟수는 %s입니다' %count)