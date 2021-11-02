from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('Netgraph/', views.netgraph_page),
    path('Netgraph/LearnPlatform/', views.learn_platform_netgraph),
    path('Netgraph/LearnPlatform/JSON/learned_platform_netgraph.json', views.learn_platform_json),
]