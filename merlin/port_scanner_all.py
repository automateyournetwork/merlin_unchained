# ----------------
# Copyright
# ----------------
# Written by John Capobianco, March 2021
# Copyright (c) 2021 John Capobianco
import django
django.setup()
from merlin.models import Devices, NMAP
from nmap import PortScanner
from datetime import datetime

device_list = Devices.objects.all()
nm = PortScanner()
timestamp=datetime.now().replace(microsecond=0)

for device in device_list:
    ip = device.ip_address
    print(f"\n --- Beginning Normal Scan of {ip} top 1024 TCP Ports")
    normal_scan_output = nm.scan(ip, '1-1024')
    print(f" --- command: {nm.command_line()}")
    print(f"\n --- Beginning UDP Scan of {ip} top 1024 UDP Ports")
    udp_scan_output = nm.scan(ip, '1-1024', '-v -sU')
    print(f" --- command: {nm.command_line()}")

for tcp_port in normal_scan_output['scan'][ip]['tcp']:
    tcp_write=NMAP(pyats_alias=device.alias,os=device.os,protocol="tcp",port=tcp_port,conf=normal_scan_output['scan'][ip]['tcp'][tcp_port]['conf'],cpe=normal_scan_output['scan'][ip]['tcp'][tcp_port]['cpe'],extra_info=normal_scan_output['scan'][ip]['tcp'][tcp_port]['extrainfo'],name=normal_scan_output['scan'][ip]['tcp'][tcp_port]['name'],product=normal_scan_output['scan'][ip]['tcp'][tcp_port]['product'],reason=normal_scan_output['scan'][ip]['tcp'][tcp_port]['reason'],state=normal_scan_output['scan'][ip]['tcp'][tcp_port]['state'],version=normal_scan_output['scan'][ip]['tcp'][tcp_port]['version'],timestamp=timestamp)
    tcp_write.save()

for udp_port in udp_scan_output['scan'][ip]['udp']:
    udp_write=NMAP(pyats_alias=device.alias,os=device.os,protocol="udp",port=udp_port,conf=udp_scan_output['scan'][ip]['udp'][udp_port]['conf'],cpe=udp_scan_output['scan'][ip]['udp'][udp_port]['cpe'],extra_info=udp_scan_output['scan'][ip]['udp'][udp_port]['extrainfo'],name=udp_scan_output['scan'][ip]['udp'][udp_port]['name'],product=udp_scan_output['scan'][ip]['udp'][udp_port]['product'],reason=udp_scan_output['scan'][ip]['udp'][udp_port]['reason'],state=udp_scan_output['scan'][ip]['udp'][udp_port]['state'],version=udp_scan_output['scan'][ip]['udp'][udp_port]['version'],timestamp=timestamp)
    udp_write.save()