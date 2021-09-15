from django.db import models

class LearnACL(models.Model):
    pyats_alias = models.TextField()
    os = models.TextField()
    acl = models.TextField()
    ace = models.TextField()
    permission = models.TextField()
    logging = models.TextField()
    source_network = models.TextField()
    destination_network = models.TextField()
    l3_protocol = models.TextField()
    l4_protocol = models.TextField()
    operator = models.TextField()
    port = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        template = '{0.pyats_alias} {0.os} {0.acl} {0.ace} {0.permission} {0.logging} {0.source_network} {0.destination_network} {0.l3_protocol} {0.l4_protocol} {0.operator} {0.port} {0.timestamp}'
        return template.format(self)

class LearnARP(models.Model):
    pyats_alias = models.TextField()
    os = models.TextField()
    interface = models.TextField()
    neighbor_ip = models.TextField()
    neighbor_mac = models.TextField()
    origin = models.TextField()
    local_proxy = models.TextField()
    proxy = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        template = '{0.pyats_alias} {0.os} {0.interface} {0.neighbor_ip} {0.neighbor_mac} {0.origin} {0.local_proxy} {0.proxy} {0.timestamp}'
        return template.format(self)        

class LearnARPStatistics(models.Model):
    pyats_alias = models.TextField()
    os = models.TextField()
    entries_total = models.TextField()
    in_drops = models.TextField()
    in_replies_pkts = models.TextField()
    in_requests_pkts = models.TextField()
    incomplete_total = models.TextField()
    out_replies_pkts = models.TextField()
    out_requests_pkts = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        template = '{0.pyats_alias} {0.os} {0.entries_total} {0.in_drops} {0.in_replies_pkts} {0.in_requests_pkts} {0.incomplete_total} {0.out_replies_pkts} {0.out_requests_pkts} {0.timestamp}'
        return template.format(self) 

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

class ShowInventory(models.Model):
    pyats_alias = models.TextField()
    os = models.TextField()
    part = models.TextField()
    description = models.TextField()
    pid = models.TextField()
    serial_number = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        template = '{0.pyats_alias} {0.os} {0.part} {0.description} {0.pid} {0.serial_number} {0.timestamp}'
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