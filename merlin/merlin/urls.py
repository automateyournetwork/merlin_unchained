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
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ShowVersion/<int:year>/', views.show_version_year_archive),
    path('ShowVersion/<int:year>/<int:month>/', views.show_version_month_archive),
    path('ShowVersion/<int:year>/<int:month>/<int:day>/', views.show_version_day_archive),
    path('ShowVersion/<str:os>/', views.show_version_os_archive),
    path('LearnVRF/<int:year>/', views.learn_vrf_year_archive),
    path('LearnVRF/<int:year>/<int:month>/', views.learn_vrf_month_archive),
    path('LearnVRF/<int:year>/<int:month>/<int:day>/', views.learn_vrf_day_archive),
    path('LearnVRF/<str:os>/', views.learn_vrf_os_archive),    
]