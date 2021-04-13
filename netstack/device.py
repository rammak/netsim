from enum import Enum
from netstack.l1_interface import Interface

class DeviceType(Enum):
    TYPE_HOST = 1
    TYPE_L0 = 2
    TYPE_L1 = 3
    TYPE_L2 = 4
    TYPE_L3 = 5


class NetDevice:
    type = None
    name = None
    l1 = None

    def __init__(self, device_name, device_type: DeviceType = DeviceType['TYPE_HOST']):
        # todo: test for device type and name validity
        self.type = device_type
        self.name = device_name
        print("Initializing ", device_name, " of ", device_type)

    def add_interface(self, name):
        self.l1 = Interface(name)


    def __del__(self):
        pass

