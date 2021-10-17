from rest_framework import serializers
from .models import Devices, EoX_PID, EoX_SN, EoX_IOS, LearnACL, LearnARP, LearnARPStatistics, LearnBGPInstances, LearnBGPRoutesPerPeer, LearnBGPTables, LearnConfig, LearnInterface, LearnPlatform, LearnPlatformSlots, LearnPlatformVirtual, LearnVLAN, LearnVRF, NMAP, PSIRT, RecommendedRelease, Serial2Contract, ShowInventory, ShowIPIntBrief, ShowVersion

class DevicesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Devices
        fields = ('hostname', 'alias', 'device_type', 'os', 'username', 'protocol', 'ip_address', 'port', 'connection_timeout', 'timestamp')

class EoX_PIDSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EoX_PID
        fields = ('pyats_alias', 'os', 'pid', 'description', 'bulletin_number', 'bulletin_url', 'external_date', 'sale_date', 'sw_maintenance','security','routine_failure','service_contract','last','svc_attach','last_updated','pid_active','migration_information','migration_option','migration_pid','migration_name','migration_strat','migration_url','timestamp')

class EoX_SNSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EoX_SN
        fields = ('pyats_alias', 'os', 'pid', 'description', 'bulletin_number', 'bulletin_url', 'external_date', 'sale_date', 'sw_maintenance','security','routine_failure','service_contract','last','svc_attach','last_updated','pid_active','migration_information','migration_option','migration_pid','migration_name','migration_strat','migration_url','timestamp')

class EoX_SWSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EoX_IOS
        fields = ('pyats_alias', 'os', 'pid', 'description', 'bulletin_number', 'bulletin_url', 'external_date', 'sale_date', 'sw_maintenance','security','routine_failure','service_contract','last','svc_attach','last_updated','pid_active','migration_information','migration_option','migration_pid','migration_name','migration_strat','migration_url','timestamp')

class LearnACLSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LearnACL
        fields = ('pyats_alias', 'os', 'acl', 'ace', 'permission', 'logging', 'source_network', 'destination_network', 'l3_protocol', 'l4_protocol', 'operator', 'port', 'timestamp')

class LearnARPSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LearnARP
        fields = ('pyats_alias', 'os', 'interface', 'neighbor_ip', 'neighbor_mac', 'origin', 'local_proxy', 'proxy', 'timestamp')

class LearnARPStatisticsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LearnARPStatistics
        fields = ('pyats_alias', 'os', 'entries_total', 'in_drops', 'incomplete_total', 'timestamp')

class LearnBGPInstancesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LearnBGPInstances
        fields = ('pyats_alias', 'os', 'instance', 'bgp_id', 'protocol_state', 'nexthop_trigger_delay_critical', 'nexthop_trigger_delay_noncritical', 'nexthop_trigger_enabled', 'vrf', 'router_id', 'cluster_id', 'confederation_id', 'neighbor', 'version', 'hold_time', 'keep_alive_interval', 'local_as', 'remote_as', 'neighbor_counters_received_bytes_in_queue', 'neighbor_counters_received_capability', 'neighbor_counters_received_keepalives', 'neighbor_counters_received_notifications', 'neighbor_counters_received_opens', 'neighbor_counters_received_route_refresh', 'neighbor_counters_received_total', 'neighbor_counters_received_total_bytes', 'neighbor_counters_received_updates', 'neighbor_counters_sent_bytes_in_queue', 'neighbor_counters_sent_capability', 'neighbor_counters_sent_keepalives', 'neighbor_counters_sent_notifications', 'neighbor_counters_sent_opens', 'neighbor_counters_sent_route_refresh', 'neighbor_counters_sent_total', 'neighbor_counters_sent_total_bytes', 'neighbor_counters_sent_updates', 'last_reset', 'reset_reason', 'timestamp')

class LearnBGPRoutesPerPeerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LearnBGPRoutesPerPeer
        fields = ('pyats_alias', 'os', 'instance', 'vrf', 'neighbor', 'advertised', 'routes', 'remote_as', 'timestamp')

class LearnBGPTablesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LearnBGPTables
        fields = ('pyats_alias', 'os', 'instance', 'vrf', 'table_version', 'prefix', 'index', 'localpref', 'next_hop', 'origin_code', 'status_code', 'weight', 'timestamp')

class LearnConfigSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LearnConfig
        fields = ('pyats_alias', 'os', 'config', 'timestamp')

class LearnInterfaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LearnInterface
        fields = ('pyats_alias', 'os', 'interface', 'description', 'enabled', 'status', 'access_vlan', 'native_vlan', 'switchport', 'switchport_mode', 'interface_type', 'bandwidth', 'auto_negotiate', 'speed', 'duplex', 'mtu', 'mac_address', 'physical_address', 'ip_address', 'medium', 'delay', 'encapsulation', 'flow_control_receive', 'flow_control_send', 'port_channel', 'port_channel_member_interfaces', 'port_channel_member', 'last_change', 'input_broadcast', 'input_crc_errors', 'input_errors', 'input_mac_pause_frames', 'input_multicast', 'input_octets', 'input_unicast', 'input_unknown', 'input_total', 'output_broadcast', 'output_discard', 'output_errors', 'output_mac_pause_frames', 'output_multicast', 'output_unicast', 'output_total', 'last_clear', 'input_rate', 'load_interval', 'output_rate', 'timestamp')

class LearnPlatformSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LearnPlatform
        fields = ('pyats_alias', 'os', 'chassis', 'chassis_sn', 'disk_free_space', 'disk_total_space','disk_used_space','image','installed_packages','main_mem','rp_uptime','rtr_type','version', 'timestamp')

class LearnPlatformSlotsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LearnPlatformSlots
        fields = ('pyats_alias', 'os', 'slot', 'slot_name', 'slot_sn', 'slot_state', 'slot_redundancy_state', 'rp_boot_image', 'slot_rp_uptime', 'timestamp')

class LearnPlatformVirtualSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LearnPlatformVirtual
        fields = ('pyats_alias', 'os', 'virtual_device_name', 'virtual_device_status', 'virtual_device_member', 'virtual_device_member_status', 'virtual_device_member_type', 'timestamp')

class LearnVLANSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LearnVLAN
        fields = ('pyats_alias', 'os', 'vlan', 'interfaces', 'mode', 'name', 'shutdown', 'state', 'timestamp')

class LearnVRFSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LearnVRF
        fields = ('pyats_alias', 'os', 'vrf', 'route_distinguisher', 'timestamp')

class NMAPSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NMAP
        fields = ('pyats_alias', 'os', 'protocol', 'port', 'conf', 'cpe', 'extra_info', 'name', 'product', 'reason', 'state', 'version','timestamp')

class PSIRTSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PSIRT
        fields = ('pyats_alias', 'os', 'advisory_id', 'advisory_title', 'bug_ids', 'ips_signatures', 'cves', 'cvrf_url', 'cvss_base_score', 'cwe', 'platform_name', 'ios_release', 'first_fixed', 'first_published', 'last_updated', 'status', 'version', 'publication_url', 'sir', 'summary', 'timestamp')

class RecommendedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RecommendedRelease
        fields = ('pyats_alias', 'os', 'basePID', 'productName', 'softwareType', 'imageName', 'description', 'featureSet', 'imageSize', 'isSuggested', 'majorRelease', 'releaseTrain', 'relDispName', 'releaseDate', 'releaseLifeCycle', 'installed_version', 'compliant', 'timestamp')

class Serial2ContractSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Serial2Contract
        fields = ('pyats_alias', 'os', 'base_pid', 'customer_name', 'address', 'city', 'state_province', 'country', 'product_line_end_date', 'is_covered', 'item_description', 'item_type', 'orderable_pid', 'pillar_code', 'parent_sn', 'service_contract', 'service_description', 'serial_number', 'warranty_end', 'warranty_type', 'warranty_description', 'timestamp')

class ParseShowInventorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShowInventory
        fields = ('pyats_alias', 'os', 'part', 'description', 'pid', 'serial_number', 'timestamp')

class ParseShowIPIntBriefSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShowIPIntBrief
        fields = ('pyats_alias', 'os', 'interface', 'interface_status', 'ip_address', 'timestamp')

class ParseShowVersionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShowVersion
        fields = ('pyats_alias', 'bootflash', 'chassis', 'cpu', 'device_name', 'memory', 'model', 'processor_board_id', 'rp', 'slots', 'days', 'hours', 'minutes', 'seconds', 'name', 'os', 'reason', 'system_compile_time', 'system_image_file', 'system_version', 'chassis_sn', 'compiled_by', 'curr_config_register', 'image_id', 'image_type', 'label', 'license_level', 'license_type', 'non_volatile', 'physical', 'next_reload_license_level', 'platform', 'processor_type', 'returned_to_rom_by', 'rom', 'rtr_type', 'uptime', 'uptime_this_cp', 'version_short', 'xe_version', 'timestamp')