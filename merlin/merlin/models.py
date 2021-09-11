from django.db import models

class LearnVLAN(models.Model):
    pyats_alias = models.TextField()
    os = models.TextField()
    vlan = models.TextField()
    interfaces = models.TextField() 
    mode = models.TextField()
    name = models.TextField()
    shutdown = models.TextField()
    state = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        template = '{0.pyats_alias} {0.os} {0.vlan} {0.interfaces} {0.mode} {0.name} {0.shutdown} {0.state} {0.timestamp}'
        return template.format(self)

class LearnVRF(models.Model):
    pyats_alias = models.TextField()
    os = models.TextField()
    vrf = models.TextField()
    address_family_ipv4 = models.TextField()
    address_family_ipv6 = models.TextField()
    route_distinguisher = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        template = '{0.pyats_alias} {0.os} {0.vrf} {0.address_family_ipv4} {0.address_family_ipv6} {0.route_distinguisher} {0.timestamp}'
        return template.format(self)

class ShowIPIntBrief(models.Model):
    pyats_alias = models.TextField()
    os = models.TextField()
    interface = models.TextField()
    interface_status = models.TextField()
    ip_address = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        template = '{0.pyats_alias} {0.os} {0.interface} {0.interface_status} {0.ip_address} {0.timestamp}'
        return template.format(self)

class ShowVersion(models.Model):
    pyats_alias = models.TextField()
    bootflash = models.TextField()
    chassis = models.TextField()
    cpu = models.TextField()
    device_name = models.TextField()
    memory = models.TextField()
    model = models.TextField()
    processor_board_id = models.TextField()
    rp = models.TextField()
    slots = models.TextField()
    days = models.TextField()
    hours = models.TextField()
    minutes = models.TextField()
    seconds = models.TextField()
    name = models.TextField()
    os = models.TextField()
    reason = models.TextField()
    system_compile_time = models.TextField()
    system_image_file = models.TextField()
    system_version = models.TextField()
    chassis_sn = models.TextField()
    compiled_by = models.TextField()
    curr_config_register = models.TextField()
    image_id = models.TextField()
    image_type = models.TextField()
    label = models.TextField()
    license_level = models.TextField()
    license_type = models.TextField()
    non_volatile = models.TextField()
    physical = models.TextField()
    next_reload_license_level = models.TextField()
    platform = models.TextField()
    processor_type = models.TextField()
    returned_to_rom_by = models.TextField()
    rom = models.TextField()
    rtr_type = models.TextField()
    uptime = models.TextField()
    uptime_this_cp = models.TextField()
    version_short = models.TextField()
    xe_version = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        template = '{0.pyats_alias} {0.bootflash} {0.chassis} {0.cpu} {0.device_name} {0.memory} {0.model} {0.processor_board_id} {0.rp} {0.slots} {0.days} {0.hours} {0.minutes} {0.seconds} {0.name} {0.os} {0.reason} {0.system_compile_time} {0.system_image_file} {0.system_version} {0.chassis_sn} {0.compiled_by} {0.curr_config_register} {0.image_id} {0.image_type} {0.label} {0.license_level} {0.license_type} {0.non_volatile} {0.physical} {0.next_reload_license_level} {0.platform} {0.processor_type} {0.returned_to_rom_by} {0.rom} {0.rtr_type} {0.uptime} {0.uptime_this_cp} {0.version_short} {0.xe_version} {0.timestamp}'
        return template.format(self)