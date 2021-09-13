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
from merlin.models import LearnACL

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
                for acl in self.learned_acl['acls']:
                    if self.learned_acl['acls'][acl]['ace']:
                        for ace in self.learned_acl['acls'][acl]['ace']:
                            if self.learned_acl['acls'][acl]['ace'][ace]['matches']['l3']:
                                if self.learned_acl['acls'][acl]['ace'][ace]['matches']['l3']['ipv4']:
                                    if self.learned_acl['acls'][acl]['ace'][ace]['matches']['l3']['ipv4']['source_network']:
                                        for source_network in self.learned_acl['acls'][acl]['ace'][ace]['matches']['l3']['ipv4']['source_network']:
                                            learnACL=LearnACL(pyats_alias=device.alias,os=device.os,acl=acl,ace=ace,permission=self.learned_acl['acls'][acl]['ace'][ace]['actions']['forwarding'],logging=self.learned_acl['acls'][acl]['ace'][ace]['actions']['logging'],source_network=source_network,destination_network=self.learned_acl['acls'][acl]['ace'][ace]['matches']['l3']['ipv4']['destination_network'],l3_protocol=self.learned_acl['acls'][acl]['ace'][ace]['matches']['l3']['ipv4']['protocol'],l4_protocol="null",operator="null",port="null",timestamp=datetime.now().replace(microsecond=0))

                    #Write to the DB    
                    learnACL.save()