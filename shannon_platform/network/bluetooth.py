from typing import Any, Dict
from shannon_platform.base.notification_center import NotificationCenter
from bluepy import btle
from threading import Thread

from shannon_platform.base.notification_center import NotificationCenter
from shannon_platform.base.metaclasses import Singleton


class BluetoothService(metaclass=Singleton):
    def __init__(self) -> None:
        super().__init__()

        self.peripheral = btle.Peripheral()
        self.peripheral.connect(self.address, btle.ADDR_TYPE_PUBLIC)
        self.peripheral.setDelegate(BluetoothNotificationHandler())
        self.service = self.p.getServiceByUUID("0000ffe0-0000-1000-8000-00805f9b34fb")
        self.characteristic = self.svc.getCharacteristics()[0]

        NotificationCenter().add_observer(name="com.shannon.device-send", callback=self.write)

        read_thread = Thread(target=self.read)
        read_thread.start()


    def read(self) -> None:
        while True:
            if self.p.waitForNotifications(1.0):
                continue

    def write(self, user_info: Dict[str, Any]) -> None:
        command = bytes([user_info['id'], user_info['value']])
        self.characteristic.write(command)


class BluetoothNotificationHandler(btle.DefaultDelegate):
    def handleNotification(self, cHandle, data):
        if len(data) < 2:
            return

        NotificationCenter().post(
            name="com.shannon.device-receive",
            user_info={
                'id': data[0],
                'value': data[1]
            }
        )