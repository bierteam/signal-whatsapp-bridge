from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
from pydbus import SystemBus
import re
from gi.repository import GLib

import dbus
from dbus.mainloop.glib import DBusGMainLoop
DBusGMainLoop(set_as_default=True)

signalGroup = [175, 177, 152, 66, 116, 102, 45, 32, 30, 52, 106, 98, 219, 217, 112, 12]
kinderGroup = [113, 38, 137, 78, 80, 168, 22, 161, 43, 32, 66, 248, 20, 74, 73, 79]

bus = SystemBus()
signal = bus.get('org.asamk.Signal')

class Signal:
    def __init__(self, WhatsApp):
        self.WhatsApp = WhatsApp

    def msgRcv (self, timestamp, source, groupID, message, attachments):
        print ("Signal: {} \n{}".format(source, message))
        self.send(source, groupID, message)
        return

    def getMessage(self):
        signal.onMessageReceived = self.msgRcv

        dbus_loop = DBusGMainLoop()
        bus = dbus.SessionBus(mainloop=dbus_loop)

        loop = GLib.MainLoop() 
        loop.run()


        # loop = GLib.MainLoop()
        # loop.run()

        # x=Thread(target = loop.run, args = ())
        # x.setDaemon(True)
        # x.start()
        # x.join()

    def send(self, source, groupID, message):
        if(groupID == signalGroup):
            self.WhatsApp.sendmsg(message)