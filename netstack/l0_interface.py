import subprocess


def check_dummy_module():
    lsmod = subprocess.Popen(['sudo', 'lsmod'], stdout=subprocess.PIPE)
    grep = subprocess.run(['grep', 'dummy'], stdin=lsmod.stdout)
    lsmod.wait()
    if grep.returncode == 0:
        return True
    else:
        return False


def load_dummy_module(unload=False):
    if unload is False:
        print("Loading dummy module...")
        mod = subprocess.run(['sudo', 'modprobe', 'dummy'])
    else:
        print("Removing dummy module...")
        mod = subprocess.run(['sudo', 'rmmod', 'dummy'])


class VirtualInterface:
    interface_name = None

    def __init__(self, name):
        # todo: test for valid name
        self.interface_name = name
        if check_dummy_module():
            print("Dummy module is already loaded")
        else:
            load_dummy_module()

    def __del__(self):
        print("Deleting interface ", self.interface_name)
        load_dummy_module(unload=True)

    def initialize(self, ip_address):
        print("Initializing virtual interface ", self.interface_name, " with IP ", ip_address)
        link = subprocess.run(['sudo', 'ip', 'link', 'add', self.interface_name, 'type', 'dummy'])
        # todo: change mac using "sudo ifconfig eth10 hw ether 00:22:22:ff:ff:ff"
        # todo: test for valid ip address
        ip = subprocess.run(['sudo', 'ip', 'addr', 'add', ip_address, 'brd', '+', 'dev', self.interface_name, 'label', self.interface_name + ':0'])

