#! /usr/bin/env python

import operator, serial, time
import datetime

LCD = serial.Serial('/dev/ttyAMA0', 9600) # LCD Netmedia serial 4x20 on GPIO

#LCD.write(chr(14)) # LCD reset
LCD.write(chr(20)) # LCD backlight
LCD.write(chr(200)) # LCD backlight value
LCD.write(chr(12)) # LCD clear screen

LCD.write("Weewx 3.8.2")
print "Weewx 3.8.2"
time.sleep(10)
LCD.write(chr(12)) # clear screen

while 1:
   try:
	  now = datetime.datetime.now()
  	f = open("/var/tmp/data.csv",'r')
  	data0 = f.readline() # header
  	data1 = f.readline() # dati
  	words = data1.split(',')
  	press = words[4]
  	pressure = float(press)
  	pressure = round(pressure*33.8639,1) # inHg to mbar
  	t_int = words[9]
  	temp_int = float(t_int)
  	temp_int = round((temp_int-32)*5/9,1) # F to C
  	hum = words[13]
  	t_ext = words[14]
  	temp_ext = float(t_ext)
  	temp_ext = round((temp_ext-32)*5/9,1) # F to C

  	print now,pressure, temp_int, temp_ext, hum

	  LCD.write(chr(17)) # cursor position
	  LCD.write(chr(0)) # riga
	  LCD.write(chr(0)) # colonna
  	LCD.write("Temp   = ")
  	LCD.write(str(temp_ext))
  	LCD.write(" C")
  	LCD.write(chr(17)) # cursor position
  	LCD.write(chr(1)) # riga
  	LCD.write(chr(0)) # colonna
  	LCD.write("Hum    = ")
  	LCD.write(hum)
  	LCD.write(" %")
    LCD.write(chr(17)) # cursor position
    LCD.write(chr(2)) # riga
    LCD.write(chr(0)) # colonna
    LCD.write("Press  = ")
  	LCD.write(str(pressure))
  	LCD.write(" mBar")
    LCD.write(chr(17)) # cursor position
    LCD.write(chr(3)) # riga
    LCD.write(chr(0)) # colonna
    LCD.write(now.strftime("%d-%b-%Y    %H:%M"))

  	time.sleep(30)
	  LCD.write(chr(12)) # cls

   finally:
	   f.close()
