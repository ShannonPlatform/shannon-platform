from typing import Any, Dict
from bluepy import btle
from threading import Thread

from shannon_platform.base.notification_center import NotificationCenter, NotificationDefaultNames
from shannon_platform.base.metaclasses import Singleton


class BluetoothService:
    def __init__(self, address: str) -> None:
        self.address = address
        self.delegate = BluetoothNotificationHandler()

        self.connect()

        NotificationCenter().add_observer(name=NotificationDefaultNames.DATA_SEND, callback=self.write)

        read_thread = Thread(target=self.read)
        read_thread.start()

    def connect(self) -> None:
        self.peripheral = btle.Peripheral()
        self.peripheral.connect(self.address, btle.ADDR_TYPE_PUBLIC)
        self.peripheral.setDelegate(self.delegate)
        self.service = self.peripheral.getServiceByUUID("0000ffe0-0000-1000-8000-00805f9b34fb")
        self.characteristic = self.service.getCharacteristics()[0]


    def read(self) -> None:
        while True:
            try:
                if self.peripheral.waitForNotifications(4.0):
                    continue
            except Exception as error:
                print(error)
                self.peripheral.disconnect()                
                continue

    def write(self, user_info: Dict[str, Any]) -> None:
        try:
            command = bytes([user_info['id'], user_info['value']])
            self.characteristic.write(command)
        except btle.BTLEDisconnectError:
            self.connect()
    

    def request_devices(self) -> None:
        self.characteristic.write(bytes([0x00, 0x00]))

    def shutdown(self) -> None:
        self.peripheral.disconnect()


class BluetoothNotificationHandler(btle.DefaultDelegate):
    def handleNotification(self, cHandle, data):
        buffer = bytearray(data)
        
        for i in range(len(buffer)//2):
            id = buffer[i*2]
            value = buffer[i*2+1]

            # device register
            if id == 0x00:
                NotificationCenter().post(
                    name=NotificationDefaultNames.REGISTER,
                    user_info={
                        'id': value
                    }
                )
            # data receive
            else:
                NotificationCenter().post(
                    name=NotificationDefaultNames.DATA_RECEIVE,
                    user_info={
                        'id': id,
                        'value': value
                    }
                )