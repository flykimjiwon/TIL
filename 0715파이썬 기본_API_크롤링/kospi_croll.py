# 0.requests 패키지를 가져온다
import requests
from bs4 import BeautifulSoup


# 1.url을 준비한다.
url = 'https://finance.naver.com/sise/'

# 2. 파이썬으로 보낸 결과를저장

reponse = requests.get(url).text
#rint(reponse)

#텍스트에서 정보를 추출
# 3.정보추출을 위해서, BeautifulSoup으로 문서 구조화
data = BeautifulSoup(reponse,'html.parser') # html구조로 바꾸기 parser
# 4. 선택자를 활용해서 해당 위치를 찾고
kospi = data.select_one('#KOSPI_now')
# 5. 내용을 출력한다.
print('----------------------')
print(kospi)