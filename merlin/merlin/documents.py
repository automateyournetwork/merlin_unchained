from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Devices, EoX_PID, EoX_SN, EoX_IOS, LearnACL, LearnARP, LearnARPStatistics, LearnBGPInstances, LearnBGPRoutesPerPeer, LearnBGPTables, LearnInterface, LearnPlatform, LearnPlatformSlots, LearnPlatformVirtual, LearnVLAN, LearnVRF, NMAP, PSIRT, RecommendedRelease, Serial2Contract, ShowInventory, ShowLicenseSummary, ShowIPIntBrief, ShowVersion

@registry.register_document
class DevicesDocument(Document):
    class Index:
        name = 'devices'
    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }
    class Django:
         model = Devices
         fields = [
             'hostname',
             'alias',
             'device_type',
             'os',
             'platform',
             'username',
             'password',
             'protocol',
             'ip_address',
             'port',
             'connection_timeout',
             'timestamp'
         ]

@registry.register_document
class EoX_PIDDocument(Document):
    class Index:
        name = 'eox_pid'
    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }
    class Django:
         model = EoX_PID
         fields = [
             'pyats_alias',
             'os',
             'pid',
             'description',
             'bulletin_number',
             'bulletin_url',
             'external_date',
             'sale_date',
             'sw_maintenance',
             'security',
             'routine_failure',
             'service_contract',
             'last',
             'svc_attach',
             'last_updated',
             'pid_active',
             'migration_information',
             'migration_option',
             'migration_pid',
             'migration_name',
             'migration_strat',
             'migration_url',
             'timestamp'
         ]

@registry.register_document
class EoX_SNDocument(Document):
    class Index:
        name = 'eox_sn'
    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }
    class Django:
         model = EoX_SN
         fields = [
             'pyats_alias',
             'os',
             'pid',
             'description',
             'bulletin_number',
             'bulletin_url',
             'external_date',
             'sale_date',
             'sw_maintenance',
             'security',
             'routine_failure',
             'service_contract',
             'last',
             'svc_attach',
             'last_updated',
             'pid_active',
             'migration_information',
             'migration_option',
             'migration_pid',
             'migration_name',
             'migration_strat',
             'migration_url',
             'timestamp'
         ]

@registry.register_document
class EoX_IOSDocument(Document):
    class Index:
        name = 'eox_ios'
    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }
    class Django:
         model = EoX_IOS
         fields = [
             'pyats_alias',
             'os',
             'pid',
             'description',
             'bulletin_number',
             'bulletin_url',
             'external_date',
             'sale_date',
             'sw_maintenance',
             'security',
             'routine_failure',
             'service_contract',
             'last',
             'svc_attach',
             'last_updated',
             'pid_active',
             'migration_information',
             'migration_option',
             'migration_pid',
             'migration_name',
             'migration_strat',
             'migration_url',
             'timestamp'
         ]

@registry.register_document
class LearnACLDocument(Document):
    class Index:
        name = 'learn_acl'
    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }
    class Django:
         model = LearnACL
         fields = [
             'pyats_alias',
             'os',
             'acl',
             'ace',
             'permission',
             'logging',
             'source_network',
             'destination_network',
             'l3_protocol',
             'l4_protocol',
             'operator',
             'port',
             'timestamp'
         ]

@registry.register_document
class LearnARPDocument(Document):
    class Index:
        name = 'learn_arp'
    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }
    class Django:
         model = LearnARP
         fields = [
             'pyats_alias',
             'os',
             'interface',
             'neighbor_ip',
             'neighbor_mac',
             'origin',
             'local_proxy',
             'proxy',
             'timestamp'
         ]

@registry.register_document
class LearnARPStatisticsDocument(Document):
    class Index:
        name = 'learn_arp_statistics'
    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }
    class Django:
         model = LearnARPStatistics
         fields = [
             'pyats_alias',
             'os',
             'entries_total',
             'in_drops',
             'in_replies_pkts',
             'in_requests_pkts',
             'incomplete_total',
             'out_replies_pkts',
             'out_requests_pkts',
             'timestamp'
         ]

@registry.register_document
class LearnBGPInstancesDocument(Document):
    class Index:
        name = 'learn_bgp_instances'
    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }
    class Django:
         model = LearnBGPInstances
         fields = [
             'pyats_alias',
             'os',
             'instance',
             'bgp_id',
             'protocol_state',
             'nexthop_trigger_delay_critical',
             'nexthop_trigger_delay_noncritical',
             'nexthop_trigger_enabled',
             'vrf',
             'router_id',
             'cluster_id',
             'confederation_id',
             'neighbor',
             'version',
             'hold_time',
             'keep_alive_interval',
             'local_as',
             'remote_as',
             'neighbor_counters_received_bytes_in_queue',
             'neighbor_counters_received_capability',
             'neighbor_counters_received_keepalives',
             'neighbor_counters_received_notifications',
             'neighbor_counters_received_opens',
             'neighbor_counters_received_route_refresh',
             'neighbor_counters_received_total',
             'neighbor_counters_received_total_bytes',
             'neighbor_counters_received_updates',
             'neighbor_counters_sent_bytes_in_queue',
             'neighbor_counters_sent_capability',
             'neighbor_counters_sent_keepalives',
             'neighbor_counters_sent_notifications',
             'neighbor_counters_sent_opens',
             'neighbor_counters_sent_route_refresh',
             'neighbor_counters_sent_total',
             'neighbor_counters_sent_total_bytes',
             'neighbor_counters_sent_updates',
             'last_reset',
             'reset_reason',
             'timestamp'
         ]

@registry.register_document
class LearnBGPRoutesPerPeerDocument(Document):
    class Index:
        name = 'learn_bgp_routes'
    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }
    class Django:
         model = LearnBGPRoutesPerPeer
         fields = [
             'pyats_alias',
             'os',
             'instance',
             'vrf',
             'neighbor',
             'advertised',
             'routes',
             'remote_as',
             'timestamp'
         ]

@registry.register_document
class LearnBGPTablesDocument(Document):
    class Index:
        name = 'learn_bgp_tables'
    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }
    class Django:
         model = LearnBGPTables
         fields = [
             'pyats_alias',
             'os',
             'instance',
             'vrf',
             'table_version',
             'prefix',
             'index',
             'localpref',
             'next_hop',
             'origin_code',
             'status_code',
             'weight',
             'timestamp'
         ]

@registry.register_document
class LearnInterfaceDocument(Document):
    class Index:
        name = 'learn_interface'
    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }
    class Django:
         model = LearnInterface
         fields = [
             'pyats_alias',
             'os',
             'interface',
             'description',
             'enabled',
             'status',
             'access_vlan',
             'native_vlan',
             'switchport',
             'switchport_mode',
             'interface_type',
             'bandwidth',
             'auto_negotiate',
             'speed',
             'duplex',
             'mtu',
             'mac_address',
             'physical_address',
             'ip_address',
             'medium',
             'delay',
             'encapsulation',
             'flow_control_receive',
             'flow_control_send',
             'port_channel',
             'port_channel_member_interfaces',
             'port_channel_member',
             'last_change',
             'input_broadcast',
             'input_crc_errors',
             'input_errors',
             'input_mac_pause_frames',
             'input_multicast',
             'input_octets',
             'input_unicast',
             'input_unknown',
             'input_total',
             'output_broadcast',
             'output_discard',
             'output_errors',
             'output_mac_pause_frames',
             'output_multicast',
             'output_unicast',
             'output_total',
             'last_clear',
             'input_rate',
             'load_interval',
             'output_rate',
             'timestamp'
         ]

@registry.register_document
class LearnPlatformDocument(Document):
    class Index:
        name = 'learn_platform'
    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }
    class Django:
         model = LearnPlatform
         fields = [
             'pyats_alias',
             'os',
             'chassis',
             'chassis_sn',
             'disk_free_space',
             'disk_total_space',
             'disk_used_space',
             'image',
             'installed_packages',
             'main_mem',
             'rp_uptime',
             'rtr_type',
             'version',
             'timestamp'
         ]

@registry.register_document
class LearnPlatformSlotsDocument(Document):
    class Index:
        name = 'learn_platform_slots'
    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }
    class Django:
         model = LearnPlatformSlots
         fields = [
             'pyats_alias',
             'os',
             'slot',
             'slot_name',
             'slot_sn',
             'slot_state',
             'slot_redundancy_state',
             'rp_boot_image',
             'slot_rp_uptime',
             'timestamp'
         ]

@registry.register_document
class LearnPlatformVirtualDocument(Document):
    class Index:
        name = 'learn_platform_virtual'
    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }
    class Django:
         model = LearnPlatformVirtual
         fields = [
             'pyats_alias',
             'os',
             'virtual_device_name',
             'virtual_device_status',
             'virtual_device_member',
             'virtual_device_member_status',
             'virtual_device_member_type',
             'timestamp'
         ]

@registry.register_document
class LearnVLANDocument(Document):
    class Index:
        name = 'learn_vlan'
    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }
    class Django:
         model = LearnVLAN
         fields = [
             'pyats_alias',
             'os',
             'vlan',
             'interfaces',
             'mode',
             'name',
             'shutdown',
             'state',
             'timestamp'
         ]

@registry.register_document
class LearnVRFDocument(Document):
    class Index:
        name = 'learn_vrf'
    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }
    class Django:
         model = LearnVRF
         fields = [
             'pyats_alias',
             'os',
             'vrf',
             'route_distinguisher',
             'timestamp'
         ]

@registry.register_document
class NMAPDocument(Document):
    class Index:
        name = 'nmap'
    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }
    class Django:
         model = NMAP
         fields = [
             'pyats_alias',
             'os',
             'protocol',
             'port',
             'conf',
             'cpe',
             'extra_info',
             'name',
             'product',
             'reason',
             'state',
             'version',
             'timestamp'
         ]

@registry.register_document
class PSIRTDocument(Document):
    class Index:
        name = 'psirt'
    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }
    class Django:
         model = PSIRT
         fields = [
             'pyats_alias',
             'os',
             'advisory_id',
             'advisory_title',
             'bug_ids',
             'ips_signatures',
             'cves',
             'cvrf_url',
             'cvss_base_score',
             'cwe',
             'platform_name',
             'ios_release',
             'first_fixed',
             'first_published',
             'last_updated',
             'status',
             'version',
             'publication_url',
             'sir',
             'summary',
             'timestamp'
         ]

@registry.register_document
class RecommendedReleaseDocument(Document):
    class Index:
        name = 'recommended_release'
    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }
    class Django:
         model = RecommendedRelease
         fields = [
             'pyats_alias',
             'os',
             'basePID',
             'productName',
             'softwareType',
             'imageName',
             'description',
             'featureSet',   
             'imageSize',
             'isSuggested',
             'majorRelease',
             'releaseTrain',
             'relDispName',
             'releaseDate',
             'releaseLifeCycle',
             'installed_version',
             'compliant',
             'timestamp'
         ]

@registry.register_document
class Serial2ContractDocument(Document):
    class Index:
        name = 'serial_2_contract'
    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }
    class Django:
         model = Serial2Contract
         fields = [
             'pyats_alias',
             'os',
             'base_pid',
             'customer_name',
             'address',
             'city',
             'state_province',
             'country',
             'product_line_end_date',
             'is_covered',
             'item_description',
             'item_type',
             'orderable_pid',
             'pillar_code',
             'parent_sn',
             'service_contract',
             'service_description',
             'serial_number',
             'warranty_end',
             'warranty_type',
             'warranty_description',
             'timestamp'
         ]

@registry.register_document
class ShowInventoryDocument(Document):
    class Index:
        name = 'show_inventory'
    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }
    class Django:
         model = ShowInventory
         fields = [
             'pyats_alias',
             'os',
             'part',
             'description',
             'pid',
             'serial_number',
             'timestamp'
         ]

@registry.register_document
class ShowIPIntBriefDocument(Document):
    class Index:
        name = 'show_ip_int_brief'
    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }
    class Django:
         model = ShowIPIntBrief
         fields = [
             'pyats_alias',
             'os',
             'interface',
             'interface_status',
             'ip_address',
             'timestamp'
         ]

@registry.register_document
class ShowLicenseSummaryDocument(Document):
    class Index:
        name = 'show_license_summary'
    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }
    class Django:
         model = ShowLicenseSummary
         fields = [
             'pyats_alias',
             'os',
             'license_name',
             'entitlement',
             'count',
             'status',
             'timestamp'
         ]

@registry.register_document
class ShowVersionDocument(Document):
    class Index:
        name = 'show_version'
    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }
    class Django:
         model = ShowVersion
         fields = [
             'pyats_alias',
             'bootflash',
             'chassis',
             'cpu',
             'device_name',
             'memory',
             'model',
             'processor_board_id',
             'rp',
             'slots',
             'days',
             'hours',
             'minutes',
             'seconds',
             'name',
             'os',
             'reason',
             'system_compile_time',
             'system_image_file',
             'system_version',
             'chassis_sn',
             'compiled_by',
             'curr_config_register',
             'image_id',
             'image_type',
             'label',
             'license_level',
             'license_type',
             'non_volatile',
             'physical',
             'next_reload_license_level',
             'platform',
             'processor_type',
             'returned_to_rom_by',
             'rom',
             'rtr_type',
             'uptime',
             'uptime_this_cp',
             'version_short',
             'xe_version',
             'timestamp'
         ]         