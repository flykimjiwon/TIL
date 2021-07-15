# 0.requests 패키지를 가져온다
import requests
from bs4 import BeautifulSoup


# 1.url을 준비한다.
url = 'https://www.upbit.com/exchange?code=CRIX.UPBIT.KRW-AXS'

# 2. 파이썬으로 보낸 결과를저장

reponse = requests.get(url).text
#rint(reponse)

#텍스트에서 정보를 추출
# 3.정보추출을 위해서, BeautifulSoup으로 문서 구조화
data = BeautifulSoup(reponse,'html.parser') # html구조로 바꾸기 parser
# 4. 선택자를 활용해서 해당 위치를 찾고

axs = data.select_one('#UpbitLayout > div:nth-child(4) > div > section.ty02 > article > span.tabB > div > div > div:nth-child(1) > table > tbody > tr.up.on > td.price > strong')
milk = data.select_one('#UpbitLayout > div:nth-child(4) > div > section.ty02 > article > span.tabB > div > div > div:nth-child(1) > table > tbody > tr.up.on > td.price > strong')
# 5. 내용을 출력한다.
print('엑시인피니티가격')
print(axs)

print('밀크코인가격')
print(milk)