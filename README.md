# Shannon Home Automation Platform
this project contains a python package to run your custom design home automation using arduino boards and raspberry pi. This project have been developed to work with Homebridge project, because of that some responses in web response may not be standard. 

## installation
you can install this project using pip
```bash
pip install shannon_platform
```

## requirements
to support bluetooth I have used the BluePy library which supports only linux. if you are considering to run this project on any OS other than Linux, you need to refactor `bluetooth.py` file.

## how arduino device can join the network?
arduino devices can connect to the system using serial ports or BLE protocol. the arduino device considered as a network routers. Inside the arduino code you can define different devices that connect to arduino using I/O pins.

Every I/O command is two byte data. The first byte defines the id of the device and the second byte defines the data that must transfer. The first four bits of id-byte (first byte) defines the type of device. to see list of available device types check the device type section.

```python
0x11 0x02
# ||   |____ Data to transfer, int number between (0, 255)
# ||________ Device unique id number (0, 15)
# |_________ Device type
```

## id palette

| id | description |
|----|-------------|
|0x00| request/response device list |
|0x1x| switch |
|0x2x| sensor |

## 🚧 UNDER CONSTRUCTION 🚧