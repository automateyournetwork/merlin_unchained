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
from datetime import datetime
from merlin.models import LearnBGPInstances, LearnBGPRoutesPerPeer, LearnBGPTables

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
                                learnBGPRoutesPerPeer = LearnBGPRoutesPerPeer(pyats_alias=device.alias,os=device.os,instance=instance,vrf=vrf,neighbor=neighbor,advertised=self.learned_bgp.routes_per_peer['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['address_family']['ipv4 unicast']['advertised'],routes=self.learned_bgp.routes_per_peer['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['address_family']['ipv4 unicast']['routes'],remote_as=self.learned_bgp.routes_per_peer['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['remote_as'],timestamp=datetime.now().replace(microsecond=0))
                        learnBGPRoutesPerPeer.save()
                        
                if self.learned_bgp.table is not None:
                    for instance in self.learned_bgp.table['instance']:
                        for vrf in self.learned_bgp.table['instance'][instance]['vrf']:
                            for prefix in self.learned_bgp.table['instance'][instance]['vrf'][vrf]['address_family']['ipv4 unicast']['prefixes']:
                                for index in self.learned_bgp.table['instance'][instance]['vrf'][vrf]['address_family']['ipv4 unicast']['prefixes'][prefix]['index']:
                                    learnBGPTables = LearnBGPTables(pyats_alias=device.alias,os=device.os,instance=instance,vrf=vrf,table_version=self.learned_bgp.table['instance'][instance]['vrf'][vrf]['address_family']['ipv4 unicast']['bgp_table_version'],prefix=prefix,index=index,localpref=self.learned_bgp.table['instance'][instance]['vrf'][vrf]['address_family']['ipv4 unicast']['prefixes'][prefix]['index'][index]['localpref'],next_hop=self.learned_bgp.table['instance'][instance]['vrf'][vrf]['address_family']['ipv4 unicast']['prefixes'][prefix]['index'][index]['next_hop'],origin_code=self.learned_bgp.table['instance'][instance]['vrf'][vrf]['address_family']['ipv4 unicast']['prefixes'][prefix]['index'][index]['origin_codes'],status_code=self.learned_bgp.table['instance'][instance]['vrf'][vrf]['address_family']['ipv4 unicast']['prefixes'][prefix]['index'][index]['status_codes'],weight=self.learned_bgp.table['instance'][instance]['vrf'][vrf]['address_family']['ipv4 unicast']['prefixes'][prefix]['index'][index]['status_codes'],timestamp=datetime.now().replace(microsecond=0))
                        learnBGPTables.save()