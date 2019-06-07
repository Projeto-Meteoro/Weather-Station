import time
from Adafruit_BME280 import *

bme = BME280(t_mode=BME280_OSAMPLE_8)

while True:
    T = bme.read_temperature()
    P = bme.read_pressure()
    print("Temperature : ", round(T), "C")
    print("Pressure : ", P, "hPa")  
    time.sleep(1)