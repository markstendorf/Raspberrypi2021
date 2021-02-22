#Statemachine til beskrivelse af livets gang
from gpiozero import LED
from gpiozero import Button
from time import sleep
from picamera import PiCamera
from datetime import datetime

NSred= LED(13)
NSgul=LED(19)
NSgreen=LED(26)
NSsidegul=LED(4)
NSsidegrøn=LED(5)

EVred=LED(21)
EVgul=LED(20)
EVgreen=LED(16)
EVsidegul=LED(24)
EVsidegrøn=LED(23)

NSknap = Button(17)#blå
EVknap = Button(6)#gul
Slukknap = Button(12)#rød

Sidetilside = 0
Svingbanetur = 0

camera=PiCamera()
dato= datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
print("Dato=",dato)

def biloverNS():
    sleep(0.5)
    if NSknap.is_pressed:
        print("Bil køre over rød NS")
    sleep(0.5)
    if NSknap.is_pressed:
        print("Bil køre over for maget rød NS")
        tagbillede()
        
def biloverEV():
    sleep(0.5)
    if EVknap.is_pressed:
        print("Bil køre over rød EV")
    sleep(0.5)
    if EVknap.is_pressed:
        print("Bil køre over for maget rød EV")
        tagbillede()

def tagbillede():
    global dato
    camera.start_preview
    sleep(2)
    camera.capture('/home/pi/Desktop/'+dato+'.jpg')
    camera.stop_preview
    dato=dato+".jpg"
    
def Stop():
    EVsidegul.off()
    NSsidegul.off()
    NSgul.off()
    EVgul.off()
    NSred.off()
    EVred.off()
    NSsidegrøn.off()
    EVsidegrøn.off()
    NSgreen.off()
    EVgreen.off()
    
def Rød():
    global Sidetilside
    global svingbanetur
    EVsidegul.off()
    NSsidegul.off()
    NSgul.off()
    EVgul.off()
    print ('\x1b[6;30;41m' + " Rød! stop " + '\x1b[0m''   \x1b[6;30;41m' + " Rød! stop " + '\x1b[0m')
    NSred.on()
    EVred.on()
    biloverEV()
    biloverNS()
    sleep(1)
    if Svingbanetur == 2:
        return SvingbaneRødGul()
    if Sidetilside == 0:
        return RødGulNS()
    elif Sidetilside == 1:
        return RødGulVØ()
#Svingbane
def SvingbaneRødGul():
    print ('\x1b[6;30;43m' + "RødGul! pil" + '\x1b[0m''   \x1b[6;30;43m' + "RødGul! pil" + '\x1b[0m')
    EVsidegul.on()
    NSsidegul.on()
    sleep(2)
    return SvingbaneGrøn()
def SvingbaneGrøn():
    global Svingbanetur
    EVsidegul.off()
    NSsidegul.off()
    print ('\x1b[7;32;40m' + " Grøn! pil " + '\x1b[0m''   \x1b[7;32;40m' + " Grøn! pil " + '\x1b[0m')
    NSsidegrøn.on()
    EVsidegrøn.on()
    sleep(4)
    Svingbanetur = 0
    return SvingbaneGul()
def SvingbaneGul():
    global Svingbanetur
    NSsidegrøn.off()
    EVsidegrøn.off()    
    print ('\x1b[6;30;43m' + " Gul! pil  " + '\x1b[0m''   \x1b[6;30;43m' + " Gul! pil  " + '\x1b[0m')
    EVsidegul.on()
    NSsidegul.on()
    sleep(1)
    return Rød()
#NS
def GrønNS():
    NSred.off()
    NSgul.off()
    print ('\x1b[7;32;40m' + " Grøn! Kør " + '\x1b[0m''   \x1b[6;30;41m' + " Rød! stop " + '\x1b[0m')
    NSgreen.on()
    sleep(1)
    biloverEV()
#    print ('\x1b[7;32;40m' + " Grøn! pil " + '\x1b[0m')
    sleep(1)
    biloverEV()
    sleep(1)
    biloverEV()
    sleep(1)
    biloverEV()
    sleep(1)
    biloverEV()
    return GulNS()

def RødGulNS():
    print ('\x1b[6;30;43m' + "RødGul! Kør" + '\x1b[0m''   \x1b[6;30;41m' + " Rød! stop " + '\x1b[0m')
    NSgul.on()
    biloverEV()
    sleep(1)
    biloverEV()
    sleep(1)
    return GrønNS()

def GulNS():
    global Sidetilside
    global Svingbanetur
    NSgreen.off()
    print ('\x1b[6;30;43m' + " Gul! stop " + '\x1b[0m''   \x1b[6;30;41m' + " Rød! stop " + '\x1b[0m')
    NSgul.on()
    biloverNS()
    biloverEV()
    sleep(1)
    Sidetilside = 1
    Svingbanetur += 1
    return Rød()

#VØ
def GrønVØ():
    EVgul.off()
    EVred.off()
    print ('\x1b[6;30;41m' + " Rød! stop " + '\x1b[0m''   \x1b[7;32;40m' + " Grøn! Kør " + '\x1b[0m')
    EVgreen.on()
    biloverNS()
    sleep(1)
#    print ('              \x1b[7;32;40m' + " Grøn! pil " + '\x1b[0m')
    biloverNS()
    sleep(1)
    biloverNS()
    sleep(1)
    biloverNS()
    sleep(1)
    biloverNS()
    sleep(1)
    return GulVØ()

def RødGulVØ():
    print ('\x1b[6;30;41m' + " Rød! stop " + '\x1b[0m''   \x1b[6;30;43m' + "RødGul! Kør" + '\x1b[0m')
    EVgul.on()
    biloverNS()
    sleep(1)
    biloverNS()
    sleep(1)
    return GrønVØ()

def GulVØ():
    global Sidetilside
    global Svingbanetur
    EVgreen.off()
    print ('\x1b[6;30;41m' + " Rød! stop " + '\x1b[0m''   \x1b[6;30;43m' + " Gul! stop " + '\x1b[0m')
    EVgul.on()
    biloverEV()
    biloverNS()
    sleep(1)
    Sidetilside = 0
    Svingbanetur += 1
    return Rød()


    
state=Rød()
while True:
    while state: state=Rød()  # starter statemachine
    print ("Done with states")

