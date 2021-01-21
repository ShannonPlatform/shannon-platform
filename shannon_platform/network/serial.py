from serial import Serial
from threading import Thread

from shannon_platform.base.notification_center import NotificationCenter
from shannon_platform.base.singleton import Singleton


class SerialService(metaclass=Singleton):
    __adaptor = Serial(port='/dev/cu.usbmodem14301', baudrate=9600)

    def __init__(self) -> None:
        super().__init__()

        NotificationCenter().add_observer(name="com.shannon.device-send", callback=self.write)

        serial_read_thread = Thread(target=self.read)
        serial_read_thread.start()
        
    def read(self):
        while True:
            data = self.__adaptor.read(2)
            if data:
                id = data[0]
                value = data[1]

                NotificationCenter().post(
                    name="com.shannon.device-receive", 
                    user_info={
                        'id': id,
                        'value': value
                    }
                )

    def write(self, user_info):
        command = bytes([user_info['id'], user_info['value']])
        self.__adaptor.write(command)