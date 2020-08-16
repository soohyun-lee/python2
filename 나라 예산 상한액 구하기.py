
# 1. 예산 나누기 나라 갯수 == > 1개 나라 당 최대 배정액 정하기
# 2. 최대 배정액 보다 낮은 금액을 요청한 나라는 요청한 금액 그대로 배정
# 3. 최대 배정액 보다 높은 금액을 요청한 나라는 최대 배정액으로 자르기
# 4. 2,3에서 배정된 예산 총 합이 최대 예산보다 적으면 3번 나라들 배정액에서 1씩 더해가기
# j = 상한액
M = int(input('예산 입력:'))
x = [int(x) for x in input('각 나라 예산:').split()]
# x = [10, 180, 150, 80]
j = M // len(x)
new = []
for i in x:
    if i < j:
        new.append(i)
    else:
        new.append(j)
print(new)

# while sum(new) == M:
while sum(new) <= M:
    for i in range(len(new)):
        if new[i] >= j:
            new[i] += 1

print(new)