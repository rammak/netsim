def str_to_mac(mac: str):
    if len(mc := mac.split(':')) != 6:
        return None
    m = bytearray(6)
    for i in range(6):
        m[i] = int(mc[i], 16)
    return m


def hex_to_str(mac: bytes):
    macstr = ""
    for i in range(len(mac)):
        macstr += hex(mac[i])[2:] + ':'
    return macstr[:-1]


def type_to_str(type : int):
    if type == 0x0800:
        return str(type) + "IPv4"
    elif type == 0x0806:
        return str(type) + "ARP"
    elif type == 0x0842:
        return str(type) + "Wake-on-LAN"
    elif type == 0x86DD:
        return str(type) + "IPv6"
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

