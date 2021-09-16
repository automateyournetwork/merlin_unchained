from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'LearnACL', views.LearnACLViewSet)
router.register(r'LearnARP', views.LearnARPViewSet)
router.register(r'LearnARPStatistics', views.LearnARPStatisticsViewSet)
router.register(r'LearnBGPInstances', views.LearnBGPInstancesViewSet)
router.register(r'LearnBGPRoutes', views.LearnBGPRoutesViewSet)
router.register(r'LearnBGPTables', views.LearnBGPTablesViewSet)
router.register(r'LearnVLAN', views.LearnVLANViewSet)
router.register(r'LearnVRF', views.LearnVRFViewSet)
router.register(r'ShowInventory', views.ShowInventoryViewSet)
router.register(r'ShowIPInterfaceBrief', views.ShowIPIntBriefViewSet)
router.register(r'ShowVersion', views.ShowVersionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]