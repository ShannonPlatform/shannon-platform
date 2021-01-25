from typing import Any, Dict
from bluepy import btle
from threading import Thread

from shannon_platform.base.notification_center import NotificationCenter, NotificationDefaultNames
from shannon_platform.base.metaclasses import Singleton


class BluetoothService:
    def __init__(self, address: str) -> None:
        self.peripheral = btle.Peripheral()
        self.peripheral.connect(address, btle.ADDR_TYPE_PUBLIC)
        self.peripheral.setDelegate(BluetoothNotificationHandler())
        self.service = self.p.getServiceByUUID("0000ffe0-0000-1000-8000-00805f9b34fb")
        self.characteristic = self.svc.getCharacteristics()[0]

        NotificationCenter().add_observer(name=NotificationDefaultNames.DATA_SEND, callback=self.write)

        read_thread = Thread(target=self.read)
        read_thread.start()


    def read(self) -> None:
        while True:
            if self.p.waitForNotifications(1.0):
                continue

    def write(self, user_info: Dict[str, Any]) -> None:
        command = bytes([user_info['id'], user_info['value']])
        self.characteristic.write(command)
    

    def request_devices(self) -> None:
        self.characteristic.write(bytes([0x00, 0x00]))


class BluetoothNotificationHandler(btle.DefaultDelegate):
    def handleNotification(self, cHandle, data):
        if len(data) < 2:
            return

        # device register
        if data[0] == 0x00:
            NotificationCenter().post(
                name=NotificationDefaultNames.REGISTER,
                user_info={
                    'id': data[1]
                }
            )
        # data receive
        else:
            NotificationCenter().post(
                name=NotificationDefaultNames.DATA_RECEIVE,
                user_info={
                    'id': data[0],
                    'value': data[1]
                }
            )