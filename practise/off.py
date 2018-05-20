import RPi.GPIO as GPIO
import RPi.GPIO as IO #Import GPIO library
import time
import sys #Import time library
#from furl import furl

#import mysql.connector

GPIO.setmode(GPIO.BOARD)                          #Set GPIO pin numbering
GPIO.setwarnings(False)
#roomID=sys.argv[1]

room = sys.argv[1]

deviceId = sys.argv[2]

pir = 11
        
if(sys.argv[1]=="1" and sys.argv[2]=="1"):
    pir = 11                                        #Associate pin 26 to pir
    
elif(sys.argv[1]=="2" and sys.argv[2]=="1"):
    pir = 13                                        #Associate pin 26 to pir
 
elif(sys.argv[1]=="3" and sys.argv[2]=="1"):
    pir = 15                                        #Associate pin 26 to pir

elif(sys.argv[1]=="4" and sys.argv[2]=="1"):
    pir = 19                                        #Associate pin 26 to pir

elif(sys.argv[1]=="5" and sys.argv[2]=="1"):
    pir = 21                                        #Associate pin 26 to pir

elif(sys.argv[1]=="6" and sys.argv[2]=="1"):
    pir = 23                                        #Associate pin 26 to pir
    
elif(sys.argv[2]=="2"):
    pir = 33

GPIO.setup(pir, GPIO.OUT)                          #Set pin as GPIO in
GPIO.output(pir,0)
#print("chalu ho gai")

print("off")

if(sys.argv[1]=="1" and sys.argv[2]=="2"):
    GPIO.setup(33, GPIO.OUT)
    # Set PWM instance and their frequency
    pwm33 = GPIO.PWM(33, 10)
    pwm33.start(60)
    pwm33.stop()
    print("ruk gya fan")
