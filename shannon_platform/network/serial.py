from os import name
from shannon_platform.base.notification_center import NotificationCenter
import threading
from typing import Callable
from serial import Serial
from serial.serialutil import PortNotOpenError
from threading import Thread
from time import sleep

from shannon_platform.base.singleton import Singleton


class SerialService():
    __adaptor = None

    @staticmethod
    def adaptor() -> Serial:
        if SerialService.__adaptor != None:
            return SerialService.__adaptor
        else:
            SerialService.__adaptor = Serial(port='/dev/cu.usbmodem14301', baudrate=9600)
            sleep(2)
            return SerialService.__adaptor

    def __init__(self) -> None:
        super().__init__()

    def request(self, message: str) -> str:
        self.adaptor().flush()
        self.adaptor().write(message.encode('ascii'))
        self.adaptor().write("message\n".encode('ascii'))
        responce = self.adaptor().readline().decode('ascii')

        return responce

