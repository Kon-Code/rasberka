from ssd1306 import SSD1306_I2C
from machine import Pin, I2C
from utime
WIDTH=128
HEIGHT=32
# konfigurujemy oled
oled=SSD1306_I2C(WIDTH,HEIGHT,i2c) 
#konfigurujemy piny na oled
I2C= I2C(0,scl=Pin(5), sda=Pin(4), freq=20000)
while True:
    reading1= adc.read(Pin(A1))
    reading2= adc.read(Pin(A2))
#przeliczamy wartości z aproksymacji
temp1=  (-0,6218*reading1 + 27,001)
temp2= (-0,6218*reading2 + 27,001)
#czysicimy niepotrzebne znaki
oled.fill(0) 
oled.invert(True)
oled.text("temperatura pierwszego układu: "+ temp1,5,8)
oled.text("temperatura drugiego układu: "+ temp2,5,18)     
oled.show();
utime.slepp(0.1)
          


