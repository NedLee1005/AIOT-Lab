from gpiozero import LED
from requests import get ##import requests 中的get方法
import json ## 匯入json Library
import time
Firebase_URL = 'https://raspberry-pi-01-27424.firebaseio.com/.json'
## 新增一個存放剛剛的firebase 的連結
led17 = LED(17)
led22 = LED(22) ##設定led變數
led27 = LED(27)
led10 = LED(5)
led09 = LED(6)
led11 = LED(13) 
led17.off()
led22.off() ##在開始執行程式前先將LED全部關閉
led27.off()
led10.off()
led09.off()
led11.off()
while True:
    LedData = get(Firebase_URL).json()['LED']
## 宣告ledData，並讓它用get 方式去讀取Firebase的網址，並轉成json 格式，
取得資料庫裡led 欄位底下的資料。
led17onoff = LedData['LED_R'] ## 讀取led17的狀態
led22onoff = LedData['LED_G'] ## 讀取led22的狀態
led27onoff = LedData['LED_B'] ## 讀取led27的狀態
led09onoff = LedData['LED-2-R']
led10onoff = LedData['LED-2-G']
led11onoff = LedData['LED-2-B']
Flash=LedData['Flashing']
led17.value = led17onoff
led22.value = led22onoff
led27.value = led27onoff
led09.value = led09onoff
led10.value = led10onoff
led11.value = led11onoff
if flash == 1:
    count=0
    for count in range(0,8):
        if count%2==0:
            led17.value=0
            led10.value=0
        else:
            led17.value=1
            led10.value=1
        if count<4:
            led22.value=0
            led09.value=0
        else:
            led22.value=1
	    led09.value=1
	    if count==0 or count==1 or count==4 or count==5:
	        led27.value=0
		led11.value=0
            else:
	        led27.value=1
		led11.value=1
	    time.sleep(.300)
