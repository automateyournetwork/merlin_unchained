from django.contrib import admin

from . import models

admin.site.register(models.LearnVLAN)
admin.site.register(models.LearnVRF)
admin.site.register(models.ShowIPIntBrief)
admin.site.register(models.ShowVersion)