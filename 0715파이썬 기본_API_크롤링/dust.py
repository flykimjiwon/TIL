#dust 라는 변수에 100을 넣고

# dust 가 80보다 크면, 나쁨

# 31~80, 보통

# ~30, 좋음

dust = 100

if dust >80:
    print('나쁨')
elif dust >=31 and dust <=80:
    print('보통')
else:
    print('좋음')