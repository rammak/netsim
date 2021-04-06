import time
from netstack.l0_interface import VirtualInterface as vi

inter = vi("eth99")
inter.initialize("192.168.1.1/24")
time.sleep(10)
