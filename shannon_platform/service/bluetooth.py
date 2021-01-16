import pygatt
import binascii
import uuid

adapter = pygatt.BGAPIBackend()
adapter.start()
device = adapter.connect('00:15:87:10:9A:4E')