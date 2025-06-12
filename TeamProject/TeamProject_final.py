## 필요한 모듈 import ##
from tkinter import *
import requests
import json
from pandas import json_normalize
import pandas as pd
import tkinter as tk



## 버스 도착 정보 조회 함수들 ##
# 7016 버스
def bus_7016(): 
    key = "znh5jtdin0nQnFc7MCaf8Mu8dub1ENyXFVN0rnb1l4tvGr3NYkTiGpug4hFEqNPnHIikiDIrtleFmiI%2BJh%2B7xg%3D%3D"
    bus_stop_id = "100000180"   # 상명대정문 정류장
    bus_id = "100100447"      # 7016 버스
    ord_number = '55'      # 7016 버스 순번

    url = f'http://ws.bus.go.kr/api/rest/arrive/getLowArrInfoByRoute?ServiceKey={key}&stId={bus_stop_id}&busRouteId={bus_id}&ord={ord_number}&resultType=json'

    response = requests.get(url)
    if response.status_code == 200:
        json_ob = json.loads(response.text)
        data = json_ob['msgBody']['itemList']
        df = json_normalize(data)
        new_window = tk.Toplevel()
        label1 = Label(new_window, text = f"1번째 버스 현재 위치: {df['stationNm1'].iloc[0]}, 남은 시간: {df['arrmsg1'].iloc[0]}" )
        label2 = Label(new_window, text = f"2째 버스 현재 위치: {df['stationNm2'].iloc[0]}, 남은 시간: {df['arrmsg2'].iloc[0]}" )
        label1.pack()
        label2.pack()



# 서대문08 
def bus_08(): 
    key = "znh5jtdin0nQnFc7MCaf8Mu8dub1ENyXFVN0rnb1l4tvGr3NYkTiGpug4hFEqNPnHIikiDIrtleFmiI%2BJh%2B7xg%3D%3D"
    bus_stop_id = "100000180"   # 상명대정문 정류장
    bus_id = "100900012"      # 서대문08 버스
    ord_number = '1'      # 서대문08 버스 순번

    url = f'http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRoute?ServiceKey={key}&stId={bus_stop_id}&busRouteId={bus_id}&ord={ord_number}&resultType=json'

    response = requests.get(url)
    if response.status_code == 200:
        json_ob = json.loads(response.text)
        data = json_ob['msgBody']['itemList']
        df = json_normalize(data)
        new_window = tk.Toplevel()
        label1 = Label(new_window, text = f"1번째 버스 현재 위치: {df['stationNm1'].iloc[0]}, 남은 시간: {df['arrmsg1'].iloc[0]}" )
        label2 = Label(new_window, text = f"2째 버스 현재 위치: {df['stationNm2'].iloc[0]}, 남은 시간: {df['arrmsg2'].iloc[0]}" )
        label1.pack()
        label2.pack()

# 종로13
def bus_13(): 
    key = "znh5jtdin0nQnFc7MCaf8Mu8dub1ENyXFVN0rnb1l4tvGr3NYkTiGpug4hFEqNPnHIikiDIrtleFmiI%2BJh%2B7xg%3D%3D"
    bus_stop_id = "100000180"   # 상명대정문 정류장
    bus_id = "100900002"      # 종로13 버스
    ord_number = '16'      # 종로13 버스 순번

    url = f'http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRoute?ServiceKey={key}&stId={bus_stop_id}&busRouteId={bus_id}&ord={ord_number}&resultType=json'

    response = requests.get(url)
    if response.status_code == 200:
        json_ob = json.loads(response.text)
        data = json_ob['msgBody']['itemList']
        df = json_normalize(data)
        new_window = tk.Toplevel()
        label1 = Label(new_window, text = f"1번째 버스 현재 위치: {df['stationNm1'].iloc[0]}, 남은 시간: {df['arrmsg1'].iloc[0]}" )
        label2 = Label(new_window, text = f"2째 버스 현재 위치: {df['stationNm2'].iloc[0]}, 남은 시간: {df['arrmsg2'].iloc[0]}" )
        label1.pack()
        label2.pack()

# 7022 세검정교회
def bus_7022a(): 
    key = "znh5jtdin0nQnFc7MCaf8Mu8dub1ENyXFVN0rnb1l4tvGr3NYkTiGpug4hFEqNPnHIikiDIrtleFmiI%2BJh%2B7xg%3D%3D"
    bus_stop_id = "100000047"   # 상명대입구 정류장
    bus_id = "100100341"      # 7022 버스
    ord_number = '52'      # 7022 버스 순번

    url = f'http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRoute?ServiceKey={key}&stId={bus_stop_id}&busRouteId={bus_id}&ord={ord_number}&resultType=json'

    response = requests.get(url)
    if response.status_code == 200:
        json_ob = json.loads(response.text)
        data = json_ob['msgBody']['itemList']
        df = json_normalize(data)
        new_window = tk.Toplevel()
        label1 = Label(new_window, text = f"1번째 버스 현재 위치: {df['stationNm1'].iloc[0]}, 남은 시간: {df['arrmsg1'].iloc[0]}" )
        label2 = Label(new_window, text = f"2째 버스 현재 위치: {df['stationNm2'].iloc[0]}, 남은 시간: {df['arrmsg2'].iloc[0]}" )
        label1.pack()
        label2.pack()

# 7022 석파랑
def bus_7022b(): 
    key = "znh5jtdin0nQnFc7MCaf8Mu8dub1ENyXFVN0rnb1l4tvGr3NYkTiGpug4hFEqNPnHIikiDIrtleFmiI%2BJh%2B7xg%3D%3D"
    bus_stop_id = "100000189"   # 상명대입구 정류장
    bus_id = "100100341"      # 7022 버스
    ord_number = '23'      # 7022 버스 순번

    url = f'http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRoute?ServiceKey={key}&stId={bus_stop_id}&busRouteId={bus_id}&ord={ord_number}&resultType=json'

    response = requests.get(url)
    if response.status_code == 200:
        json_ob = json.loads(response.text)
        data = json_ob['msgBody']['itemList']
        df = json_normalize(data)
        new_window = tk.Toplevel()
        label1 = Label(new_window, text = f"1번째 버스 현재 위치: {df['stationNm1'].iloc[0]}, 남은 시간: {df['arrmsg1'].iloc[0]}" )
        label2 = Label(new_window, text = f"2째 버스 현재 위치: {df['stationNm2'].iloc[0]}, 남은 시간: {df['arrmsg2'].iloc[0]}" )
        label1.pack()
        label2.pack()

# 110B 국민대
def bus_110b(): 
    key = "znh5jtdin0nQnFc7MCaf8Mu8dub1ENyXFVN0rnb1l4tvGr3NYkTiGpug4hFEqNPnHIikiDIrtleFmiI%2BJh%2B7xg%3D%3D"
    bus_stop_id = "100000039"   # 세검정.상명대 정류장
    bus_id = "100100015"      # 110B 버스
    ord_number = '18'      # 110B 버스 순번

    url = f'http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRoute?ServiceKey={key}&stId={bus_stop_id}&busRouteId={bus_id}&ord={ord_number}&resultType=json'

    response = requests.get(url)
    if response.status_code == 200:
        json_ob = json.loads(response.text)
        data = json_ob['msgBody']['itemList']
        df = json_normalize(data)
        new_window = tk.Toplevel()
        label1 = Label(new_window, text = f"1번째 버스 현재 위치: {df['stationNm1'].iloc[0]}, 남은 시간: {df['arrmsg1'].iloc[0]}" )
        label2 = Label(new_window, text = f"2째 버스 현재 위치: {df['stationNm2'].iloc[0]}, 남은 시간: {df['arrmsg2'].iloc[0]}" )
        label1.pack()
        label2.pack()
        
# 7212 세검정교회
def bus_7212a(): 
    key = "znh5jtdin0nQnFc7MCaf8Mu8dub1ENyXFVN0rnb1l4tvGr3NYkTiGpug4hFEqNPnHIikiDIrtleFmiI%2BJh%2B7xg%3D%3D"
    bus_stop_id = "100000047"   # 세검정교회 정류장
    bus_id = "100100341"      # 7212 버스
    ord_number = '52'      # 7212 버스 순번

    url = f'http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRoute?ServiceKey={key}&stId={bus_stop_id}&busRouteId={bus_id}&ord={ord_number}&resultType=json'

    response = requests.get(url)
    if response.status_code == 200:
        json_ob = json.loads(response.text)
        data = json_ob['msgBody']['itemList']
        df = json_normalize(data)
        new_window = tk.Toplevel()
        label1 = Label(new_window, text = f"1번째 버스 현재 위치: {df['stationNm1'].iloc[0]}, 남은 시간: {df['arrmsg1'].iloc[0]}" )
        label2 = Label(new_window, text = f"2째 버스 현재 위치: {df['stationNm2'].iloc[0]}, 남은 시간: {df['arrmsg2'].iloc[0]}" )
        label1.pack()
        label2.pack()

# 7212 석파랑
def bus_7212b(): 
    key = "znh5jtdin0nQnFc7MCaf8Mu8dub1ENyXFVN0rnb1l4tvGr3NYkTiGpug4hFEqNPnHIikiDIrtleFmiI%2BJh%2B7xg%3D%3D"
    bus_stop_id = "100000189"   # 석파랑 정류장
    bus_id = "100100499"      # 7212 버스
    ord_number = '36'      # 7212 버스 순번

    url = f'http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRoute?ServiceKey={key}&stId={bus_stop_id}&busRouteId={bus_id}&ord={ord_number}&resultType=json'

    response = requests.get(url)
    if response.status_code == 200:
        json_ob = json.loads(response.text)
        data = json_ob['msgBody']['itemList']
        df = json_normalize(data)
        new_window = tk.Toplevel()
        label1 = Label(new_window, text = f"1번째 버스 현재 위치: {df['stationNm1'].iloc[0]}, 남은 시간: {df['arrmsg1'].iloc[0]}" )
        label2 = Label(new_window, text = f"2째 버스 현재 위치: {df['stationNm2'].iloc[0]}, 남은 시간: {df['arrmsg2'].iloc[0]}" )
        label1.pack()
        label2.pack()


# 163 흥지문 방면
def bus_163a(): 
    key = "znh5jtdin0nQnFc7MCaf8Mu8dub1ENyXFVN0rnb1l4tvGr3NYkTiGpug4hFEqNPnHIikiDIrtleFmiI%2BJh%2B7xg%3D%3D"
    bus_stop_id = "100000039"   # 세검정.상명대 정류장
    bus_id = "100100032"      # 163 버스
    ord_number = '32'      # 163 버스 순번

    url = f'http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRoute?ServiceKey={key}&stId={bus_stop_id}&busRouteId={bus_id}&ord={ord_number}&resultType=json'

    response = requests.get(url)
    if response.status_code == 200:
        json_ob = json.loads(response.text)
        data = json_ob['msgBody']['itemList']
        df = json_normalize(data)
        new_window = tk.Toplevel()
        label1 = Label(new_window, text = f"1번째 버스 현재 위치: {df['stationNm1'].iloc[0]}, 남은 시간: {df['arrmsg1'].iloc[0]}" )
        label2 = Label(new_window, text = f"2째 버스 현재 위치: {df['stationNm2'].iloc[0]}, 남은 시간: {df['arrmsg2'].iloc[0]}" )
        label1.pack()
        label2.pack()
        
        
# 163 세검초 방면
def bus_163b(): 
    key = "znh5jtdin0nQnFc7MCaf8Mu8dub1ENyXFVN0rnb1l4tvGr3NYkTiGpug4hFEqNPnHIikiDIrtleFmiI%2BJh%2B7xg%3D%3D"
    bus_stop_id = "100000048"   # 세검정.상명대 정류장
    bus_id = "100100032"      # 163 버스
    ord_number = '81'      # 163 버스 순번

    url = f'http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRoute?ServiceKey={key}&stId={bus_stop_id}&busRouteId={bus_id}&ord={ord_number}&resultType=json'

    response = requests.get(url)
    if response.status_code == 200:
        json_ob = json.loads(response.text)
        data = json_ob['msgBody']['itemList']
        df = json_normalize(data)
        new_window = tk.Toplevel()
        label1 = Label(new_window, text = f"1번째 버스 현재 위치: {df['stationNm1'].iloc[0]}, 남은 시간: {df['arrmsg1'].iloc[0]}" )
        label2 = Label(new_window, text = f"2째 버스 현재 위치: {df['stationNm2'].iloc[0]}, 남은 시간: {df['arrmsg2'].iloc[0]}" )
        label1.pack()
        label2.pack()



## 버튼 생성 및 함수 호출 ##
window = Tk()

label1 = Label(window,text="원하시는 버스를 선택해주세요.", font=("Helvetica",16,"bold"))

label2 = Label(window,text="----------[ 상명대정문 ]----------", font=("bold"), fg="navy")

button1 = Button(window,text=" 7016 ", command = bus_7016)
button2 = Button(window,text=" 서대문08 ", command = bus_08)
button3 = Button(window,text=" 종로13 ", command = bus_13)

label3 = Label(window,text="----------[ 상명대입구 ]----------", font=("bold"), fg="navy")

button4 = Button(window,text=" 7022 세검정교회 ", command = bus_7022a)
button5 = Button(window,text=" 7022 석파랑 ", command = bus_7022b)
button6 = Button(window,text=" 7212 세검정교회 ", command = bus_7212a)
button7 = Button(window,text=" 7212 석파랑 ", command = bus_7212b)
button8 = Button(window,text=" 163 홍지문 방면 ", command = bus_163a)
button9 = Button(window,text=" 163 세검초 방면 ", command = bus_163b)
button10 = Button(window,text=" 110B 국민대 ", command = bus_110b)



## 인터페이스 구성 ##
label1.pack()

label2.pack()
button1.pack()
button2.pack()
button3.pack()

label3.pack()
button4.pack()
button5.pack()
button6.pack()
button7.pack()
button8.pack()
button9.pack()
button10.pack()

window.mainloop()