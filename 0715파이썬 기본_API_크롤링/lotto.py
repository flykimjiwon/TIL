#로또 번호 6개 추첨하는 코드 작성하기

#코드실행은 python 파일명.py

#1. random 모듈을가져오고
import random

#2.number 통을만들고

numbers = range(1,46)

#3. 랜덤ㄹrandom에서 sample() 샘플 6개추출해 ,pcik에 저장하고

pick = random.sample(numbers,6)
pick.sort()
#4.pick출력
print(pick)