from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'LearnVLAN', views.LearnVLANViewSet)
router.register(r'LearnVRF', views.LearnVRFViewSet)
router.register(r'ShowVersion', views.ShowVersionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]