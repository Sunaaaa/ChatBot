'''
    requests를 통해 동행복권 API 요청을 보내,
    1등 번호를 가져와 python list로 만듬
'''

import requests 

# 1. request를 통해 요청 보내기
# requests.get('주소')
url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=873'

# 응답으로 받은 결과물을 response 변수에 담는다. 
response = requests.get(url)
# print(response)
# response 안의 내용물 
# print(response.text)

res_dict = response.json()
print(res_dict)
print(res_dict['drwtNo1'])

# 1등 번호 6개가 담긴 result라는 list를 출력
result = [res_dict['drwtNo'+ str(val)] for val in range(1,7)]
print(result)