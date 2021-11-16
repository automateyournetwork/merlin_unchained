# ----------------
# Copyright
# ----------------
# Written by John Capobianco, March 2021
# Copyright (c) 2021 John Capobianco

# ----------------
# Python
# ----------------
from pyats import aetest
from pyats import topology
from pyats.log.utils import banner
from merlin.models import DynamicJobInput
from jinja2 import Environment, FileSystemLoader

template_dir = 'merlin/templates/Jinja2'
env = Environment(loader=FileSystemLoader(template_dir))
voice_command_template = env.get_template('voice_command.j2')
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
            voice_config_db = DynamicJobInput.objects.all().values('input_field')
            voice_config = voice_config_db[0]['input_field']
            templated_voice_command = voice_command_template.render(voice_command=voice_config)
            with steps.start("Voice Command", continue_=True) as step:
                try:
                    device.configure(templated_voice_command)
                    delete_records = DynamicJobInput.objects.all()
                    delete_records.delete()
                except Exception as e:
                    step.failed('Could not shut the interface correctly\n{e}'.format(e=e))