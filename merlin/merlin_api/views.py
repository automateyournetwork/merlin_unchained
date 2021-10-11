from rest_framework import viewsets
from merlin.serializers import DevicesSerializer, EoX_PIDSerializer, LearnACLSerializer, LearnARPSerializer, LearnARPStatisticsSerializer, LearnBGPInstancesSerializer, LearnBGPRoutesPerPeerSerializer, LearnBGPTablesSerializer, LearnConfigSerializer, LearnInterfaceSerializer, LearnPlatformSerializer, LearnPlatformSlotsSerializer, LearnPlatformVirtualSerializer, LearnVLANSerializer, LearnVRFSerializer, NMAPSerializer, PSIRTSerializer, RecommendedSerializer, Serial2ContractSerializer, ParseShowInventorySerializer, ParseShowIPIntBriefSerializer, ParseShowVersionSerializer
from merlin.models import Devices, EoX_PID, LearnACL, LearnARP, LearnARPStatistics, LearnBGPInstances, LearnBGPRoutesPerPeer, LearnBGPTables, LearnConfig, LearnInterface, LearnPlatform, LearnPlatformSlots, LearnPlatformVirtual, LearnVLAN, LearnVRF, NMAP, PSIRT, RecommendedRelease, Serial2Contract, ShowInventory, ShowIPIntBrief, ShowVersion

class DevicesViewSet(viewsets.ModelViewSet):
    queryset = Devices.objects.all().order_by('timestamp')
    serializer_class = DevicesSerializer

class EoX_PIDViewSet(viewsets.ModelViewSet):
    queryset = EoX_PID.objects.all().order_by('timestamp')
    serializer_class = EoX_PIDSerializer

class LearnACLViewSet(viewsets.ModelViewSet):
    queryset = LearnACL.objects.all().order_by('timestamp')
    serializer_class = LearnACLSerializer

class LearnARPViewSet(viewsets.ModelViewSet):
    queryset = LearnARP.objects.all().order_by('timestamp')
    serializer_class = LearnARPSerializer

class LearnARPStatisticsViewSet(viewsets.ModelViewSet):
    queryset = LearnARPStatistics.objects.all().order_by('timestamp')
    serializer_class = LearnARPStatisticsSerializer    

class LearnBGPInstancesViewSet(viewsets.ModelViewSet):
    queryset = LearnBGPInstances.objects.all().order_by('timestamp')
    serializer_class = LearnBGPInstancesSerializer

class LearnBGPRoutesViewSet(viewsets.ModelViewSet):
    queryset = LearnBGPRoutesPerPeer.objects.all().order_by('timestamp')
    serializer_class = LearnBGPRoutesPerPeerSerializer    

class LearnBGPTablesViewSet(viewsets.ModelViewSet):
    queryset = LearnBGPTables.objects.all().order_by('timestamp')
    serializer_class = LearnBGPTablesSerializer

class LearnConfigViewSet(viewsets.ModelViewSet):
    queryset = LearnConfig.objects.all().order_by('timestamp')
    serializer_class = LearnConfigSerializer

class LearnInterfaceViewSet(viewsets.ModelViewSet):
    queryset = LearnInterface.objects.all().order_by('timestamp')
    serializer_class = LearnInterfaceSerializer

class LearnPlatformViewSet(viewsets.ModelViewSet):
    queryset = LearnPlatform.objects.all().order_by('timestamp')
    serializer_class = LearnPlatformSerializer

class LearnPlatformSlotsViewSet(viewsets.ModelViewSet):
    queryset = LearnPlatformSlots.objects.all().order_by('timestamp')
    serializer_class = LearnPlatformSlotsSerializer

class LearnPlatformVirtualViewSet(viewsets.ModelViewSet):
    queryset = LearnPlatformVirtual.objects.all().order_by('timestamp')
    serializer_class = LearnPlatformVirtualSerializer        

class LearnVLANViewSet(viewsets.ModelViewSet):
    queryset = LearnVLAN.objects.all().order_by('timestamp')
    serializer_class = LearnVLANSerializer

class LearnVRFViewSet(viewsets.ModelViewSet):
    queryset = LearnVRF.objects.all().order_by('timestamp')
    serializer_class = LearnVRFSerializer

class NMAPViewSet(viewsets.ModelViewSet):
    queryset = NMAP.objects.all().order_by('timestamp')
    serializer_class = NMAPSerializer

class PSIRTViewSet(viewsets.ModelViewSet):
    queryset = PSIRT.objects.all().order_by('timestamp')
    serializer_class = PSIRTSerializer

class RecommendedViewSet(viewsets.ModelViewSet):
    queryset = RecommendedRelease.objects.all().order_by('timestamp')
    serializer_class = RecommendedSerializer

class Serial2ContractViewSet(viewsets.ModelViewSet):
    queryset = Serial2Contract.objects.all().order_by('timestamp')
    serializer_class = Serial2ContractSerializer

class ShowInventoryViewSet(viewsets.ModelViewSet):
    queryset = ShowInventory.objects.all().order_by('timestamp')
    serializer_class = ParseShowInventorySerializer

class ShowIPIntBriefViewSet(viewsets.ModelViewSet):
    queryset = ShowIPIntBrief.objects.all().order_by('timestamp')
    serializer_class = ParseShowIPIntBriefSerializer 

class ShowVersionViewSet(viewsets.ModelViewSet):
    queryset = ShowVersion.objects.all().order_by('timestamp')
    serializer_class = ParseShowVersionSerializer    