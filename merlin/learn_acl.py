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
from merlin.models import LearnACL, DynamicJobInput

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
        testbed.devices.values():
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