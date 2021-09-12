from rest_framework import serializers
from .models import LearnVLAN, LearnVRF, ShowInventory, ShowIPIntBrief, ShowVersion

class LearnVLANSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LearnVLAN
        fields = ('pyats_alias','os','vlan','interfaces','mode','name','shutdown','state','timestamp')

class LearnVRFSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LearnVRF
        fields = ('pyats_alias', 'os','vrf','address_family_ipv4','address_family_ipv6','route_distinguisher','timestamp')

class ParseShowInventorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShowInventory
        fields = ('pyats_alias','os','part','description','pid','serial_number','timestamp')

class ParseShowIPIntBriefSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShowIPIntBrief
        fields = ('pyats_alias','os','interface','interface_status','ip_address','timestamp')

class ParseShowVersionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShowVersion
        fields = ('pyats_alias','bootflash','chassis','cpu','device_name','memory','model','processor_board_id','rp','slots','days','hours','minutes','seconds','name','os','reason','system_compile_time','system_image_file','system_version','chassis_sn','compiled_by','curr_config_register','image_id','image_type','label','license_level','license_type','non_volatile','physical','next_reload_license_level','platform','processor_type','returned_to_rom_by','rom','rtr_type','uptime','uptime_this_cp','version_short','xe_version','timestamp')