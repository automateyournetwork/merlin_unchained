# ----------------
# Copyright
# ----------------
# Written by John Capobianco, March 2021
# Copyright (c) 2021 John Capobianco
from merlin.models import Devices
from nmap import PortScanner
from pprint import pprint

device_list = Devices.objects.all()
nm = PortScanner()

for device in device_list:
    ip = device.ip_address
    print(f"\n --- Beginning Normal Scan of {ip} top 1024 TCP Ports")
    normal_scan_output = nm.scan(ip, '1-1024')
    print(f"--- command: {nm.command_line()}")
    pprint(normal_scan_output['scan'][ip]['tcp'])
    print(f"\n --- Beginning UDP Scan of {ip} top 1024 UDP Ports")
    udp_scan_output = nm.scan(ip, '1-1024', '-v -sU')
    print(f"--- command: {nm.command_line()}")
    pprint(udp_scan_output['scan'][ip]['udp'])    