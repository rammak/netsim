from netstack.l1_interface import Interface
from netstack.l2_ethernet import frame_ethernet

i = Interface(interface_name='dum0')

while True:
	f = i.receive()
	fe = frame_ethernet()
	fe.get(f)
	fe.print_header()


