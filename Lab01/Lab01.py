from gpiozero import LED
from requests import get
import json
import time

Firebase_URL = 'https://lab01-ee469-default-rtdb.firebaseio.com/.json'

led17 = LED(17)
led22 = LED(22)
led27 = LED(27)
led10 = LED(5)
led09 = LED(6)
led11 = LED(13)

led17.off()
led22.off()
led27.off()
led10.off()
led09.off()
led11.off()

while True:
    response = get(Firebase_URL)  # Get the response from Firebase
    print(response.json())  # Debugging: print the full response to inspect the structure
    
    LedData = response.json().get('LED', {})  # Get the 'LED' data, or empty dictionary if not found
    
    if LedData:  # If the 'LED' data is found, process it
        led17onoff = LedData.get('LED_R', 0)
        led22onoff = LedData.get('LED_G', 0)
        led27onoff = LedData.get('LED_B', 0)
        led09onoff = LedData.get('LED-2-R', 0)
        led10onoff = LedData.get('LED-2-G', 0)
        led11onoff = LedData.get('LED-2-B', 0)
        Flash = LedData.get('Flashing', 0)

        led17.value = led17onoff
        led22.value = led22onoff
        led27.value = led27onoff
        led09.value = led09onoff
        led10.value = led10onoff
        led11.value = led11onoff

        if Flash == 1:
            count = 0
            for count in range(0, 8):
                if count % 2 == 0:
                    led17.value = 0
                    led10.value = 0
                else:
                    led17.value = 1
                    led10.value = 1

                if count < 4:
                    led22.value = 0
                    led09.value = 0
                else:
                    led22.value = 1
                    led09.value = 1

                if count == 0 or count == 1 or count == 4 or count == 5:
                    led27.value = 0
                    led11.value = 0
                else:
                    led27.value = 1
                    led11.value = 1

                time.sleep(0.300)
    else:
        print("No LED data found in Firebase response")
        time.sleep(1)
