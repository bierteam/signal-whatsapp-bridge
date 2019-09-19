from pydbus import SystemBus
from gi.repository import GLib
from time import sleep
import re

signalGroup = [175, 177, 152, 66, 116, 102, 45, 32, 30, 52, 106, 98, 219, 217, 112, 12]
# Kinders signalGroup = [113, 38, 137, 78, 80, 168, 22, 161, 43, 32, 66, 248, 20, 74, 73, 79]

bus = SystemBus()
signal = bus.get('org.asamk.Signal')
loop = GLib.MainLoop()

class Signal:
    def __init__(self, WhatsApp):
        self.WhatsApp = WhatsApp

    def msgRcv (self, timestamp, source, groupID, message, attachments):
        print ("Signal: {} \n{}".format(source, message))
        self.send(source, groupID, message)
        return

    def getMessage(self):
        signal.onMessageReceived = self.msgRcv
        loop.run()
        sleep(1)
        loop.quit()

    def send(self, source, groupID, message):
        if(groupID == signalGroup):
            if source == "+31652652611":
                source = "Oscar: "
            elif source == "+31624986088":
                source = "Rick: "
            elif source == "+31619429386‬":
                source = "Auke: "
            elif  source == "+31629042387‬":
                source = "Peter: "
            elif  source == "+31611708716":
                source = "Nino: "

            message = source + message
            self.WhatsApp.sendmsg(message)