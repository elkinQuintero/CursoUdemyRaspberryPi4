import lcddriver
import time
lcd = lcddriver.lcd()
texto = ""
maximo = 12
while maximo>0:
    lcd.lcd_display_string(texto+"Hola",2)
    time.sleep(1)
    texto=texto+" "
    lcd.lcd_clear()
    maximo=maximo-1
print("fin de programa")