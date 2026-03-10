import spidev
import time
import requests

firebase_url = "https://smart-farm-app-2026-default-rtdb.asia-southeast1.firebasedatabase.app/sensor_data.json"

spi = spidev.SpiDev()
spi.open(0,0)

def read_channel(channel):
    adc = spi.xfer2([1,(8+channel)<<4,0])
    data = ((adc[1]&3)<<8)+adc[2]
    return data

while True:
    moisture = read_channel(0)

    print("Soil Moisture:", moisture)

    data = {"moisture": moisture}

    requests.put(firebase_url, json=data)

    time.sleep(10)
