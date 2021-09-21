# ----------------
# Copyright
# ----------------
# Written by John Capobianco, March 2021
# Copyright (c) 2021 John Capobianco

# ----------------
# Python
# ----------------
import os
import sys
import yaml
import time
import json
import shutil
import logging
import requests
from pyats import aetest
from pyats import topology
from pyats.log.utils import banner
from general_functionalities import ParseLearnFunction
from datetime import datetime
from merlin.models import LearnInterface

# ----------------
# AE Test Setup
# ----------------
class common_setup(aetest.CommonSetup):
    """Common Setup section"""
    @aetest.subsection
    def connect_to_devices(self, testbed):
        """Connect to all the devices"""
        testbed.connect(learn_hostname=True)

# ----------------
# Test Case #1
# ----------------
class Collect_Information(aetest.Testcase):
    """Parse all the commands"""

    @aetest.test
    def parse(self, testbed, section, steps):
        """ Testcase Setup section """
        # ---------------------------------------
        # Loop over devices
        # ---------------------------------------
        for device in testbed:
            # Learn Interface to JSON
            self.learned_interface = ParseLearnFunction.parse_learn(steps, device, "interface")
            if self.learned_interface is not None:
                # Set Django Database values from pyATS JSON
                for interface in self.learned_interface:
                    if 'description' in self.learned_interface[interface]:
                        description = self.learned_interface[interface]['description']
                    else:
                        description = "null"

                    if 'enabled' in self.learned_interface[interface]:
                        enabled = self.learned_interface[interface]['enabled']
                    else:
                        enabled = "null"

                    if 'oper_status' in self.learned_interface[interface]:
                        oper_status = self.learned_interface[interface]['oper_status']
                    else:
                        oper_status = "null"

                    if 'access_vlan' in self.learned_interface[interface]:
                        access_vlan =  self.learned_interface[interface]['access_vlan']
                    else:
                        access_vlan = "null"

                    if 'native_vlan' in self.learned_interface[interface]:
                        native_vlan =  self.learned_interface[interface]['native_vlan']
                    else:
                        native_vlan = "null"

                    if 'switchport_enable' in self.learned_interface[interface]:
                        switchport_enable =  self.learned_interface[interface]['switchport_enable']
                    else:
                        switchport_enable = "null" 

                    if 'switchport_mode' in self.learned_interface[interface]:
                        switchport_mode =  self.learned_interface[interface]['switchport_mode']
                    else:
                        switchport_mode = "null" 

                    if 'interface_type' in self.learned_interface[interface]:
                        interface_type =  self.learned_interface[interface]['type']
                    else:
                        interface_type = "null"                     

                    if 'bandwidth' in self.learned_interface[interface]:
                        bandwidth =  self.learned_interface[interface]['bandwidth']
                    else:
                        bandwidth = "null"

                    if 'auto_negotiate' in self.learned_interface[interface]:
                        auto_negotiate =  self.learned_interface[interface]['auto_negotiate']
                    else:
                        auto_negotiate = "null"

                    if 'port_speed' in self.learned_interface[interface]:
                        speed =  self.learned_interface[interface]['port_speed']
                    else:
                        speed = "null"

                    if 'duplex_mode' in self.learned_interface[interface]:
                        duplex =  self.learned_interface[interface]['duplex_mode']
                    else:
                        duplex = "null"

                    if 'mtu' in self.learned_interface[interface]:
                        mtu =  self.learned_interface[interface]['mtu']
                    else:
                        mtu = "null"

                    if 'mac_address' in self.learned_interface[interface]:
                        mac_address =  self.learned_interface[interface]['mac_address']
                    else:
                        mac_address = "null"

                    if 'phys_address' in self.learned_interface[interface]:
                        physical_address =  self.learned_interface[interface]['phys_address']
                    else:
                        physical_address = "null"

                    if 'ipv4' in self.learned_interface[interface]:
                        for ip_address in self.learned_interface[interface]['ipv4']:
                            ip_address = ip_address
                    else:
                        ip_address = "null"

                    if 'medium' in self.learned_interface[interface]:
                        medium =  self.learned_interface[interface]['medium']
                    else:
                        medium = "null"

                    if 'delay' in self.learned_interface[interface]:
                        delay =  self.learned_interface[interface]['delay']
                    else:
                        delay = "null"

                    if 'encapsulation' in self.learned_interface[interface]:
                        encapsulation =  self.learned_interface[interface]['encapsulation']['encapsulation']
                    else:
                        encapsulation = "null"

                    if 'flow_control' in self.learned_interface[interface]:
                        flow_control_receive =  self.learned_interface[interface]['flow_control']['receive']
                        flow_control_send =  self.learned_interface[interface]['flow_control']['send']
                    else:
                        flow_control_receive = "null"
                        flow_control_send = "null"

                    if 'port_channel' in self.learned_interface[interface]:
                        if 'port_channel_int' in self.learned_interface[interface]['port_channel']:
                            port_channel_int = self.learned_interface[interface]['port_channel']['port_channel_int']
                        else:
                            port_channel_int = "null"
                        
                        if 'port_channel_member_intfs' in self.learned_interface[interface]['port_channel']:
                            port_channel_member_intfs = self.learned_interface[interface]['port_channel']['port_channel_member_intfs']
                        else:
                            port_channel_member_intfs = "null"

                        if 'port_channel_member' in self.learned_interface[interface]['port_channel']:
                            port_channel_member = self.learned_interface[interface]['port_channel']['port_channel_member']
                        else:
                            port_channel_member = "null"
                    else:
                        port_channel_int = "null"
                        port_channel_member_intfs = "null"
                        port_channel_member = "null"

                    if 'last_change' in self.learned_interface[interface]:
                        last_change =  self.learned_interface[interface]['last_change']
                    else:
                        last_change = "null"

                    if 'counters' in self.learned_interface[interface]:
                        if 'in_broadcast_pkts' in self.learned_interface[interface]['counters']:
                            in_broadcast_pkts = self.learned_interface[interface]['counters']['in_broadcast_pkts']
                        else:
                            in_broadcast_pkts = "null"

                        if 'in_crc_errors' in self.learned_interface[interface]['counters']:
                            in_crc_errors = self.learned_interface[interface]['counters']['in_crc_errors']
                        else: 
                            in_crc_errors = "null"

                        if 'in_errors' in self.learned_interface[interface]['counters']:
                            in_errors = self.learned_interface[interface]['counters']['in_errors']
                        else: 
                            in_errors = "null"

                        if 'in_mac_pause_frames' in self.learned_interface[interface]['counters']:
                            in_mac_pause_frames = self.learned_interface[interface]['counters']['in_mac_pause_frames']
                        else: 
                            in_mac_pause_frames = "null"

                        if 'in_multicast_pkts' in self.learned_interface[interface]['counters']:
                            in_multicast_pkts = self.learned_interface[interface]['counters']['in_multicast_pkts']
                        else: 
                            in_multicast_pkts = "null"

                        if 'in_octets' in self.learned_interface[interface]['counters']:
                            in_octets = self.learned_interface[interface]['counters']['in_octets']
                        else: 
                            in_octets = "null"

                        if 'in_unicast_pkts' in self.learned_interface[interface]['counters']:
                            in_unicast_pkts = self.learned_interface[interface]['counters']['in_unicast_pkts']
                        else: 
                            in_unicast_pkts = "null"

                        if 'in_unknown_protos' in self.learned_interface[interface]['counters']:
                            in_unknown_protos = self.learned_interface[interface]['counters']['in_unknown_protos']
                        else: 
                            in_unknown_protos = "null"

                        if 'in_pkts' in self.learned_interface[interface]['counters']:
                            in_pkts = self.learned_interface[interface]['counters']['in_pkts']
                        else: 
                            in_pkts = "null"

                        if 'out_broadcast_pkts' in self.learned_interface[interface]['counters']:
                            out_broadcast_pkts = self.learned_interface[interface]['counters']['out_broadcast_pkts']
                        else: 
                            out_broadcast_pkts = "null"

                        if 'out_discard' in self.learned_interface[interface]['counters']:
                            out_discard = self.learned_interface[interface]['counters']['out_discard']
                        else: 
                            out_discard = "null"

                        if 'out_errors' in self.learned_interface[interface]['counters']:
                            out_errors = self.learned_interface[interface]['counters']['out_errors']
                        else: 
                            out_errors = "null"

                        if 'out_mac_pause_frames' in self.learned_interface[interface]['counters']:
                            out_mac_pause_frames = self.learned_interface[interface]['counters']['out_mac_pause_frames']
                        else: 
                            out_mac_pause_frames = "null"

                        if 'out_multicast_pkts' in self.learned_interface[interface]['counters']:
                            out_multicast_pkts = self.learned_interface[interface]['counters']['out_multicast_pkts']
                        else: 
                            out_multicast_pkts = "null"

                        if 'out_unicast_pkts' in self.learned_interface[interface]['counters']:
                            out_unicast_pkts = self.learned_interface[interface]['counters']['out_unicast_pkts']
                        else: 
                            out_unicast_pkts = "null"

                        if 'out_pkts' in self.learned_interface[interface]['counters']:
                            out_pkts = self.learned_interface[interface]['counters']['out_pkts']
                        else: 
                            out_pkts = "null"

                        if 'last_clear' in self.learned_interface[interface]['counters']:
                            last_clear = self.learned_interface[interface]['counters']['last_clear']
                        else: 
                            last_clear = "null"

                    else:
                        in_broadcast_pkts = "null"
                        in_crc_errors = "null"
                        in_errors = "null"
                        in_mac_pause_frames = "null"
                        in_multicast_pkts = "null"
                        in_octets = "null"
                        in_unicast_pkts = "null"
                        in_unknown_protos = "null"
                        in_pkts = "null"
                        out_broadcast_pkts = "null"
                        out_discard = "null"
                        out_errors = "null"
                        out_mac_pause_frames = "null"
                        out_multicast_pkts = "null"
                        out_unicast_pkts = "null"
                        out_pkts = "null"
                        last_clear = "null"

                    if 'rate' in self.learned_interface[interface]:
                        input_rate =  self.learned_interface[interface]['rate']['in_rate']
                        load_interval = self.learned_interface[interface]['rate']['load_interval']
                        output_rate = self.learned_interface[interface]['rate']['out_rate']
                    else:
                        input_rate = "null"
                        load_interval = "null"
                        output_rate = "null"

                    learnInterface=LearnInterface(pyats_alias=device.alias,os=device.os,interface=interface,description=description,enabled=enabled,status=oper_status,access_vlan=access_vlan,native_vlan=native_vlan,switchport=switchport_enable,switchport_mode=switchport_mode,interface_type=interface_type,bandwidth=bandwidth,auto_negotiate=auto_negotiate,speed=speed,duplex=duplex,mtu=mtu,mac_address=mac_address,physical_address=physical_address,ip_address=ip_address,medium=medium,delay=delay,encapsulation=encapsulation,flow_control_receive=flow_control_receive,flow_control_send=flow_control_send,port_channel=port_channel_int,port_channel_member_interfaces=port_channel_member_intfs,port_channel_member=port_channel_member,last_change=last_change,input_broadcast=in_broadcast_pkts,input_crc_errors=in_crc_errors,input_errors=in_errors,input_mac_pause_frames=in_mac_pause_frames,input_multicast=in_multicast_pkts,input_octets=in_octets,input_unicast=in_unicast_pkts,input_unknown=in_unknown_protos,input_total=in_pkts,output_broadcast=out_broadcast_pkts,output_discard=out_discard,output_errors=out_errors,output_mac_pause_frames=out_mac_pause_frames,output_multicast=out_multicast_pkts,output_unicast=out_unicast_pkts,output_total=out_pkts,last_clear=last_clear,input_rate=input_rate,load_interval=load_interval,output_rate=output_rate,timestamp=datetime.now().replace(microsecond=0))
                    learnInterface.save()