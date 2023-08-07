import requests

# Local network to scan


class network:
    def __init__(self, net_adress, cidr):
        self.net_adress = net_adress
        self.cidr = cidr
        # self.hosts
        # self.first_usable
        # self.last_usable

    # Calculates number of hosts on network
    def calculate_hosts():
        pass

    def get_first_usable():
        pass

    def get_last_usable():
        pass

    # Scans network
    def scan_network():
        pass

# Found host that responds to http-request


class host:
    def __init__(self, ip_adress, name):
        self.ip_adress = ip_adress
