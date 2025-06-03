from tkinter import *
import requests
import json
from pandas import json_normalize
import pandas as pd
import tkinter as tk





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




#버튼 생성 및 함수 호출
window = Tk()
button1 = Button(window,text="7016", command = bus_7016)
button2 = Button(window,text="seodae08", command = bus_08)
button3 = Button(window,text="jongro13", command = bus_13)


button1.pack()
button2.pack()
button3.pack()


window.mainloop()