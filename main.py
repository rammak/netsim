import time
from netstack.l0_interface import VirtualInterface as vi
from netstack.device import NetDevice

inter = vi("eth99")
inter.initialize("192.168.1.1/24")
dev = NetDevice("Host1")
time.sleep(1)
