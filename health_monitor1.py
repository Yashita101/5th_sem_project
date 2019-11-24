import spidev
import time
import os
from pulsesensor import Pulsesensor
import temperature
import RPi.GPIO as GPIO
import serial
import sys
import http.client
import urllib.request


health_monitor_key="JVOD9WXB1P4NJBRR"
#temp_key="VMPNSROP5WNJPZJ3"
#pulse_rate_key="OV4UT8JRYDWS5B53"
temp_pause=5
pulse_pause=3

SERIAL_PORT="/dev/ttyS0"

ser=serial.Serial(SERIAL_PORT,baudrate=9600,timeout=5)
p = Pulsesensor()
p.startAsyncBPM()
        
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1000000


def health_monitor():
    delay = 1

    while True:
        try:
            temp_level = ReadChannel(temp_channel)
            temp_volts = ConvertVolts(temp_level,2)
            temp       = ConvertTemp(temp_level,2)
            bpm = p.BPM
            
            params1=urllib.parse.urlencode({'field1':temp,'key':temp_key})
            headers1={"Content-typZZe":"application/x-www-form-urlencoded","Accept":"text/plain"}
            conn1=http.client.HTTPConnection("api.thingspeak.com:80")
            
            params2=urllib.parse.urlencode({'field2':bpm,'key':pulse_rate_key})
            headers2={"Content-typZZe":"application/x-www-form-urlencoded","Accept":"text/plain"}
            conn2=http.client.HTTPConnection("api.thingspeak.com:80")        

            conn1.request("POST","/update",params1,headers1)
            conn2.request("POST","/update",params2,headers2)
            response1=conn1.getresponse()
            response2=conn2.getresponse()
            if bpm > 0 and temp > 0:
                    time.sleep(10)
                    print ("--------------------------------------------"  )
                    print("BPM: %d" % bpm)
                    print("Temp  : {} ({}V) {} deg C".format(temp_level,temp_volts,temp))
                    if temp < 25:
                        low_temp=time.time()
                        time.sleep(1)
                        if (time.time()-low_temp)>temp_pause:
                            ser.write(str.encode("ATD+918970736699;\r"))
                            print("Dialling...low_temp")
                            time.sleep(10)
                            ser.write(str.encode("ATH\r"))
                            print("Hanging up")
                            time.sleep(30)
                        break
                    elif temp > 30:
                        high_temp=time.time()
                        time.sleep(1)
                        if (time.time()-high_temp)>temp_pause:
                            ser.write(str.encode("ATD+918970736699;\r"))
                            print("Dialling...high_temp")
                            time.sleep(10)
                            ser.write(str.encode("ATH\r"))
                            print("Hanging up")
                            '''
                            ser.write(str.encode('AT+CMGF=1\r'))
                            print("text mode enabled")
                            time.sleep(3)
                            ser.write(str.encode('AT+CMGS="+918970736699"\r'))
                            msg="hello"
                            time.sleep(3)
                            ser.write(str.encode(msg+chr(26)))
                            time.sleep(3)
                            print("message sent")'''
                            time.sleep(30)
                        break
                    elif bpm < 70:
                        low_pulse=time.time()
                        time.sleep(1)
                        if (time.time()-low_pulse)>pulse_pause:
                            ser.write(str.encode("ATD+918970736699;\r"))
                            print("Dialling...low_pulse")
                            time.sleep(10)
                            ser.write(str.encode("ATH\r"))
                            print("Hanging up")
                            '''
                            ser.write(str.encode('AT+CMGF=1\r'))
                            print("text mode enabled")
                            time.sleep(3)
                            ser.write(str.encode('AT+CMGS="+918970736699"\r'))
                            msg="hello"
                            time.sleep(3)
                            ser.write(str.encode(msg+chr(26)))
                            time.sleep(3)
                            print("message sent")'''
                            time.sleep(30)
                        break
                    elif temp >150 :
                        high_pulse=time.time()
                        time.sleep(1)
                        if (time.time()-high_pulse)>bpm_pause:
                            ser.write(str.encode("ATD+918970736699;\r"))
                            print("Dialling...high_pulse")
                            time.sleep(10)
                            ser.write(str.encode("ATH\r"))
                            print("Hanging up")
                            '''
                            ser.write(str.encode('AT+CMGF=1\r'))
                            print("text mode enabled")
                            time.sleep(3)
                            ser.write(str.encode('AT+CMGS="+918970736699"\r'))
                            msg="hello"
                            time.sleep(3)
                            ser.write(str.encode(msg+chr(26)))
                            time.sleep(3)
                            print("message sent")'''
                            time.sleep(30)
                        break
                    else:
                        print("No Heartbeat found %d" % bpm)
                        print("Temp  : {} ({}V) {} deg C".format(temp_level,temp_volts,temp)) 
                  
                    #time.sleep(1)
            print(response1.status,response1.reason,response2.status,response2.reason)
            data1=response1.read()
            data2=response2.read()
        except InterruptedError as ie:
            p.stopAsyncBPM()
            conn.close()
        except ConnectionError as ce:
            print("Connection failed",ce)
        except KeyboardInterrupt as ki:
            print(ki)
            exit()
        break
        #time.sleep(delay)
    
if __name__=="__main__":
    while True:
        health_monitor()

'''
SERIAL_PORT="/dev/ttyS0"
ser=serial.Serial(SERIAL_PORT,baudrate=9600,timeout=5)
ser.write(str.encode("ATD+918970736699;\r"))
print("Dialling...")
time.sleep(10)
ser.write(str.encode("ATH\r"))
print("HAnging up")
ser.write(str.encode('AT+CMGF=1\r'))
print("text mode enabled")
time.sleep(3)
ser.write(str.encode('AT+CMGS="+918970736699"\r'))
msg="hello"
time.sleep(3)
ser.write(str.encode(msg+chr(26)))
time.sleep(3)
print("message sent")'''
