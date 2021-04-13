def hex_to_str(hex_array: bytes):
    out = ""
    for i in range(len(hex_array)):
        out += "{0:0{1}x}".format(hex_array[i], 2) + ':'
    return out[:-1]


def str_to_hex(string: str):
    temp = str.split(':')
    out = bytearray(6)
    for i in range(len(temp)):
        out[i] = int(temp[i], 16)
    return out


def str_to_ip(string: str):
    temp = string.split('.')
    if len(temp) != 4:
        return None
    out = bytearray(4)
    for i in range(4):
        out[i] = int(temp[i])
    return out


def ip_to_str(ip: bytes):
    out = ""
    for i in range(4):
        out += str(ip[i]) + "."
    return out[:-1]

