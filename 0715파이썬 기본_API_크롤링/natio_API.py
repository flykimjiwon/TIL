# 요청 보내주는 requests 를 가져온다.

import requests

# 1.url로 요청을 보낸 결과를 저장한다.
url = 'https://api.nationalize.io?name=michael'


# 저장하는데 이거 json, 리스트-딕셔너리로 바꿔줘

response = requests.get(url).json()
#print(response)
#print(type(response))
#print(response['age'])

print('--------------------------------')

#어느 나라인지, 가장확률높은거 출력
country = response['country']
#print(country)
#print(country[0])
#print(type(country[0]))
#print(country[0]['probability'])
#print(country[0]('probability'))
ratio = 0
ct =''
#for i in country:
 #   if [country('probability')] >ratio:

for i in country:
    if i['probability'] > ratio:
        ratio = i['probability']
        ct = i['country_id']

print('가장높은확률의나라는',ct, ratio)

