from netstack.common import *


def type_to_str(ether_type: int):
    if ether_type == 0x0800:
        return "IPv4"
    elif ether_type == 0x0806:
        return "ARP"
    elif ether_type == 0x0842:
        return "Wake-on-LAN"
    elif ether_type == 0x86DD:
        return "IPv6"
    else:
        return "Unknown"


class frame_ethernet:
    mac_dst = bytearray(6)
    mac_src = bytearray(6)
    ether_type = 0
    payload = bytearray()
    fcs = bytearray(4)
    length = 0

    def __init__(self):
        pass

    def set(self, mac_dst: bytearray, mac_src: bytearray, payload: bytes, ether_type: int = bytearray(b'\x08\x00')):
        if len(mac_dst) != 6 or len(mac_src) != 6:
            return None
        self.mac_src = mac_src
        self.mac_dst = mac_dst
        self.ether_type = ether_type
        self.payload = payload

    def get(self, data : bytes):
        self.mac_dst = data[:6]
        self.mac_src = data[6:12]
        self.ether_type = (data[12] << 8) + data[13]
        self.payload = data[14:]

    def print_header(self):
        print("Dst : ", hex_to_str(self.mac_dst), "\tSrc : ", hex_to_str(self.mac_src), "\tType : ",
              type_to_str(self.ether_type))

