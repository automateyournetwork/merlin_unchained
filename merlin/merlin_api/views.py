from rest_framework import viewsets
from merlin.serializers import LearnACLSerializer, LearnARPSerializer, LearnARPStatisticsSerializer, LearnBGPSerializer, LearnVLANSerializer, LearnVRFSerializer, ParseShowInventorySerializer, ParseShowIPIntBriefSerializer, ParseShowVersionSerializer
from merlin.models import LearnACL, LearnARP, LearnARPStatistics, LearnBGP, LearnVLAN, LearnVRF, ShowInventory, ShowIPIntBrief, ShowVersion

class LearnACLViewSet(viewsets.ModelViewSet):
    queryset = LearnACL.objects.all().order_by('timestamp')
    serializer_class = LearnACLSerializer

class LearnARPViewSet(viewsets.ModelViewSet):
    queryset = LearnARP.objects.all().order_by('timestamp')
    serializer_class = LearnARPSerializer

class LearnARPStatisticsViewSet(viewsets.ModelViewSet):
    queryset = LearnARPStatistics.objects.all().order_by('timestamp')
    serializer_class = LearnARPStatisticsSerializer    

class LearnBGPViewSet(viewsets.ModelViewSet):
    queryset = LearnBGP.objects.all().order_by('timestamp')
    serializer_class = LearnBGPSerializer

class LearnVLANViewSet(viewsets.ModelViewSet):
    queryset = LearnVLAN.objects.all().order_by('timestamp')
    serializer_class = LearnVLANSerializer

class LearnVRFViewSet(viewsets.ModelViewSet):
    queryset = LearnVRF.objects.all().order_by('timestamp')
    serializer_class = LearnVRFSerializer

class ShowInventoryViewSet(viewsets.ModelViewSet):
    queryset = ShowInventory.objects.all().order_by('timestamp')
    serializer_class = ParseShowInventorySerializer

class ShowIPIntBriefViewSet(viewsets.ModelViewSet):
    queryset = ShowIPIntBrief.objects.all().order_by('timestamp')
    serializer_class = ParseShowIPIntBriefSerializer 

class ShowVersionViewSet(viewsets.ModelViewSet):
    queryset = ShowVersion.objects.all().order_by('timestamp')
    serializer_class = ParseShowVersionSerializer    