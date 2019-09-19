from WhatsApp import WhatsApp
from Signal import Signal
from time import sleep

from threading import Thread

whatsappGroup = "Signal test"

print("starting....")
x = WhatsApp(whatsappGroup)
y = Signal(x)

while True:
    print("APP")
    t = Thread(x.get_last_message())
    t.start()

    print("SIGNAL")
    y.getMessage()
