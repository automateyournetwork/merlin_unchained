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
from general_functionalities import ParseShowCommandFunction, ParseLearnFunction
from datetime import datetime
from merlin.models import LearnACL, LearnARP, LearnARPStatistics, LearnVLAN, LearnVRF, ShowInventory, ShowIPIntBrief, ShowVersion

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
            # Learn ACL to JSON
            self.learned_acl = ParseLearnFunction.parse_learn(steps, device, "acl")
            if self.learned_acl is not None:
                # Set Django Database values from pyATS JSON
                # Layer 3 ACL Matches
                for acl in self.learned_acl['acls']:
                    if 'aces' in self.learned_acl['acls'][acl]:
                        for ace in self.learned_acl['acls'][acl]['aces']:
                            if 'l3' in self.learned_acl['acls'][acl]['aces'][ace]['matches']:
                                if 'ipv4' in self.learned_acl['acls'][acl]['aces'][ace]['matches']['l3']:
                                    if 'source_network' in self.learned_acl['acls'][acl]['aces'][ace]['matches']['l3']['ipv4']:
                                        for source_network in self.learned_acl['acls'][acl]['aces'][ace]['matches']['l3']['ipv4']['source_network']:
                                            learnACL=LearnACL(pyats_alias=device.alias,os=device.os,acl=acl,ace=ace,permission=self.learned_acl['acls'][acl]['aces'][ace]['actions']['forwarding'],logging=self.learned_acl['acls'][acl]['aces'][ace]['actions']['logging'],source_network=source_network,destination_network=self.learned_acl['acls'][acl]['aces'][ace]['matches']['l3']['ipv4']['destination_network'],l3_protocol=self.learned_acl['acls'][acl]['aces'][ace]['matches']['l3']['ipv4']['protocol'],l4_protocol="null",operator="null",port="null",timestamp=datetime.now().replace(microsecond=0))
                    else:
                        learnACL=LearnACL(pyats_alias=device.alias,os=device.os,acl=acl,ace="null",permission="null",logging="null",source_network="null",destination_network="null",l3_protocol="null",l4_protocol="null",operator="null",port="null",timestamp=datetime.now().replace(microsecond=0))
                    
                    #Write to the DB    
                    learnACL.save()

                #Layer 4 ACL Matches
                for acl in self.learned_acl['acls']:
                    if 'aces' in self.learned_acl['acls'][acl]:
                        for ace in self.learned_acl['acls'][acl]['aces']:
                            if 'l4' in self.learned_acl['acls'][acl]['aces'][ace]['matches']:
                                if 'udp' in self.learned_acl['acls'][acl]['aces'][ace]['matches']['l4']:
                                    if 'source_port' in self.learned_acl['acls'][acl]['aces'][ace]['matches']['l4']['udp']:
                                        learnACL=LearnACL(pyats_alias=device.alias,os=device.os,acl=acl,ace=ace,permission=self.learned_acl['acls'][acl]['aces'][ace]['actions']['forwarding'],logging=self.learned_acl['acls'][acl]['aces'][ace]['actions']['logging'],source_network="source protocol",destination_network="null",l3_protocol="null",l4_protocol="udp",operator=self.learned_acl['acls'][acl]['aces'][ace]['matches']['l4']['udp']['source_port']['operator']['operator'],port=self.learned_acl['acls'][acl]['aces'][ace]['matches']['l4']['udp']['source_port']['operator']['port'],timestamp=datetime.now().replace(microsecond=0))
                                    elif 'destination_port' in self.learned_acl['acls'][acl]['aces'][ace]['matches']['l4']['udp']:
                                        learnACL=LearnACL(pyats_alias=device.alias,os=device.os,acl=acl,ace=ace,permission=self.learned_acl['acls'][acl]['aces'][ace]['actions']['forwarding'],logging=self.learned_acl['acls'][acl]['aces'][ace]['actions']['logging'],source_network="null",destination_network="destination protocol",l3_protocol="null",l4_protocol="udp",operator=self.learned_acl['acls'][acl]['aces'][ace]['matches']['l4']['udp']['destination_port']['operator']['operator'],port=self.learned_acl['acls'][acl]['aces'][ace]['matches']['l4']['udp']['destination_port']['operator']['port'],timestamp=datetime.now().replace(microsecond=0))
                                elif 'tcp' in self.learned_acl['acls'][acl]['aces'][ace]['matches']['l4']:
                                    if 'source_port' in self.learned_acl['acls'][acl]['aces'][ace]['matches']['l4']['tcp']:
                                        learnACL=LearnACL(pyats_alias=device.alias,os=device.os,acl=acl,ace=ace,permission=self.learned_acl['acls'][acl]['aces'][ace]['actions']['forwarding'],logging=self.learned_acl['acls'][acl]['aces'][ace]['actions']['logging'],source_network="source protocol",destination_network="null",l3_protocol="null",l4_protocol="tcp",operator=self.learned_acl['acls'][acl]['aces'][ace]['matches']['l4']['tcp']['source_port']['operator']['operator'],port=self.learned_acl['acls'][acl]['aces'][ace]['matches']['l4']['tcp']['source_port']['operator']['port'],timestamp=datetime.now().replace(microsecond=0))
                                    elif 'destination_port' in self.learned_acl['acls'][acl]['aces'][ace]['matches']['l4']['tcp']:
                                        if 'logging' in self.learned_acl['acls'][acl]['aces'][ace]['actions']:
                                            learnACL=LearnACL(pyats_alias=device.alias,os=device.os,acl=acl,ace=ace,permission=self.learned_acl['acls'][acl]['aces'][ace]['actions']['forwarding'],logging=self.learned_acl['acls'][acl]['aces'][ace]['actions']['logging'],source_network="null",destination_network="destination protocol",l3_protocol="null",l4_protocol="tcp",operator=self.learned_acl['acls'][acl]['aces'][ace]['matches']['l4']['tcp']['destination_port']['operator']['operator'],port=self.learned_acl['acls'][acl]['aces'][ace]['matches']['l4']['tcp']['destination_port']['operator']['port'],timestamp=datetime.now().replace(microsecond=0))
                                        else:
                                            learnACL=LearnACL(pyats_alias=device.alias,os=device.os,acl=acl,ace=ace,permission=self.learned_acl['acls'][acl]['aces'][ace]['actions']['forwarding'],logging="null",source_network="null",destination_network="destination protocol",l3_protocol="null",l4_protocol="tcp",operator=self.learned_acl['acls'][acl]['aces'][ace]['matches']['l4']['tcp']['destination_port']['operator']['operator'],port=self.learned_acl['acls'][acl]['aces'][ace]['matches']['l4']['tcp']['destination_port']['operator']['port'],timestamp=datetime.now().replace(microsecond=0))
                    else:
                        learnACL=LearnACL(pyats_alias=device.alias,os=device.os,acl=acl,ace="null",permission="null",logging="null",source_network="null",destination_network="null",l3_protocol="null",l4_protocol="null",operator="null",port="null",timestamp=datetime.now().replace(microsecond=0))
                    
                    #Write to the DB
                    learnACL.save()

            # Learn ARP to JSON
            self.learned_arp = ParseLearnFunction.parse_learn(steps, device, "arp")
            if self.learned_arp is not None:
                # Set Django Database values from pyATS JSON
                for interface in self.learned_arp['interfaces']:
                    if 'ipv4' in self.learned_arp['interfaces']:
                        for neighbor in self.learned_arp['interfaces'][interface]['ipv4']['neighbors']:
                            learnARP=LearnARP(pyats_alias=device.alias,os=device.os,interface=interface,neighbor_ip=neighbor,neighbor_mac=self.learned_arp['interfaces'][interface]['ipv4']['neighbors'][neighbor]['link_layer_address'],origin=self.learned_arp['interfaces'][interface]['ipv4']['neighbors'][neighbor]['origin'],local_proxy=self.learned_arp['interfaces'][interface]['arp_dynamic_learning']['local_proxy_enable'],proxy=self.learned_arp['interfaces'][interface]['arp_dynamic_learning']['proxy_enable'],timestamp=datetime.now().replace(microsecond=0))
                    else:
                            learnARP=LearnARP(pyats_alias=device.alias,os=device.os,interface=interface,neighbor_ip="null",neighbor_mac="null",origin="null",local_proxy=self.learned_arp['interfaces'][interface]['arp_dynamic_learning']['local_proxy_enable'],proxy=self.learned_arp['interfaces'][interface]['arp_dynamic_learning']['proxy_enable'],timestamp=datetime.now().replace(microsecond=0))
                    learnARP.save()
                
                learnARPStatistics = LearnARPStatistics(pyats_alias=device.alias,os=device.os,entries_total=self.learned_arp['statistics']['entries_total'],in_drops=self.learned_arp['statistics']['in_drops'],in_replies_pkts=self.learned_arp['statistics']['in_replies_pkts'],in_requests_pkts=self.learned_arp['statistics']['in_requests_pkts'],incomplete_total=self.learned_arp['statistics']['incomplete_total'],out_replies_pkts=self.learned_arp['statistics']['out_replies_pkts'],out_requests_pkts=self.learned_arp['statistics']['out_requests_pkts'],timestamp=datetime.now().replace(microsecond=0))
                learnARPStatistics.save()

            # Learn VLAN to JSON
            self.learned_vlan = ParseLearnFunction.parse_learn(steps, device, "vlan")
            if self.learned_vlan is not None:
                # Set Django Database values from pyATS JSON
                for vlan in self.learned_vlan['vlans']:
                    if vlan != "configuration" and vlan !="interface_vlan_enabled" and vlan !="vn_segment_vlan_based_enabled":
                        if 'interfaces' in self.learned_vlan['vlans'][vlan]:                           
                            learnVLAN=LearnVLAN(pyats_alias=device.alias,os=device.os,vlan=vlan,interfaces=self.learned_vlan['vlans'][vlan]['interfaces'],mode=self.learned_vlan['vlans'][vlan]['mode'],name=self.learned_vlan['vlans'][vlan]['name'],shutdown=self.learned_vlan['vlans'][vlan]['shutdown'],state=self.learned_vlan['vlans'][vlan]['state'],timestamp=datetime.now().replace(microsecond=0))
                        else:
                            learnVLAN=LearnVLAN(pyats_alias=device.alias,os=device.os,vlan=vlan,interfaces="null",mode=self.learned_vlan['vlans'][vlan]['mode'],name=self.learned_vlan['vlans'][vlan]['name'],shutdown=self.learned_vlan['vlans'][vlan]['shutdown'],state=self.learned_vlan['vlans'][vlan]['state'],timestamp=datetime.now().replace(microsecond=0))

                        learnVLAN.save()

            # Learn VRF to JSON
            self.learned_vrf = ParseLearnFunction.parse_learn(steps, device, "vrf")            
            if self.learned_vrf is not None:
                # Set Django Database values from pyATS JSON
                for vrf in self.learned_vrf['vrfs']:
                    learnVRF=LearnVRF(pyats_alias=device.alias,os=device.os,vrf=vrf,address_family_ipv4=self.learned_vrf['vrfs'][vrf]['address_family']['ipv4'],address_family_ipv6=self.learned_vrf['vrfs'][vrf]['address_family']['ipv6'],route_distinguisher=self.learned_vrf['vrfs'][vrf]['route_distinguisher'],timestamp=datetime.now().replace(microsecond=0))
                # Save the objects into the database.
                    learnVRF.save()

            # Show Inventory to JSON
            self.parsed_show_inventory=ParseShowCommandFunction.parse_show_command(steps, device, "show inventory")
            if self.parsed_show_inventory is not None:
                for part in self.parsed_show_inventory['name']:
                    # Set Django Database values from pyATS JSON
                    showInventory=ShowInventory(pyats_alias=device.alias,os=device.os,part=part,description=self.parsed_show_inventory['name'][part]['description'],pid=self.parsed_show_inventory['name'][part]['pid'],serial_number=self.parsed_show_inventory['name'][part]['serial_number'],timestamp=datetime.now().replace(microsecond=0))
                    # Save the objects into the database.
                    showInventory.save()

            # Show IP Int Brief to JSON
            self.parsed_show_ip_brief=ParseShowCommandFunction.parse_show_command(steps, device, "show ip interface brief")
            if self.parsed_show_ip_brief is not None:
                # Set Django Database values from pyATS JSON
                for interface in self.parsed_show_ip_brief['interface']:
                    if "Vlan" in interface:
                        for vlan in self.parsed_show_ip_brief['interface'][interface]['vlan_id']:
                            showIPIntBrief=ShowIPIntBrief(pyats_alias=device.alias,os=device.os,interface=interface,interface_status=self.parsed_show_ip_brief['interface'][interface]['vlan_id'][vlan]['interface_status'],ip_address=self.parsed_show_ip_brief['interface'][interface]['vlan_id'][vlan]['ip_address'],timestamp=datetime.now().replace(microsecond=0))
                    else:
                        showIPIntBrief=ShowIPIntBrief(pyats_alias=device.alias,os=device.os,interface=interface,interface_status=self.parsed_show_ip_brief['interface'][interface]['interface_status'],ip_address=self.parsed_show_ip_brief['interface'][interface]['ip_address'],timestamp=datetime.now().replace(microsecond=0))
                        # Save the objects into the database.
                        
                    showIPIntBrief.save()

            # Show Version to JSON
            self.parsed_show_version=ParseShowCommandFunction.parse_show_command(steps, device, "show version")
            if self.parsed_show_version is not None:
                # Set Django Database values from pyATS JSON
                if device.os == "nxos":
                    showVersion=ShowVersion(pyats_alias=device.alias,bootflash=self.parsed_show_version['platform']['hardware']['bootflash'],chassis=self.parsed_show_version['platform']['hardware']['chassis'],cpu=self.parsed_show_version['platform']['hardware']['cpu'],device_name=self.parsed_show_version['platform']['hardware']['device_name'],memory=self.parsed_show_version['platform']['hardware']['memory'],model=self.parsed_show_version['platform']['hardware']['model'],processor_board_id=self.parsed_show_version['platform']['hardware']['processor_board_id'],rp=self.parsed_show_version['platform']['hardware']['rp'],slots=self.parsed_show_version['platform']['hardware']['slots'],name=self.parsed_show_version['platform']['name'],os=device.os,reason=self.parsed_show_version['platform']['reason'],days=self.parsed_show_version['platform']['kernel_uptime']['days'],hours=self.parsed_show_version['platform']['kernel_uptime']['hours'],minutes=self.parsed_show_version['platform']['kernel_uptime']['minutes'],seconds=self.parsed_show_version['platform']['kernel_uptime']['seconds'],system_compile_time=self.parsed_show_version['platform']['software']['system_compile_time'],system_image_file=self.parsed_show_version['platform']['software']['system_image_file'],system_version=self.parsed_show_version['platform']['software']['system_version'],chassis_sn="null",compiled_by="null",curr_config_register="null",image_id="null",image_type="null",label="null",license_level="null",license_type="null",non_volatile="null",physical="null",next_reload_license_level="null",platform="null",processor_type="null",returned_to_rom_by="null",rom="null",rtr_type="null",uptime="null",uptime_this_cp="null",version_short="null",xe_version="null",timestamp=datetime.now().replace(microsecond=0))
                elif device.os == "iosxe":
                    showVersion=ShowVersion(pyats_alias=device.alias,bootflash=self.parsed_show_version['version']['system_image'],chassis=self.parsed_show_version['version']['chassis'],cpu="null",device_name=self.parsed_show_version['version']['hostname'],memory=self.parsed_show_version['version']['main_mem'],model=self.parsed_show_version['version']['platform'],processor_board_id="null",rp="null",slots="null",name="null",os=device.os,reason=self.parsed_show_version['version']['last_reload_reason'],days="null",hours="null",minutes="null",seconds="null",system_compile_time=self.parsed_show_version['version']['compiled_date'],system_image_file=self.parsed_show_version['version']['system_image'],system_version=self.parsed_show_version['version']['version'],chassis_sn=self.parsed_show_version['version']['chassis_sn'],compiled_by=self.parsed_show_version['version']['compiled_by'],curr_config_register=self.parsed_show_version['version']['curr_config_register'],image_id=self.parsed_show_version['version']['image_id'],image_type=self.parsed_show_version['version']['image_type'],label=self.parsed_show_version['version']['label'],license_level=self.parsed_show_version['version']['license_level'],license_type=self.parsed_show_version['version']['license_type'],non_volatile=self.parsed_show_version['version']['mem_size']['non-volatile configuration'],physical=self.parsed_show_version['version']['mem_size']['physical'],next_reload_license_level=self.parsed_show_version['version']['next_reload_license_level'],platform=self.parsed_show_version['version']['platform'],processor_type=self.parsed_show_version['version']['processor_type'],returned_to_rom_by=self.parsed_show_version['version']['returned_to_rom_by'],rom=self.parsed_show_version['version']['rom'],rtr_type=self.parsed_show_version['version']['rtr_type'],uptime=self.parsed_show_version['version']['uptime'],uptime_this_cp=self.parsed_show_version['version']['uptime_this_cp'],version_short=self.parsed_show_version['version']['version_short'],xe_version=self.parsed_show_version['version']['xe_version'],timestamp=datetime.now().replace(microsecond=0))
                # Save the objects into the database.
                showVersion.save()