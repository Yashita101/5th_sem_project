import datetime
import spidev
import time
import os
from pulsesensor import Pulsesensor
from temperature import TemperatureSensor
import RPi.GPIO as GPIO
import serial
import sys
import http.client
import urllib.request


#health_monitor_key="JVOD9WXB1P4NJBRR"
pulse_key = "OV4UT8JRYDWS5B53"
temp_key="VMPNSROP5WNJPZJ3"
pause=5

SERIAL_PORT="/dev/ttyS0"

ser=serial.Serial(SERIAL_PORT,baudrate=9600,timeout=5)
p = Pulsesensor()
p.startAsyncBPM()
t = TemperatureSensor()

def health_monitor():
    delay = 1

    while True:
        try:
            temp_level = t.ReadChannel()
            temp_volts = t.ConvertVolts(temp_level,2)
            temp       = t.ConvertTemp(temp_level,2)
            bpm = p.BPM
            time.sleep(1)
            start=time.time()
            
            params1=urllib.parse.urlencode({'field1':temp,'key':temp_key})
            headers1={"Content-typZZe":"application/x-www-form-urlencoded","Accept":"text/plain"}
            conn1=http.client.HTTPConnection("api.thingspeak.com:80")
            
            params2=urllib.parse.urlencode({'field1':bpm,'key':pulse_key})
            headers2={"Content-typZZe":"application/x-www-form-urlencoded","Accept":"text/plain"}
            conn2=http.client.HTTPConnection("api.thingspeak.com:80")        

            conn1.request("POST","/update",params1,headers1)
            response1=conn1.getresponse()
            conn2.request("POST","/update",params2,headers2)
            response2=conn2.getresponse()
            
            phone=["+918970736699", "+919482141788"]
            
            if bpm > 0 and temp > 0:
                    
                    print ("--------------------------------------------"  )
                    print("BPM: %d" % bpm)
                    print("Temp  : {} ({}V) {} deg C".format(temp_level,temp_volts,temp))
                    time.sleep(5)
                    if (time.time()-start)>pause:
                        if temp < 30:
                            if bpm < 60:
                                print("Low BP and Low Temp")
                                
                                for i in range(len(phone)):
                                    ser.write(str.encode('AT+CMGF=1\r'))
                                    time.sleep(2)
                                    ser.write(str.encode('AT+CMGS="%s"\r'%phone[i]))
                                    time.sleep(2)
                                    msg="Patient NRSY has HYPOTHERMIA and LOW BP."
                                    time.sleep(2)
                                    ser.write(str.encode(msg+chr(26)))
                                    time.sleep(2)
                                    print("message sent to",phone[i])
                                '''
                                    
                                ser.write(str.encode('AT+CMGF=1\r'))
                                time.sleep(2)
                                ser.write(str.encode('AT+CMGS="+918970736699"\r'))
                                time.sleep(2)
                                msg="Patient NRSY has HYPOTHERMIA."
                                time.sleep(2)
                                ser.write(str.encode(msg+chr(26)))
                                time.sleep(2)
                                print("message sent ")
                                
                                ser.write(str.encode('AT+CMGF=1\r'))
                                time.sleep(2)
                                ser.write(str.encode('AT+CMGS="+919482141788"\r'))
                                time.sleep(2)
                                msg=" HYPOTHERMIA."
                                time.sleep(2)
                                ser.write(str.encode(msg+chr(26)))
                                time.sleep(2)
                                print("message sent ")'''
                            elif bpm > 110:
                                print("High BP and Low Temperature")
                                
                                for i in range(len(phone)):
                                    ser.write(str.encode('AT+CMGF=1\r'))
                                    time.sleep(2)
                                    ser.write(str.encode('AT+CMGS="%s"\r'%phone[i]))
                                    time.sleep(2)
                                    msg="Patient NRSY has HYPOTHERMIA and HIGH BP."
                                    time.sleep(2)
                                    ser.write(str.encode(msg+chr(26)))
                                    time.sleep(2)
                                    print("message sent to",i)
                                '''
                                ser.write(str.encode('AT+CMGF=1\r'))
                                time.sleep(2)
                                ser.write(str.encode('AT+CMGS="+918970736699"\r'))
                                time.sleep(2)
                                msg="Patient NRSY has HYPOTHERMIA."
                                time.sleep(2)
                                ser.write(str.encode(msg+chr(26)))
                                time.sleep(2)
                                print("message sent ")
                                
                                ser.write(str.encode('AT+CMGF=1\r'))
                                time.sleep(2)
                                ser.write(str.encode('AT+CMGS="+919482141788"\r'))
                                time.sleep(2)
                                msg=" HYPOTHERMIA."
                                time.sleep(2)
                                ser.write(str.encode(msg+chr(26)))
                                time.sleep(2)
                                print("message sent ")'''
                            else:
                                print("Low Temperature")
                                '''
                                ser.write(str.encode("ATD+918970736699;\r"))
                                print("Dialling...low_temp")
                                time.sleep(2)
                                ser.write(str.encode("ATH\r"))
                                print("Hanging up")
                                time.sleep(5)
                                '''
                            
                                for i in range(len(phone)):
                                    ser.write(str.encode('AT+CMGF=1\r'))
                                    time.sleep(2)
                                    ser.write(str.encode('AT+CMGS="%s"\r'%phone[i]))
                                    time.sleep(2)
                                    msg="Patient NRSY has HYPOTHERMIA."
                                    time.sleep(2)
                                    ser.write(str.encode(msg+chr(26)))
                                    time.sleep(2)
                                    print("message sent to",i)
                                #        break
                                '''
                            
                                ser.write(str.encode('AT+CMGF=1\r'))
                                time.sleep(2)
                                ser.write(str.encode('AT+CMGS="+918970736699"\r'))
                                time.sleep(2)
                                msg="Patient NRSY has HYPOTHERMIA."
                                time.sleep(2)
                                ser.write(str.encode(msg+chr(26)))
                                time.sleep(2)
                                print("message sent ")
                                
                                ser.write(str.encode('AT+CMGF=1\r'))
                                time.sleep(2)
                                ser.write(str.encode('AT+CMGS="+919482141788"\r'))
                                time.sleep(2)
                                msg=" HYPOTHERMIA."
                                time.sleep(2)
                                ser.write(str.encode(msg+chr(26)))
                                time.sleep(2)
                                print("message sent ")'''
                        elif temp > 34:
                            if bpm < 60:
                                print("high temp and low bp")
                                '''
                                ser.write(str.encode('AT+CMGF=1\r'))
                                print("text mode enabled")
                                time.sleep(3)
                                ser.write(str.encode('AT+CMGS="+918970736699"\r'))
                                msg="HIGH FEVER and LOW BP."
                                time.sleep(3)
                                ser.write(str.encode(msg+chr(26)))
                                time.sleep(3)
                                print("message sent")'''
                            elif bpm>110:
                                print("high temp and high bp")
                                '''
                                ser.write(str.encode('AT+CMGF=1\r'))
                                print("text mode enabled")
                                time.sleep(3)
                                ser.write(str.encode('AT+CMGS="+918970736699"\r'))
                                msg="HIGH FEVER and HIGH BP."
                                time.sleep(3)
                                ser.write(str.encode(msg+chr(26)))
                                time.sleep(3)
                                print("message sent")'''
                            else:
                                ser.write(str.encode("ATD+918970736699;\r"))
                                print("Dialling...high_temp")
                                time.sleep(2)
                                ser.write(str.encode("ATH\r"))
                                print("Hanging up")
                                time.sleep(5)
                                '''
                                ser.write(str.encode('AT+CMGF=1\r'))
                                print("text mode enabled")
                                time.sleep(3)
                                ser.write(str.encode('AT+CMGS="+918970736699"\r'))
                                msg="HIGH FEVER."
                                time.sleep(3)
                                ser.write(str.encode(msg+chr(26)))
                                time.sleep(3)
                                print("message sent")'''
                            #time.sleep(10)
                     #           break
                    
                        elif bpm < 60:
                            if temp < 30:
                                print("low temp and low bp")
                                '''
                                ser.write(str.encode('AT+CMGF=1\r'))
                                print("text mode enabled")
                                time.sleep(3)
                                ser.write(str.encode('AT+CMGS="+918970736699"\r'))
                                msg="LOW BP and HYPOTHERMIA."
                                time.sleep(3)
                                ser.write(str.encode(msg+chr(26)))
                                time.sleep(3)
                                print("message sent")'''
                            elif temp > 34:
                                print("high temp and low bp")
                                '''
                                ser.write(str.encode('AT+CMGF=1\r'))
                                print("text mode enabled")
                                time.sleep(3)
                                ser.write(str.encode('AT+CMGS="+918970736699"\r'))
                                msg="LOW BP and HIGH FEVER."
                                time.sleep(3)
                                ser.write(str.encode(msg+chr(26)))
                                time.sleep(3)
                                print("message sent")'''
                            else:
                                ser.write(str.encode("ATD+918970736699;\r"))
                                print("Dialling...low_pulse")
                                time.sleep(2)
                                ser.write(str.encode("ATH\r"))
                                print("Hanging up")
                                '''
                                ser.write(str.encode('AT+CMGF=1\r'))
                                print("text mode enabled")
                                time.sleep(3)
                                ser.write(str.encode('AT+CMGS="+918970736699"\r'))
                                msg="LOW BP"
                                time.sleep(3)
                                ser.write(str.encode(msg+chr(26)))
                                time.sleep(3)
                                print("message sent")'''
                                time.sleep(5)
                                #break
                        elif bpm >110 :
                            if temp <32:
                                print("low temp and high bp")
                                '''
                                ser.write(str.encode('AT+CMGF=1\r'))
                                print("text mode enabled")
                                time.sleep(3)
                                ser.write(str.encode('AT+CMGS="+918970736699"\r'))
                                msg="HIGH BP and HYPOTHERMIA."
                                time.sleep(3)
                                ser.write(str.encode(msg+chr(26)))
                                time.sleep(3)
                                print("message sent")'''
                            elif temp >34:
                                print("high temp and high bp")
                                '''
                                ser.write(str.encode('AT+CMGF=1\r'))
                                print("text mode enabled")
                                time.sleep(3)
                                ser.write(str.encode('AT+CMGS="+918970736699"\r'))
                                msg="HIGH BP and HIGH FEVER."
                                time.sleep(3)
                                ser.write(str.encode(msg+chr(26)))
                                time.sleep(3)
                                print("message sent")'''
                            else:
                                ser.write(str.encode("ATD+918970736699;\r"))
                                print("Dialling...high_pulse")
                                time.sleep(2)
                                ser.write(str.encode("ATH\r"))
                                print("Hanging up")
                                '''
                                ser.write(str.encode('AT+CMGF=1\r'))
                                print("text mode enabled")
                                time.sleep(3)
                                ser.write(str.encode('AT+CMGS="+918970736699"\r'))
                                msg="HIGH BP."
                                time.sleep(3)
                                ser.write(str.encode(msg+chr(26)))
                                time.sleep(3)
                                print("message sent")'''
                                time.sleep(5)
                                #break
                        
            else:
                    time.sleep(5)
                    if (time.time()-start)>5 and bpm == 0 or temp < 0:
                        print("No Heartbeat found %d" % bpm)
                        print("Temp  : {} ({}V) {} deg C".format(temp_level,temp_volts,temp))
                        '''
                                ser.write(str.encode('AT+CMGF=1\r'))
                                print("text mode enabled")
                                time.sleep(3)
                                ser.write(str.encode('AT+CMGS="+918970736699"\r'))
                                msg="EMERGENCY.Critical Condition."
                                time.sleep(3)
                                ser.write(str.encode(msg+chr(26)))
                                time.sleep(3)
                                print("message sent")'''
                        
                  
                    #time.sleep(3)
            #print(response1.status,response1.reason,response2.status,response2.reason)
    
            data1=response1.read()
            data2=response2.read()
        except InterruptedError as ie:
            p.stopAsyncBPM()
            conn1.close()
            conn2.close()
        except ConnectionError as ce:
            print("Connection failed",ce)
        except KeyboardInterrupt as ki:
            print(ki)
            exit()
        #break
        time.sleep(delay)
    
if __name__=="__main__":
    while True:
        health_monitor()