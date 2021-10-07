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
from general_functionalities import ParseShowCommandFunction
from datetime import datetime
from merlin.models import Serial2ContractCredentials, Serial2Contract

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
            # Show Inventory to JSON
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