money = input('금액을 입력하세요:')
ret1 = money.split(' ')
ret2 = ret1[1]
if ret2 == '달러':
    i = int(ret1[0]) * 1112
    print(f"{i:,}원")
else:
    j = int(ret1[0]) * 171
    print(f"{j:,}원")