import threading
from typing import Callable
from serial import Serial
from serial.serialutil import PortNotOpenError
from threading import Thread
from time import sleep


class SerialConnection():
    __adaptor = None

    @staticmethod
    def adaptor() -> Serial:
        if SerialConnection.__adaptor != None:
            return SerialConnection.__adaptor
        else:
            SerialConnection.__adaptor = Serial(port='/dev/cu.usbmodem14301', baudrate=9600)
            sleep(2)
            return SerialConnection.__adaptor

    def __init__(self) -> None:
        super().__init__()

    def request(self, message: str) -> str:
        self.adaptor().flush()
        self.adaptor().write(message.encode('ascii'))
        self.adaptor().write("message\n".encode('ascii'))
        responce = self.adaptor().readline().decode('ascii')

        return responce











# class SerialListener(Thread):
#     def __init__(self, connection: Serial) -> None:
#         super().__init__()

#         self.connection = connection
#         self.readline_callback: Callable

#     def run(self) -> None:
#         while True:
#             try:
#                 data = self.connection.readline().decode('ascii')
#                 self.readline_callback(data)
#             except PortNotOpenError:
#                 print(PortNotOpenError)
#                 break
#             except Exception as error:
#                 print(error)

# class SerialWriter():
#     def __init__(self, connection: Serial) -> None:
#         super().__init__()

#         self.connection = connection

#     def writeline(self, message: str) -> None:
#         line = message + '\r\n'
#         self.connection.write(line.encode('ascii'))
