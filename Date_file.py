#Kan benyttes i forbindelse med lyskryds, køre over for rødt!!!!!

from datetime import datetime
from time import sleep
from picamera import PiCamera

camera=PiCamera()

dato= datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
print("Dato=",dato)

camera.start_preview
sleep(2)
camera.capture("Sti til billede filen"+dato+".jpg")
camera.stop_preview
dato=dato+".jpg"

