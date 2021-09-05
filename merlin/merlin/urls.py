"""merlin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('OnDemand/', views.button),
    path('OnDemand/get_all_result/', views.get_all_ondemand, name="get_all"),
    path('OnDemand/learn_vlan_result/', views.learn_vlan_ondemand, name="learn_vlan"),
    path('OnDemand/learn_vrf_result/', views.learn_vrf_ondemand, name="learn_vrf"),
    path('OnDemand/show_version_result/', views.show_version_ondemand, name="show_version"),
    path('API/', include('merlin_api.urls')),
    path('ShowVersion/<int:year>/', views.show_version_year_archive),
    path('ShowVersion/<int:year>/<int:month>/', views.show_version_month_archive),
    path('ShowVersion/<int:year>/<int:month>/<int:day>/', views.show_version_day_archive),
    path('ShowVersion/<str:os>/', views.show_version_os_archive),
    path('ShowVersion/<str:os>/<str:pyats_alias>/', views.show_version_alias_archive),         
    path('LearnVRF/<int:year>/', views.learn_vrf_year_archive),
    path('LearnVRF/<int:year>/<int:month>/', views.learn_vrf_month_archive),
    path('LearnVRF/<int:year>/<int:month>/<int:day>/', views.learn_vrf_day_archive),
    path('LearnVRF/<str:os>/', views.learn_vrf_os_archive),
    path('LearnVRF/<str:os>/<str:pyats_alias>/', views.learn_vrf_alias_archive),
    path('CSV/LearnVRF/', views.learn_vrf_csv),
    path('CSV/LearnVRF/download', views.learn_vrf_csv_download, name='learn_vrf_csv'),
    path('LearnVLAN/<int:year>/', views.learn_vlan_year_archive),
    path('LearnVLAN/<int:year>/', views.learn_vlan_year_archive),
    path('LearnVLAN/<int:year>/<int:month>/', views.learn_vlan_month_archive),
    path('LearnVLAN/<int:year>/<int:month>/<int:day>/', views.learn_vlan_day_archive),
    path('LearnVLAN/<str:os>/', views.learn_vlan_os_archive),
    path('LearnVLAN/<str:os>/<str:pyats_alias>/', views.learn_vlan_alias_archive),
]