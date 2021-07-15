# 요청 보내주는 requests 를 가져온다.

import requests

# 1.url로 요청을 보낸 결과를 저장한다.
url = 'https://api.agify.io/?name=kimjiwon'
url_name = 'https://api.agify.io/?name='

# 저장하는데 이거 json, 리스트-딕셔너리로 바꿔줘

#response = requests.get(url_name).json()
#print(response)
#print(type(response))
#print(response['age'])

# 저장하는데 text로 바꿔줘, ->beautifulSoup 구조화
#html -> 선택자

#response_text = requests.get(url).text
#print(response_text)
#print(type(response_text))


print('--------------------------------')
# tak, tony, eric, musk 나이 확인코드

name = ['tak','tony','eric','musk']
print('나이출력')

for i in name:
    response = requests.get(url_name+i).json()
    print(i,'의 나이는',response['age'])

