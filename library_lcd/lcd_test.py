#example for lcd_i2c
import RPi_I2C_driver
from time import *

mylcd = RPi_I2C_driver.lcd()

#test1
mylcd.lcd_clear()
mylcd.lcd_display_string("HOLA MUNDO",1)
mylcd.lcd_display_string("   test",2)

sleep(5)

mylcd.lcd_clear()
mylcd.lcd_display_string_pos("Testing",1,2)

