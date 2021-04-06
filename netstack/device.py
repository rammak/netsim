from enum import Enum


class DeviceType(Enum):
    TYPE_HOST = 1
    TYPE_L0 = 2
    TYPE_L1 = 3
    TYPE_L2 = 4
    TYPE_L3 = 5


class NetDevice:
    type = None
    name = None

    def __init__(self, device_name, device_type: DeviceType = DeviceType['TYPE_HOST']):
        # todo: test for device type and name validity
        self.type = device_type
        self.name = device_name
        print("Initializing ", device_name, " of ", device_type)
        
    def __del__(self):
        pass

