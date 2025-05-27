## 7016 버스의 상명대정문 정류장 도착 정보 조회 ##
import requests
import json
from pandas import json_normalize
import pandas as pd

key = "znh5jtdin0nQnFc7MCaf8Mu8dub1ENyXFVN0rnb1l4tvGr3NYkTiGpug4hFEqNPnHIikiDIrtleFmiI%2BJh%2B7xg%3D%3D"
bus_stop_id = "100000180"	# 상명대정문 정류장
bus_id = "100100447"		# 7016 버스
ord_number = '55'		# 7016 버스 순번

url = f'http://ws.bus.go.kr/api/rest/arrive/getLowArrInfoByRoute?ServiceKey={key}&stId={bus_stop_id}&busRouteId={bus_id}&ord={ord_number}&resultType=json'

response = requests.get(url)
if response.status_code == 200:
	json_ob = json.loads(response.text)
	data = json_ob['msgBody']['itemList']
	df = json_normalize(data)
	print(f"1번째 버스 현재 위치: {df['stationNm1'].iloc[0]}, 남은 시간: {df['arrmsg1'].iloc[0]}")
	print(f"2번째 버스 현재 위치: {df['stationNm2'].iloc[0]}, 남은 시간: {df['arrmsg2'].iloc[0]}")