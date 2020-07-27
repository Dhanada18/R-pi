import paho.mqtt.client as mqtt
import json
from random import *
import time
import dht
import RPi.GPIO as GPIO

iot_hub = 'demo.thingsboard.io'
port = 1883

username = 'njbHFssfAm9jyoommVlr'
password = ''
topic = 'v1/devices/me/telemetry'

client = mqtt.Client()
client.username_pw_set(username,password)

client.connect(iot_hub,port)
print("connected")
data = dict()

GPIO.setmode(Gpio.BOARD)
Fan_Pin = 7
#DEVICE_ADDRESS = 0x48
#Temp_sensor = 12
TEMP_THRESHOLD = 30
#TEMP_HYST = 2
GPIO.setup(Fan_Pin,GPIO.OUT)
GPIO.setup(Temp_sensor,GPIO.IN)
temp_sensor = dht.DHT22(Pin(14))

while True:
	time.sleep(1)
	#Read the temp register
	sensor.measure()
	temp_sensor.temperature()
	print('Temperature: %3.1f C' %temp_sensor)

	#control the fan based on the temp
	if(temp_snsore > TEMP_THRESHOLD):
		GPIO.output(FAN_PIN, True)
	if(temp_sensor < (TEMP_THRESHOLD)):
		GPIO.output(FAN_PIN, False)

