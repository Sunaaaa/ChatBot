# 실시간 BTC (Bitcoin) 현재가를 출력하는 crypto.py
import requests 

# 1. request를 통해 요청 보내기
# requests.get('주소')
url = 'https://api.bithumb.com/public/ticker/'

# 응답으로 받은 결과물을 response 변수에 담는다. 
response = requests.get(url)
# print(response)
# response 안의 내용물 
# print(response.text)

res_dict = response.json()
# print(res_dict)
print(res_dict['data']['opening_price'])

# # 1등 번호 6개가 담긴 result라는 list를 출력
# result = [res_dict['drwtNo'+ str(val)] for val in range(1,7)]
# print(result)