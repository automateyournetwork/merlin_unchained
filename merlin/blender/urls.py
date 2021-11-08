from django.contrib import admin
from django.urls import url, include
from . import views

urlpatterns = [
    url(r'^', include('viewer.urls')),
]