import requests

#testcode
# url = 'http://apis.data.go.kr/B552584/ArpltnStatsSvc/getMsrstnAcctoRDyrg'
# api_key = 'QJRybMDa268ppzvorK%2FVc7f2gt2Jmm6X8NOQE5dBL%2BGhTeoHE5DiyptwxOMFt5h0D52gSysgWOjJHRrgmhdqNw%3D%3D'
# api_key = requests.utils.unquote(api_key)
# params ={'serviceKey' : api_key, 'returnType' : 'xml', 'numOfRows' : '100', 'pageNo' : '1', 'inqBginDt' : '20201001', 'inqEndDt' : '20201030', 'msrstnName' : '강남구' }
# response = requests.get(url, params=params)
# print(response.content)
# print(response.cookies)
# print(response.headers)

#getCtprvnMesureList #9
# url = 'http://apis.data.go.kr/B552584/ArpltnStatsSvc/getCtprvnMesureLIst'
# api_key = 'QJRybMDa268ppzvorK%2FVc7f2gt2Jmm6X8NOQE5dBL%2BGhTeoHE5DiyptwxOMFt5h0D52gSysgWOjJHRrgmhdqNw%3D%3D'
# api_key = requests.utils.unquote(api_key)
# params = {'serviceKey' : api_key, 'returnType' : 'json', 'numOfRows' : '100', 'pageNo' : '1', 'dataGubun':'HOUR','itemCode' : 'PM10'}
# response = requests.get(url, params=params)
# print(response)
# print(response.content)


#getCtprvnMesureList #12
# url = 'http://apis.data.go.kr/B552584/ArpltnStatsSvc/getCtprvnMesureSidoLIst'
# api_key = 'QJRybMDa268ppzvorK%2FVc7f2gt2Jmm6X8NOQE5dBL%2BGhTeoHE5DiyptwxOMFt5h0D52gSysgWOjJHRrgmhdqNw%3D%3D'
# api_key = requests.utils.unquote(api_key)
# #params = {'serviceKey' : api_key, 'returnType' : 'xml', 'numOfRows':'100', 'pageNo':'1', 'searchCondition':'DAILY', 'sidoName':'서울'}
# params = {'serviceKey' : api_key, 'searchCondition':'DAILY', 'sidoName':'서울'}
# # params = {'serviceKey' : api_key,  'sidoName':'서울', 'searchCondition':'DAILY'}
# response = requests.get(url, params=params)
# print(response)
# print(response.content)
# print(len(response.content))



#이거는 문제가 좀 있는듯 ? totalCount가 안잡힘 
#getMsrstnAcctoRDyrg #15 
# url = 'http://apis.data.go.kr/B552584/ArpltnStatsSvc/getMsrstnAcctoRDyrg'
# api_key = 'QJRybMDa268ppzvorK%2FVc7f2gt2Jmm6X8NOQE5dBL%2BGhTeoHE5DiyptwxOMFt5h0D52gSysgWOjJHRrgmhdqNw%3D%3D'
# api_key = requests.utils.unquote(api_key)
# # params = {'serviceKey' : api_key, 'returnType':'json', 'numOfRows':'100','pageNo':'1','msrstnName':'측정소명','inqEndDt':'20201030','inqBginDt':'20201001'}
# params = {'serviceKey' : api_key,'inqBginDt':'20201001','inqEndDt':'20201030'}
# response = requests.get(url, params=params)
# print(response)
# print(response.content)


# 얘도 문제가 좀 있는듯. totalCount가 안잡힘
# getMsrstnAcctoRMmrg #18
# url = 'http://apis.data.go.kr/B552584/ArpltnStatsSvc/getMsrstnAcctoRMmrg'
# api_key = 'QJRybMDa268ppzvorK%2FVc7f2gt2Jmm6X8NOQE5dBL%2BGhTeoHE5DiyptwxOMFt5h0D52gSysgWOjJHRrgmhdqNw%3D%3D'
# api_key = requests.utils.unquote(api_key)
# # params = {'serviceKey' :api_key, 'inqBginMm':'202007','inqEndMm':'202010', 'msrstnName':'종로구'}
# params = {'serviceKey' :api_key, 'inqBginMm':'202007','inqEndMm':'202010'}
# # params = {'serviceK1ey' : api_key, 'returnType' : 'json', 'numOfRows' : '100', 'pageNo' : '1', 'dataGubun':'HOUR','itemCode' : 'PM10'}
# response = requests.get(url, params=params)
# print(response)
# print(response.content)