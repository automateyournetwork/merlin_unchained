from rest_framework import viewsets
from merlin.serializers import LearnVLANSerializer, LearnVRFSerializer, ParseShowVersionSerializer
from merlin.models import LearnVLAN, LearnVRF, ShowVersion

class LearnVLANViewSet(viewsets.ModelViewSet):
    queryset = LearnVLAN.objects.all().order_by('timestamp')
    serializer_class = LearnVLANSerializer

class LearnVRFViewSet(viewsets.ModelViewSet):
    queryset = LearnVRF.objects.all().order_by('timestamp')
    serializer_class = LearnVRFSerializer

class ShowVersionViewSet(viewsets.ModelViewSet):
    queryset = ShowVersion.objects.all().order_by('timestamp')
    serializer_class = ParseShowVersionSerializer    