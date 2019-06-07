from time import sleep
import requests
import board
import digitalio
import busio
import adafruit_bmp280


i2c = busio.I2C(board.SCL, board.SDA)
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)

def hpa_to_inches(pressure_in_hpa):
    pressure_in_inches_of_m = pressure_in_hpa * 0.02953
    return pressure_in_inches_of_m

def degc_to_degf(temperature_in_c):
    temperature_in_f = (temperature_in_c * (9/5.0)) + 32
    return temperature_in_f

# create a string to hold the first part of the URL
WUurl = "https://weatherstation.wunderground.com/weatherstation\
/updateweatherstation.php?"
WU_station_id = "ISOPAU7" # Replace XXXX with your PWS ID
WU_station_pwd = "VolT1o1o" # Replace YYYY with your Password
WUcreds = "ID=" + WU_station_id + "&PASSWORD="+ WU_station_pwd
date_str = "&dateutc=now"    
action_str = "&action=updateraw"

while True:
    
    T = bmp280.temperature
    P = bmp280.pressure
    pressure_str = "{0:.2f}".format(hpa_to_inches(P))
    ambient_temp_str = "{0:.2f}".format(degc_to_degf(T))

    r= requests.get(
        WUurl +
        WUcreds +
        date_str +
        "&baromin=" + pressure_str +
        "&tempf=" + ambient_temp_str +
        action_str)


    print("Received " + str(r.status_code) + " " + str(r.text))
    sleep(300)