from django.views.generic import TemplateView, ListView
from django.db.models import Q
from merlin.models import LearnACL, LearnARP, LearnARPStatistics, LearnVLAN, LearnVRF, ShowInventory, ShowIPIntBrief, ShowVersion

class SearchView(TemplateView):
    template_name = 'Search/search.html'

class SearchResultView(ListView):
    template_name = 'Search/Results/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = (LearnACL.objects.filter(
            Q(pyats_alias=query) | Q(os=query) | Q(acl=query) | Q(ace=query) | Q(permission=query) | Q(logging=query) | Q(source_network=query) | Q(destination_network=query) | Q(l3_protocol=query) | Q(l4_protocol=query) | Q(operator=query) | Q(port=query)
        ),LearnARP.objects.filter(
            Q(pyats_alias=query) | Q(os=query) | Q(interface=query) | Q(neighbor_ip=query) | Q(neighbor_mac=query) | Q(origin=query) | Q(local_proxy=query) | Q(proxy=query)
        ),LearnARPStatistics.objects.filter(
            Q(pyats_alias=query) | Q(os=query) | Q(entries_total=query) | Q(in_drops=query) | Q(in_replies_pkts=query) | Q(in_requests_pkts=query) | Q(incomplete_total=query) | Q(out_replies_pkts=query) | Q(out_requests_pkts=query)
        ),LearnVLAN.objects.filter(
            Q(pyats_alias=query) | Q(os=query) | Q(vlan=query) | Q(interfaces=query) | Q(mode=query) | Q(name=query) | Q(shutdown=query) | Q(state=query)
        ),LearnVRF.objects.filter(
            Q(pyats_alias=query) | Q(os=query) | Q(vrf=query) | Q(address_family_ipv4=query) | Q(address_family_ipv6=query) | Q(route_distinguisher=query)
        ),ShowInventory.objects.filter(
            Q(pyats_alias=query) | Q(os=query) | Q(part=query) | Q(description=query) | Q(pid=query) | Q(serial_number=query) 
        ),ShowIPIntBrief.objects.filter(
            Q(pyats_alias=query) | Q(os=query) | Q(interface=query) | Q(interface_status=query) | Q(ip_address=query)
        ),ShowVersion.objects.filter(
            Q(pyats_alias=query) | Q(bootflash=query) | Q(chassis=query) | Q(cpu=query) | Q(device_name=query) | Q(memory=query) | Q(model=query) | Q(processor_board_id=query) | Q(rp=query) | Q(slots=query) | Q(days=query) | Q(hours=query) | Q(minutes=query) | Q(seconds=query) | Q(name=query) | Q(os=query) | Q(reason=query) | Q(system_compile_time=query) | Q(system_image_file=query) | Q(system_version=query) | Q(chassis_sn=query) | Q(compiled_by=query) | Q(curr_config_register=query) | Q(image_id=query) | Q(image_type=query) | Q(label=query) | Q(license_level=query) | Q(license_type=query) | Q(non_volatile=query) | Q(physical=query) | Q(next_reload_license_level=query) | Q(platform=query) | Q(processor_type=query) | Q(returned_to_rom_by=query) | Q(rom=query) | Q(rtr_type=query) | Q(uptime=query) | Q(uptime_this_cp=query) | Q(version_short=query) | Q(xe_version=query) 
        )
        )

        return object_list