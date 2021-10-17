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
from general_functionalities import ParseShowCommandFunction, ParseLearnFunction, ParseConfigFunction, ParseDictFunction
from datetime import datetime
from merlin.models import EoXCredentials, EoX_PID, EoX_SN, EoX_IOS, LearnACL, LearnARP, LearnARPStatistics, LearnBGPInstances, LearnBGPRoutesPerPeer, LearnBGPTables, LearnConfig, LearnInterface, LearnPlatform, LearnPlatformSlots, LearnPlatformVirtual, LearnVLAN, LearnVRF, RecommendedReleaseCredentials, RecommendedRelease, Serial2ContractCredentials, Serial2Contract, PSIRTCredentials, PSIRT, ShowInventory, ShowIPIntBrief, ShowVersion 
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
        for device in testbed.devices.values():
            # EoX - PID
            # Show Inventory to JSON
            self.parsed_show_inventory=ParseShowCommandFunction.parse_show_command(steps, device, "show inventory")
            with steps.start('Store data',continue_=True) as step:

                # Get OAuth Token
                if hasattr(self, 'parsed_show_inventory'):
                    db_key = EoXCredentials.objects.all().values('key')
                    db_user = EoXCredentials.objects.all().values('client_secret')
                    eox_pid_api_username = db_key[0]['key']
                    eox_pid_api_password = db_user[0]['client_secret']

                    oauth_token_raw = requests.post("https://cloudsso.cisco.com/as/token.oauth2?grant_type=client_credentials&client_id=%s&client_secret=%s" % (eox_pid_api_username,eox_pid_api_password))
                    oauth_token_json = oauth_token_raw.json()
                    oauth_headers = {"Authorization": "%s %s" % (oauth_token_json['token_type'],oauth_token_json['access_token'])}

                # Go Get Recommended Release using chassis PID and Oauth token
                if device.os == "nxos":
                    if "N9K-C9500v" in self.parsed_show_inventory['name']['Chassis']['pid']:
                        pid = "N9K-C93180LC-EX"
                    else:
                        pid = self.parsed_show_inventory['name']['Chassis']['pid']
                    with steps.start('Calling API',continue_=True) as step:
                        try:
                            eox_pid_raw = requests.get("https://api.cisco.com/supporttools/eox/rest/5/EOXByProductID/%s" % pid, headers=oauth_headers)
                            eox_pid_json = eox_pid_raw.json()
                        except Exception as e:
                            step.failed('Could not parse it correctly\n{e}'.format(e=e))                           
                        
                        if "EndOfSecurityVulSupportDate" in eox_pid_json:
                            security=pid['EndOfSecurityVulSupportDate']['value']
                        else:
                            security="2000-01-01"

                        for pid in eox_pid_json['EOXRecord']:
                            if "EOXError" not in pid:                                
                                eox_pid = EoX_PID(pyats_alias=device.alias,os=device.os,pid=pid['EOLProductID'],description=pid['ProductIDDescription'],bulletin_number=pid['ProductBulletinNumber'],bulletin_url=pid['LinkToProductBulletinURL'],external_date=pid['EOXExternalAnnouncementDate']['value'],sale_date=pid['EndOfSaleDate']['value'],sw_maintenance=pid['EndOfSWMaintenanceReleases']['value'],security=security,routine_failure=pid['EndOfRoutineFailureAnalysisDate']['value'],service_contract=pid['EndOfServiceContractRenewal']['value'],last=pid['LastDateOfSupport']['value'],svc_attach=pid['EndOfSvcAttachDate']['value'],last_updated=pid['UpdatedTimeStamp']['value'],pid_active=pid['EOXMigrationDetails']['PIDActiveFlag'],migration_information=pid['EOXMigrationDetails']['MigrationInformation'],migration_option=pid['EOXMigrationDetails']['MigrationOption'],migration_pid=pid['EOXMigrationDetails']['MigrationProductId'],migration_name=pid['EOXMigrationDetails']['MigrationProductName'],migration_strat=pid['EOXMigrationDetails']['MigrationStrategy'],migration_url=pid['EOXMigrationDetails']['MigrationProductInfoURL'],timestamp=datetime.now().replace(microsecond=0))
                                eox_pid.save()
                elif device.os == "iosxe":
                    if device.type == "Catalyst 9300":
                        for slot,value01 in self.parsed_show_inventory['slot'].items():
                            for pid,value02 in value01.items():                                                            
                                for part,value03 in value02.items():
                                    pid = value03['pid']
                                    with steps.start('Calling API',continue_=True) as step:
                                        try:
                                            eox_pid_raw = requests.get("https://api.cisco.com/supporttools/eox/rest/5/EOXByProductID/%s" % pid, headers=oauth_headers)
                                            eox_pid_json = eox_pid_raw.json()
                                        except Exception as e:
                                            step.failed('Could not parse it correctly\n{e}'.format(e=e))                           

                                        if "EndOfSecurityVulSupportDate" in eox_pid_json:
                                            security=pid['EndOfSecurityVulSupportDate']['value']
                                        else:
                                            security="2000-01-01"

                                        for pid in eox_pid_json['EOXRecord']:
                                            if "EOXError" not in pid:
                                                eox_pid = EoX_PID(pyats_alias=device.alias,os=device.os,pid=pid['EOLProductID'],description=pid['ProductIDDescription'],bulletin_number=pid['ProductBulletinNumber'],bulletin_url=pid['LinkToProductBulletinURL'],external_date=pid['EOXExternalAnnouncementDate']['value'],sale_date=pid['EndOfSaleDate']['value'],sw_maintenance=pid['EndOfSWMaintenanceReleases']['value'],security=security,routine_failure=pid['EndOfRoutineFailureAnalysisDate']['value'],service_contract=pid['EndOfServiceContractRenewal']['value'],last=pid['LastDateOfSupport']['value'],svc_attach=pid['EndOfSvcAttachDate']['value'],last_updated=pid['UpdatedTimeStamp']['value'],pid_active=pid['EOXMigrationDetails']['PIDActiveFlag'],migration_information=pid['EOXMigrationDetails']['MigrationInformation'],migration_option=pid['EOXMigrationDetails']['MigrationOption'],migration_pid=pid['EOXMigrationDetails']['MigrationProductId'],migration_name=pid['EOXMigrationDetails']['MigrationProductName'],migration_strat=pid['EOXMigrationDetails']['MigrationStrategy'],migration_url=pid['EOXMigrationDetails']['MigrationProductInfoURL'],timestamp=datetime.now().replace(microsecond=0))
                                                eox_pid.save() 
            
            # EoX - SN
            # Show Inventory to JSON
            self.parsed_show_inventory=ParseShowCommandFunction.parse_show_command(steps, device, "show inventory")
            with steps.start('Store data',continue_=True) as step:

                # Get OAuth Token
                if hasattr(self, 'parsed_show_inventory'):
                    db_key = EoXCredentials.objects.all().values('key')
                    db_user = EoXCredentials.objects.all().values('client_secret')
                    eox_sn_api_username = db_key[0]['key']
                    eox_sn_api_password = db_user[0]['client_secret']

                    oauth_token_raw = requests.post("https://cloudsso.cisco.com/as/token.oauth2?grant_type=client_credentials&client_id=%s&client_secret=%s" % (eox_sn_api_username,eox_sn_api_password))
                    oauth_token_json = oauth_token_raw.json()
                    oauth_headers = {"Authorization": "%s %s" % (oauth_token_json['token_type'],oauth_token_json['access_token'])}

                # Go Get Recommended Release using chassis PID and Oauth token
                if device.os == "nxos":
                    for part,value in self.parsed_show_inventory.items():
                        for pid,value01 in value.items():
                                sn = value01['serial_number']
                                with steps.start('Calling API',continue_=True) as step:
                                    try:
                                        eox_sn_raw = requests.get("https://api.cisco.com/supporttools/eox/rest/5/EOXBySerialNumber/%s" % sn, headers=oauth_headers)
                                        eox_sn_json = eox_sn_raw.json()
                                    except Exception as e:
                                        step.failed('Could not parse it correctly\n{e}'.format(e=e))                           
                                    
                                    if "EndOfSecurityVulSupportDate" in eox_sn_json:
                                        security=pid['EndOfSecurityVulSupportDate']['value']
                                    else:
                                        security="2000-01-01"
                                
                                    for pid in eox_sn_json['EOXRecord']:
                                        if "EOXError" not in pid:
                                            eox_sn = EoX_SN(pyats_alias=device.alias,os=device.os,pid=pid['EOLProductID'],description=pid['ProductIDDescription'],bulletin_number=pid['ProductBulletinNumber'],bulletin_url=pid['LinkToProductBulletinURL'],external_date=pid['EOXExternalAnnouncementDate']['value'],sale_date=pid['EndOfSaleDate']['value'],sw_maintenance=pid['EndOfSWMaintenanceReleases']['value'],security=security,routine_failure=pid['EndOfRoutineFailureAnalysisDate']['value'],service_contract=pid['EndOfServiceContractRenewal']['value'],last=pid['LastDateOfSupport']['value'],svc_attach=pid['EndOfSvcAttachDate']['value'],last_updated=pid['UpdatedTimeStamp']['value'],pid_active=pid['EOXMigrationDetails']['PIDActiveFlag'],migration_information=pid['EOXMigrationDetails']['MigrationInformation'],migration_option=pid['EOXMigrationDetails']['MigrationOption'],migration_pid=pid['EOXMigrationDetails']['MigrationProductId'],migration_name=pid['EOXMigrationDetails']['MigrationProductName'],migration_strat=pid['EOXMigrationDetails']['MigrationStrategy'],migration_url=pid['EOXMigrationDetails']['MigrationProductInfoURL'],timestamp=datetime.now().replace(microsecond=0))
                                            eox_sn.save()
            # EoX - Software
            # Show Version to JSON
            self.parsed_show_version=ParseShowCommandFunction.parse_show_command(steps, device, "show version")
            
            with steps.start('Store data',continue_=True) as step:

                # Get OAuth Token
                if hasattr(self, 'parsed_show_version'):
                    db_key = EoXCredentials.objects.all().values('key')
                    db_user = EoXCredentials.objects.all().values('client_secret')
                    eox_sw_api_username = db_key[0]['key']
                    eox_sw_api_password = db_user[0]['client_secret']

                    oauth_token_raw = requests.post("https://cloudsso.cisco.com/as/token.oauth2?grant_type=client_credentials&client_id=%s&client_secret=%s" % (eox_sw_api_username,eox_sw_api_password))
                    oauth_token_json = oauth_token_raw.json()
                    oauth_headers = {"Authorization": "%s %s" % (oauth_token_json['token_type'],oauth_token_json['access_token'])}

                # Go Get Recommended Release using chassis PID and Oauth token
                if device.os == "nxos":
                    sw = self.parsed_show_version['platform']['software']['system_version']
                    with steps.start('Calling API',continue_=True) as step:
                        try:
                            eox_sw_raw = requests.get("https://api.cisco.com/supporttools/eox/rest/5/EOXBySWReleaseString/1?responseencoding=&input1=%s,%s" % (sw, device.os), headers=oauth_headers)
                            eox_sw_json = eox_sw_raw.json()
                        except Exception as e:
                            step.failed('Could not parse it correctly\n{e}'.format(e=e))                           
                                    
                    if "EndOfSecurityVulSupportDate" in eox_sw_json:
                        security=pid['EndOfSecurityVulSupportDate']['value']
                    else:
                        security="2000-01-01"

                    for pid in eox_sw_json['EOXRecord']:
                        if "EOXError" not in pid:
                            eox_sw = EoX_IOS(pyats_alias=device.alias,os=device.os,pid=pid['EOLProductID'],description=pid['ProductIDDescription'],bulletin_number=pid['ProductBulletinNumber'],bulletin_url=pid['LinkToProductBulletinURL'],external_date=pid['EOXExternalAnnouncementDate']['value'],sale_date=pid['EndOfSaleDate']['value'],sw_maintenance=pid['EndOfSWMaintenanceReleases']['value'],security=security,routine_failure=pid['EndOfRoutineFailureAnalysisDate']['value'],service_contract=pid['EndOfServiceContractRenewal']['value'],last=pid['LastDateOfSupport']['value'],svc_attach=pid['EndOfSvcAttachDate']['value'],last_updated=pid['UpdatedTimeStamp']['value'],pid_active=pid['EOXMigrationDetails']['PIDActiveFlag'],migration_information=pid['EOXMigrationDetails']['MigrationInformation'],migration_option=pid['EOXMigrationDetails']['MigrationOption'],migration_pid=pid['EOXMigrationDetails']['MigrationProductId'],migration_name=pid['EOXMigrationDetails']['MigrationProductName'],migration_strat=pid['EOXMigrationDetails']['MigrationStrategy'],migration_url=pid['EOXMigrationDetails']['MigrationProductInfoURL'],timestamp=datetime.now().replace(microsecond=0))
                            eox_sw.save()

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

            # Learn BGP to JSON
            with steps.start("Learning BGP", continue_=True) as step:
                try:
                    self.learned_bgp = device.learn("bgp")
                except Exception as e:
                    step.failed('Could not learn it correctly\n{e}'.format(e=e))
                    return None

                if self.learned_bgp.info is not None:
                    # Set Django Database values from pyATS JSON
                    for instance in self.learned_bgp.info['instance']:
                        for vrf in self.learned_bgp.info['instance'][instance]['vrf']:
                            for neighbor in self.learned_bgp.info['instance'][instance]['vrf'][vrf]['neighbor']:
                                learnBGPInstances=LearnBGPInstances(pyats_alias=device.alias,os=device.os,instance=instance,bgp_id=self.learned_bgp.info['instance'][instance]['bgp_id'],protocol_state=self.learned_bgp.info['instance'][instance]['protocol_state'],nexthop_trigger_delay_critical=self.learned_bgp.info['instance'][instance]['vrf'][vrf]['address_family']['ipv4 unicast']['nexthop_trigger_delay_critical'],nexthop_trigger_delay_noncritical=self.learned_bgp.info['instance'][instance]['vrf'][vrf]['address_family']['ipv4 unicast']['nexthop_trigger_delay_non_critical'],nexthop_trigger_enabled=self.learned_bgp.info['instance'][instance]['vrf'][vrf]['address_family']['ipv4 unicast']['nexthop_trigger_enable'],vrf=vrf,router_id=self.learned_bgp.info['instance'][instance]['vrf'][vrf]['router_id'],cluster_id=self.learned_bgp.info['instance'][instance]['vrf'][vrf]['cluster_id'],confederation_id=self.learned_bgp.info['instance'][instance]['vrf'][vrf]['confederation_identifier'],neighbor=neighbor,version=self.learned_bgp.info['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['bgp_version'],hold_time=self.learned_bgp.info['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['bgp_negotiated_keepalive_timers']['hold_time'],keep_alive_interval=self.learned_bgp.info['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['bgp_negotiated_keepalive_timers']['keepalive_interval'],local_as=self.learned_bgp.info['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['local_as_as_no'],remote_as=self.learned_bgp.info['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['remote_as'],neighbor_counters_received_bytes_in_queue=self.learned_bgp.info['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['bgp_neighbor_counters']['messages']['received']['bytes_in_queue'],neighbor_counters_received_capability=self.learned_bgp.info['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['bgp_neighbor_counters']['messages']['received']['capability'],neighbor_counters_received_keepalives=self.learned_bgp.info['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['bgp_neighbor_counters']['messages']['received']['keepalives'],neighbor_counters_received_notifications=self.learned_bgp.info['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['bgp_neighbor_counters']['messages']['received']['notifications'],neighbor_counters_received_opens=self.learned_bgp.info['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['bgp_neighbor_counters']['messages']['received']['opens'],neighbor_counters_received_route_refresh=self.learned_bgp.info['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['bgp_neighbor_counters']['messages']['received']['route_refresh'],neighbor_counters_received_total=self.learned_bgp.info['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['bgp_neighbor_counters']['messages']['received']['total'],neighbor_counters_received_total_bytes=self.learned_bgp.info['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['bgp_neighbor_counters']['messages']['received']['total_bytes'],neighbor_counters_received_updates=self.learned_bgp.info['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['bgp_neighbor_counters']['messages']['received']['updates'],neighbor_counters_sent_bytes_in_queue=self.learned_bgp.info['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['bgp_neighbor_counters']['messages']['sent']['bytes_in_queue'],neighbor_counters_sent_capability=self.learned_bgp.info['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['bgp_neighbor_counters']['messages']['sent']['capability'],neighbor_counters_sent_keepalives=self.learned_bgp.info['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['bgp_neighbor_counters']['messages']['sent']['keepalives'],neighbor_counters_sent_notifications=self.learned_bgp.info['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['bgp_neighbor_counters']['messages']['sent']['notifications'],neighbor_counters_sent_opens=self.learned_bgp.info['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['bgp_neighbor_counters']['messages']['sent']['opens'],neighbor_counters_sent_route_refresh=self.learned_bgp.info['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['bgp_neighbor_counters']['messages']['sent']['route_refresh'],neighbor_counters_sent_total=self.learned_bgp.info['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['bgp_neighbor_counters']['messages']['sent']['total'],neighbor_counters_sent_total_bytes=self.learned_bgp.info['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['bgp_neighbor_counters']['messages']['sent']['total_bytes'],neighbor_counters_sent_updates=self.learned_bgp.info['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['bgp_neighbor_counters']['messages']['sent']['updates'],last_reset=self.learned_bgp.info['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['bgp_session_transport']['connection']['last_reset'],reset_reason=self.learned_bgp.info['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['bgp_session_transport']['connection']['reset_reason'],timestamp=datetime.now().replace(microsecond=0))
                        learnBGPInstances.save()

                if self.learned_bgp.routes_per_peer is not None:
                    for instance in self.learned_bgp.routes_per_peer['instance']:
                        for vrf in self.learned_bgp.routes_per_peer['instance'][instance]['vrf']:
                            for neighbor in self.learned_bgp.routes_per_peer['instance'][instance]['vrf'][vrf]['neighbor']:
                                if self.learned_bgp.routes_per_peer['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['address_family']['ipv4 unicast']['advertised'] == {}:
                                    advertised="0"
                                else:
                                    advertised=self.learned_bgp.routes_per_peer['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['address_family']['ipv4 unicast']['advertised']

                                if self.learned_bgp.routes_per_peer['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['address_family']['ipv4 unicast']['routes'] == {}:
                                    routes="0"
                                else:
                                    routes=self.learned_bgp.routes_per_peer['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['address_family']['ipv4 unicast']['advertised']

                                learnBGPRoutesPerPeer = LearnBGPRoutesPerPeer(pyats_alias=device.alias,os=device.os,instance=instance,vrf=vrf,neighbor=neighbor,advertised=advertised,routes=routes,remote_as=self.learned_bgp.routes_per_peer['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['remote_as'],timestamp=datetime.now().replace(microsecond=0))
                                print (learnBGPRoutesPerPeer)
                        learnBGPRoutesPerPeer.save()
                        
                if self.learned_bgp.table is not None:
                    for instance in self.learned_bgp.table['instance']:
                        for vrf in self.learned_bgp.table['instance'][instance]['vrf']:
                            for prefix in self.learned_bgp.table['instance'][instance]['vrf'][vrf]['address_family']['ipv4 unicast']['prefixes']:
                                for index in self.learned_bgp.table['instance'][instance]['vrf'][vrf]['address_family']['ipv4 unicast']['prefixes'][prefix]['index']:
                                    learnBGPTables = LearnBGPTables(pyats_alias=device.alias,os=device.os,instance=instance,vrf=vrf,table_version=self.learned_bgp.table['instance'][instance]['vrf'][vrf]['address_family']['ipv4 unicast']['bgp_table_version'],prefix=prefix,index=index,localpref=self.learned_bgp.table['instance'][instance]['vrf'][vrf]['address_family']['ipv4 unicast']['prefixes'][prefix]['index'][index]['localpref'],next_hop=self.learned_bgp.table['instance'][instance]['vrf'][vrf]['address_family']['ipv4 unicast']['prefixes'][prefix]['index'][index]['next_hop'],origin_code=self.learned_bgp.table['instance'][instance]['vrf'][vrf]['address_family']['ipv4 unicast']['prefixes'][prefix]['index'][index]['origin_codes'],status_code=self.learned_bgp.table['instance'][instance]['vrf'][vrf]['address_family']['ipv4 unicast']['prefixes'][prefix]['index'][index]['status_codes'],weight=self.learned_bgp.table['instance'][instance]['vrf'][vrf]['address_family']['ipv4 unicast']['prefixes'][prefix]['index'][index]['weight'],timestamp=datetime.now().replace(microsecond=0))
                        learnBGPTables.save()

            # Learn Config to JSON
            self.learned_config = ParseConfigFunction.parse_learn(steps, device, "config")            
            if self.learned_config is not None:
                # Set Django Database values from pyATS JSON
                learnConfig=LearnConfig(pyats_alias=device.alias,os=device.os,config=self.learned_config,timestamp=datetime.now().replace(microsecond=0))
                # Save the objects into the database.
                learnConfig.save()

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

            # Learn Platform to JSON
            self.learned_platform = ParseDictFunction.parse_learn(steps, device, "platform")
            if self.learned_platform is not None:
                for slot in self.learned_platform['slot']:
                    for part in self.learned_platform['slot'][slot]:
                        slot = slot
                        slot_name = self.learned_platform['slot'][slot][part]['name']
                        slot_sn = self.learned_platform['slot'][slot][part]['sn']
                        slot_state = self.learned_platform['slot'][slot][part]['state']
                        if 'redundancy_state' in self.learned_platform['slot'][slot][part]:
                            slot_redundancy_state = self.learned_platform['slot'][slot][part]['redundancy_state']
                        else:
                            slot_redundancy_state = 'null'

                        if 'rp_boot_image' in self.learned_platform['slot'][slot][part]:
                            rp_boot_image = self.learned_platform['slot'][slot][part]['rp_boot_image']
                        else:
                            rp_boot_image = 'null'

                        if 'rp_uptime' in self.learned_platform['slot'][slot][part]:
                            rp_uptime = self.learned_platform['slot'][slot][part]['rp_uptime']
                        else:
                            rp_uptime = 'null'

                    # Set Django Database values from pyATS JSON
                    learnPlatformSlots=LearnPlatformSlots(pyats_alias=device.alias,os=device.os,slot=slot,slot_name=slot_name,slot_sn=slot_sn,slot_state=slot_state,slot_redundancy_state=slot_redundancy_state,rp_boot_image=rp_boot_image,slot_rp_uptime=rp_uptime,timestamp=datetime.now().replace(microsecond=0))

                    # Save the objects into the database.
                    learnPlatformSlots.save()

                for virtual_device in self.learned_platform['virtual_device']:
                    virtual_device_name = self.learned_platform['virtual_device'][virtual_device]['vd_name']
                    virtual_device_status = self.learned_platform['virtual_device'][virtual_device]['vd_status']
                    for member in self.learned_platform['virtual_device'][virtual_device]['membership']:
                        virtual_device_member = member
                        virtual_device_member_status = self.learned_platform['virtual_device'][virtual_device]['membership'][member]['status']
                        virtual_device_member_type = self.learned_platform['virtual_device'][virtual_device]['membership'][member]['type']
                
                        # Set Django Database values from pyATS JSON
                        learnPlatformVirtual=LearnPlatformVirtual(pyats_alias=device.alias,os=device.os,virtual_device_name=virtual_device_name,virtual_device_status=virtual_device_status,virtual_device_member=member,virtual_device_member_status=virtual_device_member_status,virtual_device_member_type=virtual_device_member_type,timestamp=datetime.now().replace(microsecond=0))

                        # Save the objects into the database.
                        learnPlatformVirtual.save()

                # Set Django Database values from pyATS JSON
                learnPlatform=LearnPlatform(pyats_alias=device.alias,os=device.os,chassis=self.learned_platform['chassis'],chassis_sn=self.learned_platform['chassis_sn'],disk_free_space=self.learned_platform['disk_free_space'],disk_total_space=self.learned_platform['disk_total_space'],disk_used_space=self.learned_platform['disk_used_space'],image=self.learned_platform['image'],installed_packages=self.learned_platform['installed_packages'],main_mem=self.learned_platform['main_mem'],rp_uptime=self.learned_platform['rp_uptime'],rtr_type=self.learned_platform['rtr_type'],version=self.learned_platform['version'],timestamp=datetime.now().replace(microsecond=0))

                # Save the objects into the database.
                learnPlatform.save()

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
                    learnVRF=LearnVRF(pyats_alias=device.alias,os=device.os,vrf=vrf,route_distinguisher=self.learned_vrf['vrfs'][vrf]['route_distinguisher'],timestamp=datetime.now().replace(microsecond=0))
                # Save the objects into the database.
                    learnVRF.save()

            # Recommended Releases API
            # Show Version to JSON
            self.parsed_show_inventory=ParseShowCommandFunction.parse_show_command(steps, device, "show inventory")
            self.parsed_show_version=ParseShowCommandFunction.parse_show_command(steps, device, "show version")
            with steps.start('Store data',continue_=True) as step:

                # Get OAuth Token
                if hasattr(self, 'parsed_show_inventory'):
                    db_key = RecommendedReleaseCredentials.objects.all().values('key')
                    db_user = RecommendedReleaseCredentials.objects.all().values('client_secret')
                    recommended_release_api_username = db_key[0]['key']
                    recommended_release_api_password = db_user[0]['client_secret']

                    oauth_token_raw = requests.post("https://cloudsso.cisco.com/as/token.oauth2?grant_type=client_credentials&client_id=%s&client_secret=%s" % (recommended_release_api_username,recommended_release_api_password))
                    oauth_token_json = oauth_token_raw.json()
                    oauth_headers = {"Authorization": "%s %s" % (oauth_token_json['token_type'],oauth_token_json['access_token'])}

                # Get Current Version from Device 
                if self.parsed_show_version is not None:
                    if device.os == "nxos":
                        current_version=self.parsed_show_version['platform']['software']['system_version']
                    elif device.os == "iosxe":
                        current_version=self.parsed_show_version['version']['version']

                # Go Get Recommended Release using chassis PID and Oauth token
                if device.os == "nxos":               
                    if "N9K-C9500v" in self.parsed_show_inventory['name']['Chassis']['pid']:
                        pid = "N9K-C93180LC-EX"
                    else:
                        pid = self.parsed_show_inventory['name']['Chassis']['pid']
                    
                    with steps.start('Calling API',continue_=True) as step:
                        try:
                            recommended_release_raw = requests.get("https://api.cisco.com/software/suggestion/v2/suggestions/software/productIds/%s" % pid, headers=oauth_headers)
                            recommended_release_json = recommended_release_raw.json()
                        except Exception as e:
                            step.failed('Could not parse it correctly\n{e}'.format(e=e))                           
                        
                        for product in recommended_release_json['productList']:
                            for suggestion in product['suggestions']:
                                if 'images' in suggestion:
                                    for image in suggestion['images']:
                                        if current_version == suggestion['relDispName']:
                                            compliant = "TRUE"
                                        else:
                                            compliant = "FALSE"
                                        recommended_release = RecommendedRelease(pyats_alias=device.alias,os=device.os,basePID = product['product']['basePID'],productName = product['product']['productName'],softwareType = product['product']['softwareType'],imageName = image['imageName'],description = image['description'],featureSet = image['featureSet'],imageSize = image['imageSize'],isSuggested = suggestion['isSuggested'],majorRelease = suggestion['majorRelease'],releaseTrain = suggestion['releaseTrain'],relDispName = suggestion['relDispName'],releaseDate = suggestion['releaseDate'],releaseLifeCycle = suggestion['releaseLifeCycle'],installed_version=current_version,compliant=compliant,timestamp=datetime.now().replace(microsecond=0))
                                        recommended_release.save()
                elif device.os == "iosxe":
                    if device.type == "Catalyst 9300":
                        for key,value in self.parsed_show_inventory['slot']['1']['other'].items():
                            pid = value['pid']
                            with steps.start('Calling API',continue_=True) as step:
                                try:
                                    recommended_release_raw = requests.get("https://api.cisco.com/software/suggestion/v2/suggestions/software/productIds/%s" % pid, headers=oauth_headers)
                                    recommended_release_json = recommended_release_raw.json()
                                    print(recommended_release_json)
                                except Exception as e:
                                    step.failed('Could not parse it correctly\n{e}'.format(e=e))                           
                        
                            for product in recommended_release_json['productList']:
                                for suggestion in product['suggestions']:
                                    if 'images' in suggestion:
                                        for image in suggestion['images']:
                                            if current_version == suggestion['relDispName']:
                                                compliant = "TRUE"
                                            else:
                                                compliant = "FALSE"
                                            recommended_release = RecommendedRelease(pyats_alias=device.alias,os=device.os,basePID = product['product']['basePID'],productName = product['product']['productName'],softwareType = product['product']['softwareType'],imageName = image['imageName'],description = image['description'],featureSet = image['featureSet'],imageSize = image['imageSize'],isSuggested = suggestion['isSuggested'],majorRelease = suggestion['majorRelease'],releaseTrain = suggestion['releaseTrain'],relDispName = suggestion['relDispName'],releaseDate = suggestion['releaseDate'],releaseLifeCycle = suggestion['releaseLifeCycle'],installed_version=current_version,compliant=compliant,timestamp=datetime.now().replace(microsecond=0))
                                            recommended_release.save()

            # Serial 2 Contract API 
            self.parsed_show_inventory=ParseShowCommandFunction.parse_show_command(steps, device, "show inventory")
            timestamp=datetime.now().replace(microsecond=0)
            #If Device is NXOS go get transceiver serial numbers
            if device.os == "nxos":
                # Show Interface Transceiver
                self.parsed_show_interface_transceiver = ParseShowCommandFunction.parse_show_command(steps, device, "show interface transceiver")
            with steps.start('Store data',continue_=True) as step:
                # Get OAuth Token
                if hasattr(self, 'parsed_show_inventory'):
                    db_key = Serial2ContractCredentials.objects.all().values('key')
                    db_user = Serial2ContractCredentials.objects.all().values('client_secret')
                    serial2contract_api_username = db_key[0]['key']
                    serial2contract_api_password = db_user[0]['client_secret']          #
                    oauth_token_raw = requests.post("https://cloudsso.cisco.com/as/token.oauth2?grant_type=client_credentials&client_id=%s&client_secret=%s" % (serial2contract_api_username,serial2contract_api_password))
                    oauth_token_json = oauth_token_raw.json()
                    oauth_headers = {"Authorization": "%s %s" % (oauth_token_json['token_type'],oauth_token_json['access_token'])}          #
                # Go Get Serial 2 Contract using each serial number and Oauth token
                    if device.platform == "cat4500":
                        for part,value in self.parsed_show_inventory.items():
                            for pid,value in value.items():
                                for sn,value in value.items():
                                    time.sleep(5)
                                    with steps.start('Calling API',continue_=True) as step:
                                        try:                                      
                                            serial2contract_raw = requests.get("https://api.cisco.com/sn2info/v2/coverage/summary/serial_numbers/%s" % value['sn'], headers=oauth_headers)
                                            serial2contract_json = serial2contract_raw.json()
                                            for serial in serial2contract_json['serial_numbers']:
                                                contract_site_customer_name = serial['contract_site_customer_name']
                                                contract_site_address1 = serial['contract_site_address1']
                                                contract_site_city = serial['contract_site_city']
                                                contract_site_state_province = serial['contract_site_state_province']
                                                contract_site_country = serial['contract_site_country']
                                                covered_product_line_end_date = serial['covered_product_line_end_date']
                                                is_covered = serial['is_covered']
                                                parent_sr_no = serial['parent_sr_no']
                                                service_contract_number = serial['service_contract_number']
                                                service_line_descr = serial['service_line_descr']
                                                sr_no = serial['sr_no']
                                                warranty_end_date = serial['warranty_end_date']
                                                warranty_type = serial['warranty_type']
                                                warranty_type_description = serial['warranty_type_description']
                                                for pid in serial['base_pid_list']:
                                                    base_pid = pid['base_pid']
                                                for order in serial['orderable_pid_list']:
                                                    item_description = order['item_description']
                                                    item_type = order['item_type']
                                                    orderable_pid = ['orderable_pid']
                                                    pillar_code = ['pillar_code']

                                                serial2contract = Serial2Contract(pyats_alias=device.alias,os=device.os,base_pid = base_pid,customer_name = contract_site_customer_name,address = contract_site_address1,city = contract_site_city,state_province = contract_site_state_province,country = contract_site_country,product_line_end_date = covered_product_line_end_date,is_covered = is_covered,item_description = item_description,item_type = item_type,orderable_pid = orderable_pid,pillar_code = pillar_code,parent_sn = parent_sr_no,service_contract = service_contract_number,service_description = service_line_descr,serial_number = sr_no,warranty_end = warranty_end_date,warranty_type = warranty_type,warranty_description = warranty_type_description,timestamp=timestamp)
                                                serial2contract.save()
                                        except Exception as e:
                                            step.failed('There was a problem with the APIy\n{e}'.format(e=e))                                                      #
                    elif device.platform == "cat3850":
                        for slot,value01 in self.parsed_show_inventory['slot'].items():
                            for pid,value02 in value01.items():
                                for part,value03 in value02.items():
                                    time.sleep(5)
                                    with steps.start('Calling API',continue_=True) as step:
                                        try:                                      
                                            serial2contract_raw = requests.get("https://api.cisco.com/sn2info/v2/coverage/summary/serial_numbers/%s" % value03['sn'], headers=oauth_headers)
                                            serial2contract_json = serial2contract_raw.json()
                                            for serial in serial2contract_json['serial_numbers']:
                                                contract_site_customer_name = serial['contract_site_customer_name']
                                                contract_site_address1 = serial['contract_site_address1']
                                                contract_site_city = serial['contract_site_city']
                                                contract_site_state_province = serial['contract_site_state_province']
                                                contract_site_country = serial['contract_site_country']
                                                covered_product_line_end_date = serial['covered_product_line_end_date']
                                                is_covered = serial['is_covered']
                                                parent_sr_no = serial['parent_sr_no']
                                                service_contract_number = serial['service_contract_number']
                                                service_line_descr = serial['service_line_descr']
                                                sr_no = serial['sr_no']
                                                warranty_end_date = serial['warranty_end_date']
                                                warranty_type = serial['warranty_type']
                                                warranty_type_description = serial['warranty_type_description']
                                                for pid in serial['base_pid_list']:
                                                    base_pid = pid['base_pid']
                                                for order in serial['orderable_pid_list']:
                                                    item_description = order['item_description']
                                                    item_type = order['item_type']
                                                    orderable_pid = ['orderable_pid']
                                                    pillar_code = ['pillar_code']

                                                serial2contract = Serial2Contract(pyats_alias=device.alias,os=device.os,base_pid = base_pid,customer_name = contract_site_customer_name,address = contract_site_address1,city = contract_site_city,state_province = contract_site_state_province,country = contract_site_country,product_line_end_date = covered_product_line_end_date,is_covered = is_covered,item_description = item_description,item_type = item_type,orderable_pid = orderable_pid,pillar_code = pillar_code,parent_sn = parent_sr_no,service_contract = service_contract_number,service_description = service_line_descr,serial_number = sr_no,warranty_end = warranty_end_date,warranty_type = warranty_type,warranty_description = warranty_type_description,timestamp=timestamp)
                                                serial2contract.save()
                                        except Exception as e:
                                            step.failed('There was a problem with the APIy\n{e}'.format(e=e))                                                      #
                    elif device.platform == "cat9300":
                        for slot,value01 in self.parsed_show_inventory['slot'].items():
                            for pid,value02 in value01.items():
                                for part,value03 in value02.items():                 
                                    time.sleep(5)
                                    with steps.start('Calling API',continue_=True) as step:
                                        try:    
                                            serial2contract_raw = requests.get("https://api.cisco.com/sn2info/v2/coverage/summary/serial_numbers/%s" % value03['sn'], headers=oauth_headers)
                                            serial2contract_json = serial2contract_raw.json()
                                            for serial in serial2contract_json['serial_numbers']:
                                                contract_site_customer_name = serial['contract_site_customer_name']
                                                contract_site_address1 = serial['contract_site_address1']
                                                contract_site_city = serial['contract_site_city']
                                                contract_site_state_province = serial['contract_site_state_province']
                                                contract_site_country = serial['contract_site_country']
                                                covered_product_line_end_date = serial['covered_product_line_end_date']
                                                is_covered = serial['is_covered']
                                                parent_sr_no = serial['parent_sr_no']
                                                service_contract_number = serial['service_contract_number']
                                                service_line_descr = serial['service_line_descr']
                                                sr_no = serial['sr_no']
                                                warranty_end_date = serial['warranty_end_date']
                                                warranty_type = serial['warranty_type']
                                                warranty_type_description = serial['warranty_type_description']
                                                for pid in serial['base_pid_list']:
                                                    base_pid = pid['base_pid']
                                                for order in serial['orderable_pid_list']:
                                                    item_description = order['item_description']
                                                    item_type = order['item_type']
                                                    orderable_pid = ['orderable_pid']
                                                    pillar_code = ['pillar_code']

                                                serial2contract = Serial2Contract(pyats_alias=device.alias,os=device.os,base_pid = base_pid,customer_name = contract_site_customer_name,address = contract_site_address1,city = contract_site_city,state_province = contract_site_state_province,country = contract_site_country,product_line_end_date = covered_product_line_end_date,is_covered = is_covered,item_description = item_description,item_type = item_type,orderable_pid = orderable_pid,pillar_code = pillar_code,parent_sn = parent_sr_no,service_contract = service_contract_number,service_description = service_line_descr,serial_number = sr_no,warranty_end = warranty_end_date,warranty_type = warranty_type,warranty_description = warranty_type_description,timestamp=timestamp)
                                                serial2contract.save()
                                        except Exception as e:
                                            step.failed('There was a problem with the APIy\n{e}'.format(e=e))                                                 #
                    elif device.os == "nxos":
                        for part,value in self.parsed_show_inventory.items():
                            for pid,value in value.items():             
                                with steps.start('Calling API',continue_=True) as step:
                                    try:    
                                        serial2contract_raw = requests.get("https://api.cisco.com/sn2info/v2/coverage/summary/serial_numbers/%s" % value['serial_number'], headers=oauth_headers)
                                        serial2contract_json = serial2contract_raw.json()
                                        for serial in serial2contract_json['serial_numbers']:
                                            contract_site_customer_name = serial['contract_site_customer_name']
                                            contract_site_address1 = serial['contract_site_address1']
                                            contract_site_city = serial['contract_site_city']
                                            contract_site_state_province = serial['contract_site_state_province']
                                            contract_site_country = serial['contract_site_country']
                                            covered_product_line_end_date = serial['covered_product_line_end_date']
                                            is_covered = serial['is_covered']
                                            parent_sr_no = serial['parent_sr_no']
                                            service_contract_number = serial['service_contract_number']
                                            service_line_descr = serial['service_line_descr']
                                            sr_no = serial['sr_no']
                                            warranty_end_date = serial['warranty_end_date']
                                            warranty_type = serial['warranty_type']
                                            warranty_type_description = serial['warranty_type_description']
                                            for pid in serial['base_pid_list']:
                                                base_pid = pid['base_pid']
                                            for order in serial['orderable_pid_list']:
                                                item_description = order['item_description']
                                                item_type = order['item_type']
                                                orderable_pid = ['orderable_pid']
                                                pillar_code = ['pillar_code']

                                        serial2contract = Serial2Contract(pyats_alias=device.alias,os=device.os,base_pid = base_pid,customer_name = contract_site_customer_name,address = contract_site_address1,city = contract_site_city,state_province = contract_site_state_province,country = contract_site_country,product_line_end_date = covered_product_line_end_date,is_covered = is_covered,item_description = item_description,item_type = item_type,orderable_pid = orderable_pid,pillar_code = pillar_code,parent_sn = parent_sr_no,service_contract = service_contract_number,service_description = service_line_descr,serial_number = sr_no,warranty_end = warranty_end_date,warranty_type = warranty_type,warranty_description = warranty_type_description,timestamp=timestamp)
                                        serial2contract.save()
                                    except Exception as e:
                                        step.failed('There was a problem with the APIy\n{e}'.format(e=e))

                        for interface in self.parsed_show_interface_transceiver.items():
                            if 'transceiver_present' in interface:
                                with steps.start('Calling API',continue_=True) as step:
                                    try:    
                                        serial2contract_raw = requests.get("https://api.cisco.com/sn2info/v2/coverage/summary/serial_numbers/%s" % interface['serial_number'], headers=oauth_headers)
                                        serial2contract_json = serial2contract_raw.json()
                                        for serial in serial2contract_json['serial_numbers']:
                                            contract_site_customer_name = serial['contract_site_customer_name']
                                            contract_site_address1 = serial['contract_site_address1']
                                            contract_site_city = serial['contract_site_city']
                                            contract_site_state_province = serial['contract_site_state_province']
                                            contract_site_country = serial['contract_site_country']
                                            covered_product_line_end_date = serial['covered_product_line_end_date']
                                            is_covered = serial['is_covered']
                                            parent_sr_no = serial['parent_sr_no']
                                            service_contract_number = serial['service_contract_number']
                                            service_line_descr = serial['service_line_descr']
                                            sr_no = serial['sr_no']
                                            warranty_end_date = serial['warranty_end_date']
                                            warranty_type = serial['warranty_type']
                                            warranty_type_description = serial['warranty_type_description']
                                            for pid in serial['base_pid_list']:
                                                base_pid = pid['base_pid']
                                            for order in serial['orderable_pid_list']:
                                                item_description = order['item_description']
                                                item_type = order['item_type']
                                                orderable_pid = ['orderable_pid']
                                                pillar_code = ['pillar_code']

                                        serial2contract = Serial2Contract(pyats_alias=device.alias,os=device.os,base_pid = base_pid,customer_name = contract_site_customer_name,address = contract_site_address1,city = contract_site_city,state_province = contract_site_state_province,country = contract_site_country,product_line_end_date = covered_product_line_end_date,is_covered = is_covered,item_description = item_description,item_type = item_type,orderable_pid = orderable_pid,pillar_code = pillar_code,parent_sn = parent_sr_no,service_contract = service_contract_number,service_description = service_line_descr,serial_number = sr_no,warranty_end = warranty_end_date,warranty_type = warranty_type,warranty_description = warranty_type_description,timestamp=timestamp)
                                        serial2contract.save()
                                    except Exception as e:
                                        step.failed('There was a problem with the APIy\n{e}'.format(e=e))

            # PSIRT API 
            self.parsed_show_version=ParseShowCommandFunction.parse_show_command(steps, device, "show version")
            with steps.start('Store data',continue_=True) as step:

                # Get OAuth Token
                if hasattr(self, 'parsed_show_version'):
                    db_key=PSIRTCredentials.objects.all().values('key')
                    db_user=PSIRTCredentials.objects.all().values('client_secret')
                    psirt_api_username=db_key[0]['key']
                    psirt_api_password=db_user[0]['client_secret']

                    oauth_token_raw=requests.post("https://cloudsso.cisco.com/as/token.oauth2?grant_type=client_credentials&client_id=%s&client_secret=%s" % (psirt_api_username,psirt_api_password))
                    oauth_token_json=oauth_token_raw.json()
                    oauth_headers={"Authorization": "%s %s" % (oauth_token_json['token_type'],oauth_token_json['access_token'])}

                # Get Current Version from Device 
                if self.parsed_show_version is not None:
                    if device.os == "nxos":
                        current_version=self.parsed_show_version['platform']['software']['system_version']
                    elif device.os == "iosxe":
                        current_version=self.parsed_show_version['version']['version']

                with steps.start('Calling API',continue_=True) as step:
                    try:
                        if device.os == "nxos":
                            psirt_raw=requests.get("https://api.cisco.com/security/advisories/nxos?version=%s" % current_version, headers=oauth_headers)
                        else:
                            psirt_raw=requests.get("https://api.cisco.com/security/advisories/ios?version=%s" % current_version, headers=oauth_headers)
                    
                    except Exception as e:
                        step.failed('Could not parse it correctly\n{e}'.format(e=e))                           
                        
                    psirt_json=psirt_raw.json()
                    for advisory in psirt_json['advisories']:
                        if device.os == "nxos":
                            for platform in advisory['platforms']:
                                psirt=PSIRT(pyats_alias=device.alias,os=device.os,advisory_id=advisory['advisoryId'],advisory_title=advisory['advisoryTitle'],bug_ids=advisory['bugIDs'],ips_signatures=advisory['ipsSignatures'],cves=advisory['cves'],cvrf_url=advisory['cvrfUrl'],cvss_base_score=advisory['cvssBaseScore'],cwe=advisory['cwe'],platform_name=platform['name'],ios_release=advisory['iosRelease'],first_fixed=platform['firstFixes'],first_published=advisory['firstPublished'],last_updated=advisory['lastUpdated'],status=advisory['status'],version=advisory['version'],publication_url=advisory['publicationUrl'],sir=advisory['sir'],summary=advisory['summary'],timestamp=datetime.now().replace(microsecond=0))
                        else:        
                            psirt=PSIRT(pyats_alias=device.alias,os=device.os,advisory_id=advisory['advisoryId'],advisory_title=advisory['advisoryTitle'],bug_ids=advisory['bugIDs'],ips_signatures=advisory['ipsSignatures'],cves=advisory['cves'],cvrf_url=advisory['cvrfUrl'],cvss_base_score=advisory['cvssBaseScore'],cwe=advisory['cwe'],platform_name="null",ios_release=advisory['iosRelease'],first_fixed=advisory['firstFixed'],first_published=advisory['firstPublished'],last_updated=advisory['lastUpdated'],status=advisory['status'],version=advisory['version'],publication_url=advisory['publicationUrl'],sir=advisory['sir'],summary=advisory['summary'],timestamp=datetime.now().replace(microsecond=0))
                        
                        psirt.save()

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