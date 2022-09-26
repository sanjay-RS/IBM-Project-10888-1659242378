import datetime
import time
import random

now = datetime.datetime.now()

while True:
    temperature = random.randint(0, 100)
    humidity = random.randint(0, 100)
    if(temperature>=50 or humidity>=50):      
	print("Threshold temperature/humidity crossed limit on",now.strftime("%d-%m-%y"),"at",now.strftime("%H:%M"))
	time.sleep(1)