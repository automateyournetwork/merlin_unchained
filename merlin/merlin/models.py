from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Devices(models.Model):
    hostname = models.TextField()
    alias = models.TextField()
    device_type = models.TextField()
    os = models.TextField()
    platform = models.TextField()
    username = models.TextField()
    password = models.TextField()
    protocol = models.TextField()
    ip_address = models.TextField()
    port = models.TextField()
    connection_timeout = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        template = '{0.hostname} {0.alias} {0.device_type} {0.os} {0.platform} {0.username} {0.password} {0.protocol} {0.ip_address} {0.port} {0.connection_timeout} {0.timestamp}'
        return template.format(self)

class DynamicJobInput(models.Model):
    input_field = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        template = '{0.input_field} {0.timestamp}'
        return template.format(self)

class EoXCredentials(models.Model):
    key = models.TextField()
    client_secret = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        template = '{0.key} {0.client_secret} {0.timestamp}'
        return template.format(self)

class EoX_PID(models.Model):
    pyats_alias = models.TextField()
    os = models.TextField()
    pid = models.TextField()
    description = models.TextField()
    bulletin_number = models.TextField()
    bulletin_url = models.TextField()
    external_date = models.DateTimeField()
    sale_date = models.DateTimeField()
    sw_maintenance = models.DateTimeField()
    security = models.DateTimeField()
    routine_failure = models.DateTimeField()
    service_contract = models.DateTimeField()
    last = models.DateTimeField()
    svc_attach = models.DateTimeField()
    last_updated = models.DateTimeField()
    pid_active = models.TextField()
    migration_information = models.TextField()
    migration_option = models.TextField()
    migration_pid = models.TextField()
    migration_name = models.TextField()
    migration_strat = models.TextField()
    migration_url = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        template = '{0.pyats_alias} {0.os} {0.pid} {0.description} {0.bulletin_number} {0.bulletin_url} {0.external_date} {0.sale_date} {0.sw_maintenance} {0.security} {0.routine_failure} {0.service_contract} {0.last} {0.svc_attach} {0.last_updated} {0.pid_active} {0.migration_information} {0.migration_option} {0.migration_pid} {0.migration_name} {0.migration_strat} {0.migration_url} {0.timestamp}'
        return template.format(self)

class EoX_SN(models.Model):
    pyats_alias = models.TextField()
    os = models.TextField()
    pid = models.TextField()
    description = models.TextField()
    bulletin_number = models.TextField()
    bulletin_url = models.TextField()
    external_date = models.DateTimeField()
    sale_date = models.DateTimeField()
    sw_maintenance = models.DateTimeField()
    security = models.DateTimeField()
    routine_failure = models.DateTimeField()
    service_contract = models.DateTimeField()
    last = models.DateTimeField()
    svc_attach = models.DateTimeField()
    last_updated = models.DateTimeField()
    pid_active = models.TextField()
    migration_information = models.TextField()
    migration_option = models.TextField()
    migration_pid = models.TextField()
    migration_name = models.TextField()
    migration_strat = models.TextField()
    migration_url = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        template = '{0.pyats_alias} {0.os} {0.pid} {0.description} {0.bulletin_number} {0.bulletin_url} {0.external_date} {0.sale_date} {0.sw_maintenance} {0.security} {0.routine_failure} {0.service_contract} {0.last} {0.svc_attach} {0.last_updated} {0.pid_active} {0.migration_information} {0.migration_option} {0.migration_pid} {0.migration_name} {0.migration_strat} {0.migration_url} {0.timestamp}'
        return template.format(self)

class EoX_IOS(models.Model):
    pyats_alias = models.TextField()
    os = models.TextField()
    pid = models.TextField()
    description = models.TextField()
    bulletin_number = models.TextField()
    bulletin_url = models.TextField()
    external_date = models.DateTimeField()
    sale_date = models.DateTimeField()
    sw_maintenance = models.DateTimeField()
    security = models.DateTimeField()
    routine_failure = models.DateTimeField()
    service_contract = models.DateTimeField()
    last = models.DateTimeField()
    svc_attach = models.DateTimeField()
    last_updated = models.DateTimeField()
    pid_active = models.TextField()
    migration_information = models.TextField()
    migration_option = models.TextField()
    migration_pid = models.TextField()
    migration_name = models.TextField()
    migration_strat = models.TextField()
    migration_url = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        template = '{0.pyats_alias} {0.os} {0.pid} {0.description} {0.bulletin_number} {0.bulletin_url} {0.external_date} {0.sale_date} {0.sw_maintenance} {0.security} {0.routine_failure} {0.service_contract} {0.last} {0.svc_attach} {0.last_updated} {0.pid_active} {0.migration_information} {0.migration_option} {0.migration_pid} {0.migration_name} {0.migration_strat} {0.migration_url} {0.timestamp}'
        return template.format(self)

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

class LearnBGPInstances(models.Model):
    pyats_alias = models.TextField()
    os = models.TextField()
    instance = models.TextField()
    bgp_id = models.TextField()
    protocol_state = models.TextField()
    nexthop_trigger_delay_critical = models.TextField()
    nexthop_trigger_delay_noncritical = models.TextField()
    nexthop_trigger_enabled = models.TextField()
    vrf = models.TextField()
    router_id = models.TextField()
    cluster_id = models.TextField()
    confederation_id = models.TextField()
    neighbor = models.TextField()
    version = models.TextField()
    hold_time = models.TextField()
    keep_alive_interval = models.TextField()
    local_as = models.TextField()
    remote_as = models.TextField()
    neighbor_counters_received_bytes_in_queue = models.TextField()
    neighbor_counters_received_capability = models.TextField()
    neighbor_counters_received_keepalives = models.TextField()
    neighbor_counters_received_notifications = models.TextField()
    neighbor_counters_received_opens = models.TextField()
    neighbor_counters_received_route_refresh = models.TextField()
    neighbor_counters_received_total = models.TextField()
    neighbor_counters_received_total_bytes = models.TextField()
    neighbor_counters_received_updates = models.TextField()
    neighbor_counters_sent_bytes_in_queue = models.TextField()
    neighbor_counters_sent_capability = models.TextField()
    neighbor_counters_sent_keepalives = models.TextField()
    neighbor_counters_sent_notifications = models.TextField()
    neighbor_counters_sent_opens = models.TextField()
    neighbor_counters_sent_route_refresh = models.TextField()
    neighbor_counters_sent_total = models.TextField()
    neighbor_counters_sent_total_bytes = models.TextField()
    neighbor_counters_sent_updates = models.TextField()
    last_reset = models.TextField()
    reset_reason = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        template = '{0.pyats_alias} {0.os} {0.instance} {0.bgp_id} {0.protocol_state} {0.nexthop_trigger_delay_critical} {0.nexthop_trigger_delay_noncritical} {0.nexthop_trigger_enabled} {0.vrf} {0.router_id} {0.cluster_id} {0.confederation_id} {0.neighbor} {0.version} {0.hold_time} {0.keep_alive_interval} {0.local_as} {0.remote_as} {0.neighbor_counters_received_bytes_in_queue} {0.neighbor_counters_received_capability} {0.neighbor_counters_received_keepalives} {0.neighbor_counters_received_notifications} {0.neighbor_counters_received_opens} {0.neighbor_counters_received_route_refresh} {0.neighbor_counters_received_total} {0.neighbor_counters_received_total_bytes} {0.neighbor_counters_received_updates} {0.neighbor_counters_sent_bytes_in_queue} {0.neighbor_counters_sent_capability} {0.neighbor_counters_sent_keepalives} {0.neighbor_counters_sent_notifications} {0.neighbor_counters_sent_opens} {0.neighbor_counters_sent_route_refresh} {0.neighbor_counters_sent_total} {0.neighbor_counters_sent_total_bytes} {0.neighbor_counters_sent_updates} {0.last_reset} {0.reset_reason} {0.timestamp}'
        return template.format(self)

class LearnBGPRoutesPerPeer(models.Model):
    pyats_alias = models.TextField()
    os = models.TextField()
    instance = models.TextField()
    vrf = models.TextField()
    neighbor = models.TextField()
    advertised = models.TextField()
    routes = models.TextField()
    remote_as = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        template = '{0.pyats_alias} {0.os} {0.instance} {0.vrf} {0.neighbor} {0.advertised} {0.routes} {0.remote_as} {0.timestamp}'
        return template.format(self)

class LearnBGPTables(models.Model):
    pyats_alias = models.TextField()
    os = models.TextField()
    instance = models.TextField()
    vrf = models.TextField()
    table_version = models.TextField()
    prefix = models.TextField()
    index = models.TextField()
    localpref = models.TextField()
    next_hop = models.TextField()
    origin_code = models.TextField()
    status_code = models.TextField()
    weight = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        template = '{0.pyats_alias} {0.os} {0.instance} {0.vrf} {0.table_version} {0.prefix} {0.index} {0.localpref} {0.next_hop} {0.origin_code} {0.status_code} {0.weight} {0.timestamp}'
        return template.format(self)

class LearnConfig(models.Model):
    pyats_alias = models.TextField()
    os = models.TextField()
    config = models.JSONField()
    timestamp = models.DateTimeField()

    def __str__(self):
        template = '{0.pyats_alias} {0.os} {0.config} {0.timestamp}'
        return template.format(self)

class LearnInterface(models.Model):
    pyats_alias = models.TextField()
    os = models.TextField()
    interface = models.TextField()
    description = models.TextField()
    enabled = models.TextField()
    status = models.TextField()
    access_vlan = models.TextField()
    native_vlan = models.TextField()
    switchport = models.TextField()
    switchport_mode = models.TextField()
    interface_type = models.TextField()
    bandwidth = models.TextField()
    auto_negotiate = models.TextField()
    speed = models.TextField()
    duplex = models.TextField()
    mtu = models.TextField()
    mac_address = models.TextField()
    physical_address = models.TextField()
    ip_address = models.TextField()
    medium = models.TextField()
    delay = models.TextField()
    encapsulation = models.TextField()
    flow_control_receive = models.TextField()
    flow_control_send = models.TextField()
    port_channel = models.TextField()
    port_channel_member_interfaces = models.TextField()
    port_channel_member = models.TextField()
    last_change = models.TextField()
    input_broadcast = models.TextField()
    input_crc_errors = models.TextField()
    input_errors = models.TextField()
    input_mac_pause_frames = models.TextField()
    input_multicast = models.TextField()
    input_octets = models.TextField()
    input_unicast = models.TextField()
    input_unknown = models.TextField()
    input_total = models.TextField()
    output_broadcast = models.TextField()
    output_discard = models.TextField()
    output_errors = models.TextField()
    output_mac_pause_frames = models.TextField()
    output_multicast = models.TextField()
    output_unicast = models.TextField()
    output_total = models.TextField()
    last_clear = models.TextField()
    input_rate = models.TextField()
    load_interval = models.TextField()
    output_rate = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        template = '{0.pyats_alias} {0.os} {0.interface} {0.description} {0.enabled} {0.status} {0.access_vlan} {0.native_vlan} {0.switchport} {0.switchport_mode} {0.interface_type} {0.bandwidth} {0.auto_negotiate} {0.speed} {0.duplex} {0.mtu} {0.mac_address} {0.physical_address} {0.ip_address} {0.medium} {0.delay} {0.encapsulation} {0.flow_control_receive} {0.flow_control_send} {0.port_channel} {0.port_channel_member} {0.last_change} {0.input_broadcast} {0.input_crc_errors} {0.input_errors} {0.input_mac_pause_frames} {0.input_multicast} {0.input_octets} {0.input_unicast} {0.input_unknown} {0.input_total} {0.output_broadcast} {0.output_discard} {0.output_errors} {0.output_mac_pause_frames} {0.output_multicast} {0.output_unicast} {0.output_total} {0.last_clear} {0.input_rate} {0.load_interval} {0.output_rate} {0.timestamp}'
        return template.format(self)

class InterfaceEnable(models.Model):
    pyats_alias = models.TextField()
    interface = models.TextField()

    def __str__(self):
        template = '{0.pyats_alias} {0.interface}'
        return template.format(self)

class LearnPlatform(models.Model):
    pyats_alias = models.TextField()
    os = models.TextField()
    chassis = models.TextField()
    chassis_sn = models.TextField()
    disk_free_space = models.TextField()
    disk_total_space = models.TextField()
    disk_used_space = models.TextField()
    image = models.TextField()
    installed_packages = models.TextField()
    main_mem = models.TextField()
    rp_uptime = models.TextField()
    rtr_type = models.TextField()
    version = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        template = '{0.pyats_alias} {0.os} {0.chassis} {0.chassis_sn} {0.disk_free_space} {0.disk_total_space} {0.disk_used_space} {0.image} {0.installed_packages} {0.main_mem} {0.rp_uptime} {0.rtr_type} {0.version} {0.timestamp}'
        return template.format(self)

class LearnPlatformSlots(models.Model):
    pyats_alias = models.TextField()
    os = models.TextField()
    slot = models.TextField()
    slot_name = models.TextField()
    slot_sn = models.TextField()
    slot_state = models.TextField()
    slot_redundancy_state = models.TextField()
    rp_boot_image = models.TextField()
    slot_rp_uptime = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        template = '{0.pyats_alias} {0.os} {0.slot} {0.slot_name} {0.slot_sn} {0.slot_state} {0.slot_redundancy_state} {0.rp_boot_image} {0.slot_rp_uptime} {0.timestamp}'
        return template.format(self)

class LearnPlatformVirtual(models.Model):
    pyats_alias = models.TextField()
    os = models.TextField()    
    virtual_device_name = models.TextField()
    virtual_device_status = models.TextField()
    virtual_device_member = models.TextField()
    virtual_device_member_status = models.TextField()
    virtual_device_member_type = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        template = '{0.pyats_alias} {0.os} {0.virtual_device_name} {0.virtual_device_status} {0.virtual_device_member} {0.virtual_device_member_status} {0.virtual_device_member_type} {0.timestamp}'
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
    route_distinguisher = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        template = '{0.pyats_alias} {0.os} {0.vrf} {0.route_distinguisher} {0.timestamp}'
        return template.format(self)

class NMAP(models.Model):
    pyats_alias = models.TextField()
    os = models.TextField()
    protocol = models.TextField()
    port = models.TextField()
    conf = models.TextField()
    cpe = models.TextField()
    extra_info = models.TextField()
    name = models.TextField()
    product = models.TextField()
    reason = models.TextField()
    state = models.TextField()
    version = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        template = '{0.pyats_alias} {0.os} {0.protocol} {0.port} {0.conf} {0.cpe} {0.extra_info} {0.name} {0.product} {0.reason} {0.state} {0.version} {0.timestamp}'
        return template.format(self)

class PSIRTCredentials(models.Model):
    key = models.TextField()
    client_secret = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        template = '{0.key} {0.client_secret} {0.timestamp}'
        return template.format(self)

class PSIRT(models.Model):
    pyats_alias = models.TextField()
    os = models.TextField()
    advisory_id = models.TextField()
    advisory_title = models.TextField()
    bug_ids = models.TextField()
    ips_signatures = models.TextField()
    cves = models.TextField()
    cvrf_url = models.TextField()
    cvss_base_score = models.TextField()
    cwe = models.TextField()
    platform_name = models.TextField()
    ios_release = models.TextField()
    first_fixed = models.TextField()
    first_published = models.TextField()
    last_updated = models.TextField()
    status = models.TextField()
    version = models.TextField()
    publication_url = models.TextField()
    sir = models.TextField()
    summary = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        template = '{0.pyats_alias} {0.os} {0.advisory_id} {0.advisory_title} {0.bug_ids} {0.ips_signatures} {0.cves} {0.cvrf_url} {0.cvss_base_score} {0.cwe} {0.platform_name} {0.ios_release} {0.first_fixed} {0.first_published} {0.last_updated} {0.status} {0.version} {0.publication_url} {0.sir} {0.summary} {0.timestamp}'
        return template.format(self)

class RecommendedReleaseCredentials(models.Model):
    key = models.TextField()
    client_secret = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        template = '{0.key} {0.client_secret} {0.timestamp}'
        return template.format(self)

class RecommendedRelease(models.Model):
    pyats_alias = models.TextField()
    os = models.TextField()
    basePID = models.TextField()
    productName = models.TextField()
    softwareType = models.TextField()
    imageName = models.TextField()
    description = models.TextField()
    featureSet = models.TextField()   
    imageSize = models.TextField()
    isSuggested = models.TextField()
    majorRelease = models.TextField()
    releaseTrain = models.TextField()
    relDispName = models.TextField()
    releaseDate = models.TextField()
    releaseLifeCycle = models.TextField()
    installed_version= models.TextField()
    compliant = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        template = '{0.pyats_alias} {0.os} {0.basePID} {0.productName} {0.softwareType} {0.imageName} {0.description} {0.featureSet} {0.imageSize} {0.isSuggested} {0.majorRelease} {0.releaseTrain} {0.relDispName} {0.releaseDate} {0.releaseLifeCycle} {0.installed_version} {0.compliant} {0.timestamp}'
        return template.format(self)

class Serial2ContractCredentials(models.Model):
    key = models.TextField()
    client_secret = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        template = '{0.key} {0.client_secret} {0.timestamp}'
        return template.format(self)

class Serial2Contract(models.Model):
    pyats_alias = models.TextField()
    os = models.TextField()
    base_pid = models.TextField()
    customer_name = models.TextField()
    address = models.TextField()
    city = models.TextField()
    state_province = models.TextField()
    country = models.TextField()
    product_line_end_date = models.TextField()
    is_covered = models.TextField()
    item_description = models.TextField()
    item_type = models.TextField()
    orderable_pid = models.TextField()
    pillar_code = models.TextField()
    parent_sn = models.TextField()
    service_contract = models.TextField()
    service_description = models.TextField()
    serial_number = models.TextField()
    warranty_end = models.TextField()
    warranty_type = models.TextField()
    warranty_description = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        template = '{0.pyats_alias} {0.os} {0.base_pid} {0.customer_name} {0.address} {0.city} {0.state_province} {0.country} {0.product_line_end_date} {0.is_covered} {0.item_description} {0.item_type} {0.orderable_pid} {0.pillar_code} {0.parent_sn} {0.service_contract} {0.service_description} {0.serial_number} {0.warranty_end} {0.warranty_type} {0.warranty_description} {0.timestamp}'
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

class ShowLicenseSummary(models.Model):
    pyats_alias = models.TextField()
    os = models.TextField()
    license_name = models.TextField()
    entitlement = models.TextField()
    count = models.TextField()
    status = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        template = '{0.pyats_alias} {0.os} {0.license_name} {0.entitlement} {0.count} {0.status} {0.timestamp}'
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

class TwilioCredentials(models.Model):
    sid = models.TextField()
    token = models.TextField()
    from_number = PhoneNumberField(unique=True)
    from_number_sms = PhoneNumberField(unique=True)

    def __str__(self):
        template = '{0.sid} {0.token} {0.from_number} {0.from_number_sms}'
        return template.format(self)

class NumbersToCall(models.Model):
    number_to_call = PhoneNumberField(unique=True)

    def __str__(self):
        template = '{0.number_to_call}'
        return template.format(self)