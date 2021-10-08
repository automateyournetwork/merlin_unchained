# ----------------
# Copyright
# ----------------
# Written by John Capobianco, March 2021
# Copyright (c) 2021 John Capobianco
from merlin.models import Devices, DynamicJobInput
from django.db.models import Q
from nmap import PortScanner
from pprint import pprint

search_input = DynamicJobInput.objects.latest('timestamp')
device_list = Devices.objects.filter(Q(hostname=search_input.input_field) | Q(alias=search_input.input_field) | Q(device_type=search_input.input_field) | Q(os=search_input.input_field) | Q(username=search_input.input_field) | Q(ip_address=search_input.input_field) | Q(platform=search_input.input_field))
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