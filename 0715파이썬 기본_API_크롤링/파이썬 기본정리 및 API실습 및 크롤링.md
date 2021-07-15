# 파이썬 기본정리 및 API실습 및 크롤링



- 파이썬 기본

  ```
  dust.py, hello.py, lotto.py,phone.py
  ```

  

- 파이썬 크롤링 `kospi_croll.py` `money_croll.py`

  코스피지수, 환율 크롤링

  ```
  pip install requests 한다음
  
  import requests
  from bs4 import BeautifulSoup <-이거중요 pip install bs4도해주기
  
  url저장한다음
  requests.get(url).text형태로저장
  크롬에서 검사로들어가 copy selector이용
  ```

  

- 파이썬 API실습 `age_API.py` `natio_API.py`

  ```
  import requests 해준다음
  
  url저장후
  
  requests.get(url).json() 형태로 가져온다.
  
  그다음 사용하기!
  ```

  



