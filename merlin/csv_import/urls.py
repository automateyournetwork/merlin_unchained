from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from csv_import.views import device_upload

urlpatterns = [
    path('DeviceImport/', device_upload, name="device_upload"),
]