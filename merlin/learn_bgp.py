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
from merlin.models import LearnBGP

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
            self.learned_bgp = ParseLearnFunction.parse_learn(steps, device, "bgp")
            if self.learned_bgp is not None:
                # Set Django Database values from pyATS JSON
                for instance in self.learned_bgp['instance']:
                    for vrf in self.learned_bgp['instance'][instance]['vrf']:
                        for neighbor in self.learned_bgp['instance'][instance]['vrf'][vrf]['neighbor']:
                            learnBGP=LearnBGP(pyats_alias=device.alias,os=device.os,instance=instance,bgp_id=self.learned_bgp['instance'][instance]['bgp_id'],state=self.learned_bgp['instance'][instance]['protocol_state'],vrf=vrf,router_id=self.learned_bgp['instance'][instance]['vrf'][vrf]['router_id'],cluster_id=self.learned_bgp['instance'][instance]['vrf'][vrf]['cluster_id'],confederation_id=self.learned_bgp['instance'][instance]['vrf'][vrf]['confederation_identifier'],neighbor=neighbor,version=self.learned_bgp['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['bgp_version'],hold_time=self.learned_bgp['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['holdtime'],keep_alive_interval=self.learned_bgp['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['keepalive_interval'],local_as=self.learned_bgp['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['local_as_as_no'],remote_as=self.learned_bgp['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['remote_as'],total_received=self.learned_bgp['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['bgp_neighbor_counters']['messages']['received']['total'],total_sent=self.learned_bgp['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['bgp_neighbor_counters']['messages']['sent']['total'],last_reset=self.learned_bgp['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['bgp_session_transport']['connection']['last_reset'],reset_reason=self.learned_bgp['instance'][instance]['vrf'][vrf]['neighbor'][neighbor]['bgp_session_transport']['connection']['reset_reason'],timestamp=datetime.now().replace(microsecond=0))
                    learnBGP.save()