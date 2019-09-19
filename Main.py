from WhatsApp import WhatsApp
from Signal import Signal
from time import sleep

from threading import Thread

whatsappGroup = "Signal test"

print("starting....")
x = WhatsApp(whatsappGroup)
y = Signal(x)

while True:
    sleep(1)
    print("APP")
    x.get_last_message
    # t = Thread(x.get_last_message())
    # t.start()
    
    print("SIGNAL")
    y.getMessage()
