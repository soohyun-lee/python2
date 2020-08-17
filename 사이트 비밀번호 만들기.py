# 예) [http://naver.com](http://naver.com) 의  비밀 번호는 →nav51!
# - 규칙1: http:// 부분제거 → naver.com
# - 규칙2: 처음 만나는 점(.) 이후 부분 제거 → naver
# - 규칙3: 남은 글자 중 처음 3글자(nev) + 글자수(5) +글자 내 'e'의 갯수(1) + '!'
def website(x):
    b = x.strip('https://')
    for i in range(len(b)):
        if b[i] == '.':
            n = b[0:i]
            k = [n[:3],str(len(n)),str(n.count('e')),'!']
            return ''.join(k)

a = website(input('사이트 주소:'))
print(a)