import Adafruit_DHT as dht
import lcddriver
import time

sensor = dht.DHT11
lcd=lcddriver.lcd()

try:
    while True:
        h,t = dht.read_retry(sensor,4)
        lcd.lcd_display_string("T="+str(t),1)
        lcd.lcd_display_string("H="+str(h),2)
        time.sleep(3)
        lcd.lcd_clear()
except:
    print("Fin de Programa")